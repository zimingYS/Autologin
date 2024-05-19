import time
import os
import win32com.client
from os import path

def LoginInfo (domainInput,usernameInput,passwordInput):
    listDomain = {1:"default",2:"cmcc",3:"telecom",4:"unicom"}
    domain = listDomain.get(domainInput)
    Write(domain,usernameInput,passwordInput)
    


def Write(domain,username,password):
    from configparser import ConfigParser

# 创建配置解析器
    config = ConfigParser()

#配置默认用户信息
    config.add_section('User')
    config.set('User', 'domain', domain)
    config.set('User', 'username', username)
    config.set('User', 'password', password)

# 写入文件
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
    
print("请选择您的登录方式:")
print("1.校园网登录")
print("2.移动登录")
print("3.电信登录")
print("4.联通登录")
domainInput = int(input(">"))

print("\033c", end="")

print("请输入您的学号:")
usernameInput = input(">")
print("\033c", end="")

print("请输入您的密码:")
passwordInput = input(">")
print("\033c", end="")

LoginInfo(domainInput,usernameInput,passwordInput)
    
print("配置成功")

