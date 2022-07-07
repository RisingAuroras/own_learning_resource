#-*- codeing = utf-8 -*-
#encoding=utf-8
import sys
import io
from bs4 import BeautifulSoup # 网页解析：获取数据
import re # 正则表达式
#import urllib # 指定url 获取网络数据
import urllib.request
import urllib.parse
import urllib.error
import xlwt # Excel操作
import sqlite3 # 进行SQLite数据库操作的

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

# 影片详情的规则
findLink = re.compile(r'<a href="(.*?)">') # 创建正则表达式对象，表示规则（字符串模式）
# 影片图片
findImgSrc = re.compile(r'<img .*src="(.*?)"',re.S) # re.S 让换行符包含在字符中
# 影片片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
# 影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
# 影片概况
findInq = re.compile(r'<span class="inq">(.*)</span>',re.S)
# 影片相关内容
findBd = re.compile(r'<p class="">(.*?)</p>',re.S) # re.S忽视换行符

def main():
    baseurl = 'https://movie.douban.com/top250?start='
    #爬取网页
    dataList = getData(baseurl)
    #保存数据
    # savePath = '.\\豆瓣电影Top250.xls'
    dbPath = "movie250.db"

    # saveData(dataList,savePath)
    saveDataToDB(dataList,dbPath)
#3、保存数据
def saveData(dataList,savePath):
    book = xlwt.Workbook(encoding="utf-8",style_compression=0) # 创建workbook对象
    sheet = book.add_sheet('豆瓣电影Top250',cell_overwrite_ok=True) # 创建工作表
    col = ("电影详情链接","图片链接","影片中文名","影片外国名","评分","评价数","概括","相关信息")
    for i in range(0,8):
        sheet.write(0,i,col[i]) #列名
    for i in range(0,250):
        print("第%d条" % i)
        data = dataList[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])

    book.save(savePath)


def saveDataToDB(dataList,dbPath):
    try:
        initDB(dbPath)
    except sqlite3.Error as e:
        print(e)
    conn = sqlite3.connect(dbPath)
    cursor = conn.cursor()
    for i in dataList:
        sql = r'insert into `movie250`(`info_link`,`pic_link`,`cname`,`ename`,`score`,' \
                  '`rated`,`introduction`,`info`) values("'+i[0]+'","'+i[1]+'","'+i[3]+'","'+i[3]+\
                '",'+str(i[4])+','+str(i[5])+',"'+i[6]+'","'+i[7]+'")'
        print(sql)
        cursor.execute(sql)

    conn.commit()
    conn.close()



def initDB(dbPath):
    sql = '''
        create table movie250
        (
            id integer primary key autoincrement,
            info_link text,
            pic_link text,
            cname varchar,
            ename varchar,
            score numeric,
            rated numeric,
            introduction text,
            info text
        );
    '''
    conn = sqlite3.connect(dbPath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()


# 得到一个指定url的网页内容 # ask("https://www.douban.com/")#ask("https://movie.douban.com/top250?start=")
def ask(url):
    # 模拟浏览器头部信息，想豆瓣服务器发送消息
    headers = {
        # 用户代理：告诉豆瓣服务器 我们是什么类型的机器 浏览器（本质上是告诉服务器，我们可以接受什么类型的内容）
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
    }
    req = urllib.request.Request(url,headers=headers)
    html = ''
    try:
        response = urllib.request.urlopen(req)
        html = response.read().decode('utf-8')
        # writeToFile('C:\\Users\\24278\\Desktop',html)
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print("code: " + e.code)
        if hasattr(e,"reason"):
            print("reason: " + e.reason)
    return html


#写入文件
def writeToFile(path,info):
    with open(path + '\\b.html', "w",encoding='utf-8') as file_object:
        file_object.write(info)


# 爬取网页
def getData(baseurl):
    dataList = []

    for i in range(0,250,25):
        url = baseurl + str(i)
        html = ask(url) # 保存获取到的网页源码
        # 逐一解析数据
        soup = BeautifulSoup(html,"html.parser") # 使用html解析器
        for item in soup.find_all('div',class_='item'): # 查找符合要求的字符串，形成列表 (class=item的div
            # writeToFile('C:\\Users\\24278\\Desktop',item.text)
            # print(item) 电影item信息
            data = [] # 保存一部电影的所有信息
            item = str(item)
            # 影片详情的链接
            link = re.findall(findLink,item)[0] # re库用来通过正则表达式来查找指定的字符串(第一个参数是规则，第二个是需要匹配的信息）
            data.append(link) # 添加链接

            imgSrc = re.findall(findImgSrc,item)[0]
            data.append(imgSrc) # 添加图片

            titles = re.findall(findTitle,item) # 片名可能只有一个中文名，没有外国名
            if(len(titles) == 2):
                ctitle = titles[0]
                data.append(ctitle) # 添加中文名
                otitle = titles[1].replace("/","")
                data.append(otitle) # 添加外国名
            else:
                data.append(titles[0])
                data.append(' ') # 外国名字 留空



            rating = re.findall(findRating,item)
            if(len(rating) == 1):
                data.append(rating[0]) # 评分
            else:
                data.append(' ')

            judgeNum = re.findall(findJudge,item)[0]
            data.append(judgeNum) # 评价人数

            inq = re.findall(findInq,item)
            if(len(inq) == 0):
                data.append(" ")
            else:
                data.append(inq[0].replace("。",'')) # 概述

            bd = re.findall(findBd,item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?'," ",bd) # 去掉<br/>
            bd = re.sub('/'," ",bd) # 去掉/
            data.append(bd.strip()) # 去掉前后空格

            dataList.append(data)

    print(dataList)
    return dataList

if __name__ == '__main__':  #当程序执行时(函数入口)
    #调用函数
    main()