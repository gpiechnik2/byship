import click

from byship.validator import Validator
from byship.asyncrunner import AsyncRunner
from byship.output import Output


@click.version_option('1.0')
@click.command()
@click.argument("url", type=str)
@click.option('--threads', '-t', default=5,
              help='Maximum number of threads at once (default 5).')
@click.option('--headers', '-h', type=str,
              help='Custom headers in JSON file.')
@click.option('--output', '-o', type=str,
              help='Results file name (default results.txt).')
@click.option('--json/--no-json', '-j/-nj', default=False,
              help='Write output in JSON format (false by default)')
@click.option('--wait-timeout', '-wt', type=int,
              help='Waiting time in seconds between threads_value requests (default 2s).')
@click.option('--connect-timeout', '-ct', type=int,
              help='The maximum amount of time to wait until a socket connection to the requested host is established (default 10s).')
@click.option('--read-timeout', '-rt', type=int,
              help='The maximum duration to wait for a chunk of data to be received (for example, a chunk of the response body) (default 10s).')
@click.option('--force/--no-force', '-f/-nf', default=False,
              help='Force running (false by default)')
def cli(url, threads, headers, output, json, wait_timeout, connect_timeout, read_timeout, force):
    """byship
    A fast, efficient and asynchronous crawler to retrieve all url's on a page.
    """

    validator = Validator(url, threads, headers, output, json, wait_timeout, connect_timeout, read_timeout, force)
    validator.validate_data()

    runner = AsyncRunner(url, threads, headers, output, json, wait_timeout, connect_timeout, read_timeout, force)
    runner.run_synchronous()
    urls = runner.get_urls()

    output_obj = Output()
    output_obj.print_total_quantity_of_urls(len(urls))


if __name__ == '__main__':
    cli()
