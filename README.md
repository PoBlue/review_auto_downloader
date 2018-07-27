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

## 第0步: 安装依赖库
```
pip install -r requirements.txt
```

## 用法1: Review 邮件通知
使用 Mail Gun 进行邮件通知, 不使用 QQ Mail, Gmail 的详细原因[参考这里](https://github.com/PoBlue/small_script/tree/master/python-gmail)

1. 在该项目中新建文件 `data.py`, 复制粘贴下面的信息
2. 打开 [MailGun domains](https://app.mailgun.com/app/domains)，根据图片所示，填写下面内容
```
# api key
mail_gun_api = "填写 API"

# domain
mail_domain = "填写domain"

# 接收邮件的地址
to_mail = "xxxxx@gmail.com"

# 邮件的主题
subject = "Review Robot"

# 邮件内容模板
message_template = "Hello! You have a review: {name},Price is {price} d ,language is chinese"

# mail gun 提供的 api url
gun_base_url = "填写api base url"

# 不用改
gun_url = gun_base_url + "/messages"
```

<img width="1080" alt="示意图" src="https://user-images.githubusercontent.com/9304701/43195338-61b94c82-9037-11e8-885f-a9bec7a97154.png">


3. 设置 Review 的 token, 【你的 Token】换为 Reviewer 的 Token
4. 浏览器打开 [token 链接](https://review-api.udacity.com/api/v1/me/api_token.json) (需要是登陆了 reviewer 账号的浏览器)
```
python main.py -token [你的 Token]
```

5. 终端上输入命令 `python main.py mail`. 就行了～

## 用法2: 本地自动下载项目

### 设置
1. 设置 Review 的 token, 【你的 Token】换为 Reviewer 的 Token
```
python main.py -token [你的 Token]
```

2. 设置项目的存储位置，需弄两个, 一个 src path，一个 project_path
```
python main.py -src_path /path/to/dir
python main.py -project_path /path/to/dir
```

3. 打开 Chrome, 观察并复制下载项目文件时的 **Cookie**
4. 然后新建一个文件 `cookie.txt`, 复制 **Cookie** 进去
```
#cookie
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
