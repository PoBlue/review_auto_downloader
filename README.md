# review_auto_downloader

- ***以前:*** 打开 Review -> 点击下载项目 -> 等待 -> 解压移到相应文件夹，循环 n 次
- ***现在:*** 设置 -> 命令，只需 1 次。

## 功能

当获取到新的 Review 时，自动下载 Review 里的项目，并提醒

![提醒图片](http://oqyjxfpox.bkt.clouddn.com/17-6-3/17826225.jpg)

## 需要环境
1. [安装 clint](https://github.com/kennethreitz/clint)
2. [安装 terminal-notifier](https://github.com/julienXX/terminal-notifier)
3. Python 3


## 使用

### 设置
设置 Review 的 token, 【你的 Token】换为 Reviewer 的 Token
```
python main.py -token [你的 Token]
```

设置项目的存储位置，需弄两个, 一个 src path，一个 project_path
```
python main.py -src_path /path/to/dir
python main.py -project_path /path/to/dir
```

### 开始
设置好后，用以下命令开始
```
python main.py start
```

### 更多
下面的命令，提示有哪些命令能帮助你
```
python main.py help
```
