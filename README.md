<h1 align="center">
  <img src="static/logo.jpg" alt="portospy" width="260px"></a>
  <br>
</h1>

<h4 align="center">A fast, efficient and asynchronous crawler to retrieve all url's on a page.</h4>
      
<p align="center">
  <a href="#installation">Installation</a> •
  <a href="#commands">Commands</a> •
  <a href="#running">Running</a> •
  <a href="#running-with-docker">Running with Docker</a> •
  <a href="#license">License</a>
</p>

---
Simple asynchronous crawler written in python that obtains url's from a specified website. The project was created because none of the repositories did not meet my expectations.

# Installation

Download the repository locally
```sh
git clone https://github.com/gpiechnik2/globeexplorer.git
```

Go to the downloaded repository
```sh
cd globeexplorer
```

Install the tool locally
```sh
pip install --editable .

```

The tool can be run through Docker. Go to the [Docker session](#running-with-docker) for more information.

# Commands
```sh
globeexplorer --help
```

Here are all the flags it supports.

| Flag                        | Description                                                                                                               |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| -t, --threads               | Maximum number of threads at once                                                                                         |
<!-- | -od, --other-domains        | -->
| -h, --headers               | Custom headers in json file                                                                                               |
| -o, --output                | Results file name (default results.txt)                                                                                   |
| -j, --json / -nj, --no-json | Write output in JSON format (false by default)                                                                            |
| -wt, --wait-timeout         | Waiting time in seconds between threads_value requests (default 2s)                                                       |
| -ct, --connect-timeout      | The maximum amount of time to wait until a socket connection to the requested host is established (default 10s)           |
| -rt, --read-timeout         | The maximum duration to wait for a chunk of data to be received (for example, a chunk of the response body) (default 10s) |

# Running
To use the tool, use the following command:

```console

```

In the meantime the url file will be generated.

# Running with Docker
Build a docker image:

```
docker build -t portos -f Dockerfile . 
```

Then get the IMAGE_ID with the `docker images` command and run the tool with it.
```
docker run -it IMAGE_ID https://example.com
```

# License
