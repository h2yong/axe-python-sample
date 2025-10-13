# [celery](https://github.com/celery/celery)分布式任务队列 sample

- [celery分布式任务队列 sample](#celery分布式任务队列-sample)
  - [windows 执行 celery 命令](#windows-执行-celery-命令)
    - [使用 solo 作为`perfork pool`](#使用-solo-作为perfork-pool)
    - [使用 Threads 作为`perfork pool`](#使用-threads-作为perfork-pool)
    - [使用gevent作为`perfork pool`](#使用gevent作为perfork-pool)
    - [使用eventlet作为`perfork pool`](#使用eventlet作为perfork-pool)
  - [调度分布式函数](#调度分布式函数)
  - [参考文档](#参考文档)

## windows 执行 celery 命令

> 注意：在 Windows 下，需要指定以下`perfork pool`如`-P gevent`后 celery 才能触发执行，否则 celery 收到任务但不执行，也就是说不会有任务执行结果。

### 使用 solo 作为`perfork pool`

> 单进程执行, 即在 worker 所在的进程和线程上处理任务，严格来说，他不算一个 pool.

1.执行命令: `celery -A celery_task worker -P solo --loglevel=info`

### 使用 Threads 作为`perfork pool`

> Threads pool 线程池类型中的线程由操作系统内核直接管理，只要 Python 的 ThreadPoolExector 支持 Windows 线程，这种池类型就可以在 Windows 上工作，推荐使用在 IO 负载的场景.

1.执行命令: `celery -A celery_task worker -P threads --loglevel=info --concurrency=4`

### 使用[gevent](http://sdiehl.github.io/gevent-tutorial/)作为`perfork pool`

> gevent 是一个基于协程的 Python 网络库，它使用 greenlet 在 libev 或 libuv 事件循环之上提供高级同步 API。gevent 实现了 python 标准库里面大部分的阻塞式系统调用，包括 socket、ssl、threading 和 select 等模块，可以使用 "猴子补丁" 将这些阻塞式调用变为协作式运行。

1. 安装 gevent 依赖包: `pip install gevent`
2. 执行命令: `celery -A celery_task worker -P gevent --loglevel=info --concurrency=4`

### 使用[eventlet](https://github.com/eventlet/eventlet)作为`perfork pool`

> eventlet 是一个基于 greenlet 的 Python 并发网络库，它使用非阻塞 I/O 和轻量级协程 greenlet 来实现高效的并发。

1. 安装 gevent 依赖包: `pip install eventlet`
2. 执行命令: `celery -A celery_task worker -P eventlet --loglevel=info --concurrency=4`

## 调度分布式函数

`python celery_sample.py`

运行后, 通过 redis 客户端即可查看此次任务存放的 result 结果。

## 参考文档

- https://beltxman.com/4176.html
- https://celery-doc-chinese.oubing.site/zh-cn/latest/
