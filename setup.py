from setuptools import setup, find_packages

setup(
    name='byship',
    version='1.0',
    description='A fast, efficient and asynchronous crawler to scrape all urls on a page',
    author='@gpiechnik2',
    packages=find_packages(
        exclude=[
            "byship",
            "results.json",
            "results.txt"
        ]
    ),
    include_package_data=True,
    install_requires=[
        'asyncio',
        'httpx',
    ],
    entry_points={
        'console_scripts': [
            'byship = byshipcli:cli',
        ],
    },
)
