from datetime import datetime


class Output:
    def __init__(self):
        self.PURPLE = '\u001b[38;5;93m'
        self.OFF = '\033[0m'
        self.RED = '\u001b[38;5;124m'
        self.GREEN = '\u001b[38;5;35m'
        self.YELLOW = '\u001b[33m'
        
    def red(self, text):
        return "{}{}{}".format(
            self.RED,
            text,
            self.OFF
        )

    def green(self, text):
        return "{}{}{}".format(
            self.GREEN,
            text,
            self.OFF
        )

    def purple(self, text):
        return "{}{}{}".format(
            self.PURPLE,
            text,
            self.OFF
        )

    def yellow(self, text):
        return "{}{}{}".format(
            self.YELLOW,
            text,
            self.OFF
        )
    
    def print_logo(self):
        print(" ")
        print(" {}                 __     __        ".format(self.purple('__')))
        print("{}--.--.-----.|  |--.|__|.-----.".format(self.purple('|  |--.')))
        print("{}  |  |__ --||     ||  ||  _  |".format(self.purple('|  _  |')))
        print("{}___  |_____||__|__||__||   __| v1.0 by @gpiechnik2".format(self.purple('|_____|')))
        print("      |_____|                 |__|   ")
        print(" ")

    def get_time(self):
        return datetime.now().strftime("%H:%M:%S")

    def get_purple_semicolon(self):
        return self.purple(';')

    def print_info(self, url, domain, threads, headers, output, json, wait_timeout, connect_timeout, read_timeout, force):
        purple_semicolon = self.get_purple_semicolon()
        print('{} [{}] {} {} {} {} {} {} {} {} {}'.format(
            self.purple('◉'),
            self.get_time(),
            'url: {}{}'.format(self.purple(url), purple_semicolon),
            'domain: {}{}'.format(self.purple(domain), purple_semicolon),
            'headers: {}{}'.format(self.purple(headers), purple_semicolon),
            'output: {}{}'.format(self.purple(output), purple_semicolon),
            'json: {}{}'.format(self.purple(json), purple_semicolon),
            'wait timeout: {} seconds{}'.format(self.purple(wait_timeout), purple_semicolon),
            'connect timeout: {} seconds{}'.format(self.purple(connect_timeout), purple_semicolon),
            'read timeout: {} seconds{}'.format(self.purple(read_timeout), purple_semicolon),
            'force: {}{}\n'.format(self.purple(force), purple_semicolon)
        ))

    def print_timeout_exceed(self, timeout_type, timeout_value, url):
        purple_semicolon = self.get_purple_semicolon()
        print('{} [{}] {}{}'.format(
            self.purple('◉'),
            self.get_time(),
            '{} Perhaps increasing the value of {} will help. Current value: {}{} Url: {}'.format(
                self.red('The timeout for waiting has been exceeded.'), self.purple((timeout_type)), self.purple(str(timeout_value)), purple_semicolon, self.purple(url)
            ),
            purple_semicolon
        ))
    
    def print_current_quantity_of_urls(self, urls_quantity):
        purple_semicolon = self.get_purple_semicolon()
        print('{} [{}] {}{}'.format(
            self.purple('◉'),
            self.get_time(),
            'Currently has been scraped: {} urls'.format(urls_quantity),
            purple_semicolon
        ))

    def print_total_quantity_of_urls(self, urls_quantity):
        purple_semicolon = self.get_purple_semicolon()
        print('{} [{}] {}{}'.format(
            self.purple('◉'),
            self.get_time(),
            'Total number of scraped urls: {}'.format(self.purple(urls_quantity)),
            purple_semicolon
        ))

    def print_validation_error_and_exit(self, error):
        purple_semicolon = self.get_purple_semicolon()
        print('{} [{}] {}{}'.format(
            self.purple('◉'),
            self.get_time(),
            self.red(error),
            purple_semicolon
        ))
        exit()

    def print_validation_warning(self, warning):
        purple_semicolon = self.get_purple_semicolon()
        print('{} [{}] {}{}'.format(
            self.purple('◉'),
            self.get_time(),
            self.yellow(warning),
            purple_semicolon
        ))

    def print_output_file_created(self, output_value):
        purple_semicolon = self.get_purple_semicolon()
        print('{} [{}] {}{}'.format(
            self.purple('◉'),
            self.get_time(),
            "The file with the scraped urls has been created. Its name is: {}. You can open it at any time and see the list of url's which is updating all the time. If you stop the program, it will not delete the file".format(
                self.purple(output_value)
            ),
            purple_semicolon
        ))
