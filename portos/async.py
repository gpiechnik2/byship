import asyncio
import httpx
import re
from time import sleep


# parameters
timeout = httpx.Timeout(10.0, connect=10.0, read=10.0)
limits = httpx.Limits(max_connections=5)
client = httpx.AsyncClient(limits=limits)
headers = None
wait = 2

# data storage
urls = []
urls_to_crawl = []

async def get_https_url(url):
    if 'http' not in url:
        return 'https://' + url
    return url

async def get_urls_from_string(inputString):
    regex = r"\b((?:https?://)?(?:(?:www\.)?(?:[\da-z\.-]+)\.(?:[a-z]{2,6})|(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)|(?:(?:[0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,7}:|(?:[0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,5}(?::[0-9a-fA-F]{1,4}){1,2}|(?:[0-9a-fA-F]{1,4}:){1,4}(?::[0-9a-fA-F]{1,4}){1,3}|(?:[0-9a-fA-F]{1,4}:){1,3}(?::[0-9a-fA-F]{1,4}){1,4}|(?:[0-9a-fA-F]{1,4}:){1,2}(?::[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:(?:(?::[0-9a-fA-F]{1,4}){1,6})|:(?:(?::[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(?::[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(?:ffff(?::0{1,4}){0,1}:){0,1}(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(?:[0-9a-fA-F]{1,4}:){1,4}:(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])))(?::[0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])?(?:/[\w\.-]*)*/?)\b"
    matches = re.findall(regex, inputString)
    return matches

async def add_url_from_response(response, domain):
    matches = await get_urls_from_string(response)
    for match in matches:
        match_http = await get_https_url(match)
        if domain in match_http and match_http not in urls:
            urls.append(match_http)
            urls_to_crawl.append(match_http)

async def delete_from_urls_to_crawl(url):
    if url in urls_to_crawl:
        urls_to_crawl.remove(url)

async def async_request(domain, url):
    async with httpx.AsyncClient(limits=limits) as client:
        await delete_from_urls_to_crawl(url)
        try:
            r = await client.get(url, follow_redirects=True, timeout=timeout, headers=headers)
            await add_url_from_response(r.text, domain)
        except httpx.ReadTimeout:
            print('Error while handling {}. Maybe you should increase timeout?'.format(url))

async def main(domain, url):
    urls.append(url)
    urls_to_crawl.append(url)
    while len(urls_to_crawl) > 0:
        if len(urls_to_crawl) > 5:
            request_list = [asyncio.create_task(async_request(domain, url)) for url in urls_to_crawl[:5]]
            print('A crawlowac bede: {}'.format([url for url in urls_to_crawl[:5]]))
        else:
            request_list = [asyncio.create_task(async_request(domain, url)) for url in urls_to_crawl[:len(urls_to_crawl)]]
            print('B crawlowac bede: {}'.format([url for url in urls_to_crawl[:len(urls_to_crawl)]]))
        
        sleep(wait)
        await asyncio.gather(*request_list)

if __name__ == '__main__':
    asyncio.run(main('thenewlook.pl', 'https://thenewlook.pl'))
