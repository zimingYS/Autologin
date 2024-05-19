import requests
import json
from configparser import ConfigParser

#读取文件
config = ConfigParser()
config.read('config.ini')
domain = config.get('User','domain')
username = config.get('User','username')
password = config.get('User','password')


#登录地址
post_addr="http://10.255.254.13/api/portal/v1/login"

#构造头部信息
post_header={
'Accept': 'application/json, text/javascript, */*; q=0.01',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
'Connection': 'keep-alive',
'Content-Length': '64',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Host': '10.255.254.13',
'Origin': 'http://10.255.254.13',
'Referer': 'http://10.255.254.13/portal/index.html?v=202102142343',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
'X-Requested-With': 'X-Requested-With: XMLHttpRequest'
}

#构造登录数据
post_data={"domain":domain,
           "username":username,
           "password":password}

#发送post请求登录网页
data = json.dumps(post_data)
requests.post(post_addr,data=data,headers=post_header)