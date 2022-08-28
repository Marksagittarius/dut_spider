# Dut Spider

一个使用Python编写的简单Web爬虫项目



## Features

* 多线程调度
* 持久化存储
* 后端服务
* 注册路由
* 模板引擎
* 性能监控
* 可视化渲染
* 交互式界面
* 命令行工具
* 依赖配置脚本



## Usage



### 安装依赖(windows)

```shell
$ ./env.bat
```



### 安装依赖 (MacOS or Linux)

```shell
$ ./env.sh
```



### 爬取所有网页数据

```shell
$ python main.py -c
```



### 将本地json渲染成html

```shell
$ python main.py -r
```





### 启动服务器

```shell
$ python main.py -d
```





## Example

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

也可以直接使用所有选项

```shell
$ python main.py -crd
...
INFO:     Started server process [9092]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://localhost:8080 (Press CTRL+C to quit)
```



服务器会运行在本地的8080端口，直接访问只会得到一个空的`json`, 有三个路由，分别对应着一，二，三题的作业

- http://localhost:8080/actress
- http://localhost:8080/television
- http://localhost:8080/epidemic