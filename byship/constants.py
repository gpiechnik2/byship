from byship.files import Files


class Constants:
    def __init__(self):
        self.files = Files()

    def get_output(self, output_value, json):
        if output_value:
            if json:
                return output_value + '.json'
            return output_value

        if json:
            return self.get_json_output()
        return 'results.txt'

    def get_json_output(self):
        return 'results.json'

    def get_threads(self, threads):
        return threads if threads else 5

    def get_headers(self, headers):
        if headers:
            return self.files.get_json_data(headers)
        return None

    def get_wait_timeout(self, wait_timeout):
        return wait_timeout if wait_timeout else 2

    def get_connect_timeout(self, connect_timeout):
        return float(connect_timeout) if connect_timeout else 10.0

    def get_read_timeout(self, read_timeout):
        return float(read_timeout) if read_timeout else 10.0
