"""
base function
"""
import os
import zipfile
import urllib.request
import socket
import requests
from mail import send_of_mail
from http.cookies import SimpleCookie
socket.setdefaulttimeout(100)


def convertCookie(cookieStr):
    cookie = SimpleCookie()
    cookie.load(cookieStr)

    # Even though SimpleCookie is dictionary-like, it internally uses a Morsel object
    # which is incompatible with requests. Manually construct a dictionary instead.
    cookies = {}
    for key, morsel in cookie.items():
        cookies[key] = morsel.value
    return cookies


def move_file(from_path, to_path):
    """
    move file from from_path to to_path
    """
    os.rename(from_path, to_path)


def unzip_file(file_path, extract_path):
    """
    unzip file, and return the unzip file name
    """
    file_name = "do not know"
    with open(file_path, 'rb') as f:
        z = zipfile.ZipFile(f)
        file_name = z.namelist()[0]
        for name in z.namelist():
            z.extract(name, extract_path)
        z.close()
    return file_name


def mailToOmniFocus(review_id, review_name, price, review_link, file_name):
    """
    添加到of上
    """
    #弄好信息
    note = """
--------------------------
    {review_name}
    - [Price] {price} 刀
--------------------------
    - [File]  {file_name}
    - [Link] {review_link}
--------------------------
    - [ID] {review_id}
--------------------------
    """.format(review_name=review_name, price=price, file_name=file_name, 
                review_link=review_link, review_id=review_id)
    
    task_name = "【Review】 {name}".format(name=review_name)
    #发送邮件到 of。名字为 reivew name
    send_of_mail(note, task_name)
    return None


def download_file(url):
    """
    download file with url
    """
    local_filename = "review-archive.zip"
    while True:
        try:
            print('start download')
            # 读取 Cookie
            with open('cookie.txt', 'r') as myfile:
                cookie_data = myfile.read()
            
            cookie = convertCookie(cookie_data)
            file_r = requests.get(url, cookies=cookie)

            if file_r.status_code != 200:
                print("Error: can not get file from url")
                print(file_r.content)
                print("-"*8)

            open(local_filename, 'wb').write(file_r.content)
            break
        except Exception as error:
            print("timeout and restart, can not download {0}, Error: {1}"
                  .format(url, error))
    return local_filename


def notify(title, subtitle, message):
    """
    notify with a message in Mac
    """
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    sound = '-sound default'
    os.system('terminal-notifier {}'.format(' '.join([m, t, s, sound])))


def main():
    mailToOmniFocus("21", "test", "20", "http://test", "test/")
    pass

if __name__ == '__main__':
    main()