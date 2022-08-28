# Dut Spider

A simple project about Web Spider made by python.

## Features

* Multi-thread Scheduling
* Persistent Storage
* Back-end Service
* Routing Registered Configuration
* Template Engine
* Performance Monitoring
* Description and Visualization
* Interactive Interface
* Command Line Tool
* Dependency Management Shell

## Usage

### Install the vital packages(Windows)

```shell
$ ./env.bat
```

### Install the vital packages(MacOS or Linux)

```shell
$ ./env.sh
```

### Start all the tasks of spider.

```shell
$ python main.py -c
```

### Render all the charts to html files.

```shell
$ python main.py -r
```

### Deploy the server

```shell
$ python main.py -d
```

### Example

```shell
$ python main.py -d
[Task: (taskName)]
......
Spider Time :(timeOfTask)s
......
$ python main.py -r
Render /(routerName)
....
$ python main.py -d
INFO:     Started server process [9092]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://localhost:8080 (Press CTRL+C to quit)
```
