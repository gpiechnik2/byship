import asyncio
import httpx
from time import sleep

from byship.utils import get_main_domain, get_https_url, get_urls_from_string
from byship.constants import Constants
from byship.output import Output
from byship.files import Files


class AsyncRunner:
    def __init__(self, url, threads, headers, output_value, json, wait_timeout, connect_timeout, read_timeout, force):
        self.constants = Constants()
        self.output = Output()

        self.url = url
        self.domain = get_main_domain(self.url)
        self.threads = self.constants.get_threads(threads)
        self.headers = self.constants.get_headers(headers)
        self.output_value = self.constants.get_output(output_value, json)
        self.json = json
        self.wait_timeout = self.constants.get_wait_timeout(wait_timeout)
        self.connect_timeout = self.constants.get_connect_timeout(connect_timeout)
        self.read_timeout = self.constants.get_read_timeout(read_timeout)
        self.force = force

        self.timeout = httpx.Timeout(10.0, connect=self.connect_timeout, read=self.read_timeout)
        self.limits = httpx.Limits(max_connections=self.threads)
        self.client = httpx.AsyncClient(limits=self.limits)

        self.urls = []
        self.urls_to_crawl = []
        self.files = Files()

    async def add_url_from_response(self, response):
        matches = get_urls_from_string(self.domain, response)
        for match in matches:
            match_http = get_https_url(match)
            if self.domain in match_http and match_http not in self.urls:
                self.urls.append(match_http)
                self.urls_to_crawl.append(match_http)
                self.files.append_url_to_output_file(match_http, self.output_value)

    async def delete_from_urls_to_crawl(self, url):
        if url in self.urls_to_crawl:
            self.urls_to_crawl.remove(url)

    async def async_request(self, url):
        async with httpx.AsyncClient(limits=self.limits) as client:
            await self.delete_from_urls_to_crawl(url)
            try:
                r = await client.get(url, follow_redirects=True, timeout=self.timeout, headers=self.headers)
                await self.add_url_from_response(r.text)
            except httpx.ReadTimeout:
                self.output.print_timeout_exceed('read_timeout', self.read_timeout, url)
            except httpx.ConnectTimeout:
                self.output.print_timeout_exceed('connect_timeout', self.connect_timeout, url)
            except httpx.ConnectError:
                pass

    async def main(self, url):
        self.urls.append(url)
        self.files.append_url_to_output_file(url, self.output_value)
        self.urls_to_crawl.append(url)
        while len(self.urls_to_crawl) > 0:
            if len(self.urls_to_crawl) > 5:
                request_list = [asyncio.create_task(self.async_request(url)) for url in self.urls_to_crawl[:5]]
            else:
                request_list = [asyncio.create_task(self.async_request(url)) for url in self.urls_to_crawl[:len(self.urls_to_crawl)]]
            
            sleep(self.wait_timeout)
            await asyncio.gather(*request_list)

    def run_synchronous(self):
        self.output.print_logo()
        self.output.print_info(self.url, self.domain, self.threads, self.headers, self.output_value, self.json, self.wait_timeout, self.connect_timeout, self.read_timeout, self.force)
        self.files.create_output_file(self.output_value)
        self.output.print_output_file_created(self.output_value)

        asyncio.run(self.main(self.url))
    
    def get_urls(self):
        return self.urls
