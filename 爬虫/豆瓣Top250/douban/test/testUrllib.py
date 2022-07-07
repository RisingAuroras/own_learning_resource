#-*- codeing = utf-8 -*-
import urllib.request
import urllib.parse

# # 获取一个get请求
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8')) # 对获取到的网页源码以utf-8的格式解码

# 获取一个post请求

# data = bytes(urllib.parse.urlencode({'hello':'world'}),encoding= 'utf-8')# parse解析为二进制封装到data里
# reponse = urllib.request.urlopen('http://httpbin.org/post',data= data)
# print(reponse.read().decode('utf-8'))

# 超时处理
# try:
#     reponse = urllib.request.urlopen('https://bbksmile.blog.csdn.net/',timeout=3)
#     print(reponse.read().decode('utf-8'))
# except urllib.error.URLError as e:
#     print("Time Out")


# reponse = urllib.request.urlopen('https://baidu.com',timeout=3)
# print(reponse.status) # 获取状态码
# print(reponse.getheaders())# 获取请求头
# print(reponse.getheader('Server')) #获取请求头中的一个属性



# urlTest = 'http://httpbin.org/post'
# headersTest = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}
# data = bytes(urllib.parse.urlencode({'start':'1'}),encoding='utf-8')
# req = urllib.request.Request(url=urlTest,data=data,headers=headersTest,method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode())



#获取豆瓣网页信息
url = "https://www.douban.com"
headers={
# 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
# 'Accept-Encoding': 'gzip, deflate, br',
# 'Accept-Language':"zh-CN,zh;q=0.9",
# 'Cache-Control': 'max-age=0',
# 'Connection': 'keep-alive',
# 'Cookie': 'bid=WvCKPOxo2UA; __utmc=30149280; __utmz=30149280.1611970261.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ll="118229"; __utmc=223695111; __utmz=223695111.1611970264.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _vwo_uuid_v2=DE41D4FCE342866E2B1B73516D51BE55F|cd06f05cbe10ebbc5a5fef334315dfcc; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.1433202331.1611970261.1612006969.1612013859.5; __utmb=30149280.0.10.1612013859; __utma=223695111.821023340.1611970264.1612006969.1612013859.5; __utmb=223695111.0.10.1612013859; _pk_id.100001.4cf6=b4d9190519571dde.1611970260.5.1612013866.1612006969.',
# 'Host': 'movie.douban.com',
# 'Sec-Fetch-Dest': 'document',
# 'Sec-Fetch-Mode': 'navigate',
# 'Sec-Fetch-Site': 'none',
# 'Sec-Fetch-User': '?1',
# 'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
}
req = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(req,timeout=3)
print(response.read().decode('utf-8'))