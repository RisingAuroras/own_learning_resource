#-*- codeing = utf-8 -*-
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import re


# 爬取网络图片链接
findArticleLink = re.compile(r'<a href="(.*?)">') # 创建正则表达式对象，表示规则（字符串模式）
findImgLink = re.compile(r'<div class="imgbox".*style="background-image:url\((.*?)\)">')



def ask(url):
    try:
        headers = {
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
        req = urllib.request.Request(url=url, headers=headers)
        response = urllib.request.urlopen(req,timeout=3)
        html = response.read().decode('utf-8')
        return html
    except urllib.error.URLError as e:
        print("Time out")

def main():
    url = "https://imeizi.me/article/1072/"
    html = ask(url)
    dataList = []
    writeToFile(r'C:\Users\auroras\Desktop\data1.html', html)
    exit(0)
    soup = BeautifulSoup(html,"html.parser")
    htmlData = soup.find_all("article",class_="excerpt excerpt-c5")
    # print(dataList[0])
    for item in htmlData:
        item = str(item)
        articleLink = re.findall(findArticleLink,item)[0]
        CoverLink = re.findall(findImgLink,item)[0]
        dataList.append((articleLink,CoverLink))
    for i in dataList:
        print(i[0] + "  " + i[1])


        # print(item)

#写入文件
def writeToFile(path,info):
    with open(path, "w",encoding='utf-8') as file_object:
        file_object.write(info)

if __name__ == '__main__':
    main()