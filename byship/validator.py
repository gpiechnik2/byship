from os.path import exists

from byship.output import Output
from byship.constants import Constants


class Validator:
    def __init__(self, url, threads, headers, output_value, json, wait_timeout, connect_timeout, read_timeout, force):
        self.constants = Constants()
        self.output = Output()

        self.url = url
        self.threads = self.constants.get_threads(threads)
        self.headers = self.constants.get_headers(headers)
        self.output_value = self.constants.get_output(output_value, json)
        self.wait_timeout = self.constants.get_wait_timeout(wait_timeout)
        self.connect_timeout = self.constants.get_connect_timeout(connect_timeout)
        self.read_timeout = self.constants.get_read_timeout(read_timeout)
        self.force = force

    def _validate_url(self):
        if 'http://' not in self.url and 'https://' not in self.url:
            self.output.print_validation_error_and_exit('Define a valid url with http or https protocol')

    def _validate_threads(self):
        if self.threads < 1:
            self.output.print_validation_error_and_exit('The number of threads must not be less than 1')
    
    def _validate_headers(self):
        if self.headers:
            file_exists = exists(self.headers)
            if not file_exists:
                self.output.print_validation_error_and_exit('Headers file with path {} does not exist'.format(
                    self.headers
                ))

    def _validate_output(self):
        if self.output_value:
            if not self.force:
                file_exists = exists(self.output_value)
                if file_exists:
                    self.output.print_validation_error_and_exit('The url file exists in the current folder under the name {}. If you want to force the tool to remove it and run a scan, add the --force flag'.format(
                        self.output_value
                    ))

    def _validate_wait_timeout(self):
        if self.wait_timeout <= 0:
            self.output.print_validation_error_and_exit('Wait timeout cannot take values smaller or equal to 0. Current value: {}'.format(
                self.wait_timeout
            ))
        if self.wait_timeout > 10:
            self.output.print_validation_warning('Wait timeout is very large and can slow down tests. Current value: {}'.format(
                self.wait_timeout
            ))

    def _validate_connect_timeout(self):
        if self.connect_timeout <= 0:
            self.output.print_validation_error_and_exit('Connect timeout cannot take values smaller or equal to 0. Current value: {}'.format(
                self.connect_timeout
            ))
        if self.connect_timeout > 60.0:
            self.output.print_validation_warning('Connect timeout is very large and can slow down tests. Current value: {}'.format(
                self.connect_timeout
            ))

    def _validate_read_timeout(self):
        if self.read_timeout <= 0:
            self.output.print_validation_error_and_exit('Read timeout cannot take values smaller or equal to 0. Current value: {}'.format(
                self.read_timeout
            ))
        if self.read_timeout > 60.0:
            self.output.print_validation_warning('Read timeout is very large and can slow down tests. Current value: {}'.format(
                self.read_timeout
            ))

    def validate_data(self):
        self._validate_url()
        self._validate_threads()
        self._validate_headers()
        self._validate_output()
        self._validate_wait_timeout()
        self._validate_connect_timeout()
        self._validate_read_timeout()
