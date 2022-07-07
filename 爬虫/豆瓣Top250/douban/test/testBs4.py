from bs4 import BeautifulSoup
import re
'''
# BeautifulSoup4 将复杂HTML对象转化为一个复杂的树形结构，
# 每个节点都是Python对象，所有对象都可以归纳为以下四种
- Tag 标签及其内容 <class 'bs4.element.Tag'> 默认拿找到的第一个
- NavigableString  标签里的内容 print(type(bs.title.string)) <class 'bs4.element.NavigableString'>
- BeautifulSoup 文件树 <class 'bs4.BeautifulSoup'>
- Comment 注释 ，是一个特殊的NavigableString，只显示注释中的内容，不包括注释
'''

def main1():
    file = open("./baidu.html","rb") # 如果找不到就创建，rb表示以二进制形式打开
    html = file.read()
    bs = BeautifulSoup(html,"html.parser") # 形成文件树（解析html文档用html.parser解析器
    # print(type(bs.title.string)) # bs.title 包含标签及其内容，.string 获取标签中的内容  <class 'bs4.element.NavigableString'>
    # print(bs.a.attrs) #获取 <a 中的属性
    # print(bs.title.text)  # <class 'str'>
    #eg 1
    array = bs.find_all('a')
    for i in array[0:len(array)+1]:
        print(i)
        print(i.text)
    #eg 2
    #print(bs.head.link)
    #eg 3 标签属性
    # print(bs.head.link.attrs)

'''


 
'''
def main2():
    file = open("./baidu.html","rb")
    html = file.read().decode('utf-8') # 以utf-8解码，去除\n
    bs = BeautifulSoup(html,"html.parser") # 形成文件树
    # 文档的遍历
    # print(bs.head.contents)
    # print(bs.head.contents[1])

    # 文档的搜索
    # 1、字符串过滤：会查找与字符串完全匹配的内容
    # t_list = bs.find_all("a")
    # print(t_list)
    # 2、正则表达式搜索，使用search()方法来匹配内容
    # t_list = bs.find_all(re.compile("a")) # 找到含有a字样的标签
    # print(t_list)
    # t_list = bs.find_all(text= re.compile("\d")) # 应用正则表达式来查找包含特定文本的内容(标签里的字符串)
    # 3、方法:传入一个函数（方法），根据函数的要求来搜索
    # t_list = bs.find_all(name_is_exists)
    # print(t_list)
    # for item in t_list:
    #     print(item)
    # 2.kwargs 参数
    # t_list = bs.find_all(id="head")
    # t_list = bs.find_all(class_="true")
    # print(t_list)
    # for item in t_list:
    #     print(item)
    # 4、text 参数
    # t_list = bs.find_all(text= "hao123")
    # print(t_list)
    # t_list = bs.find_all(text=["hao123","地图","贴吧"])
    # print(t_list)
    # 5、limit参数  限定返回数量
    t_list = bs.find_all("a",limit=3)
    # css 选择器
    # print(bs.select("title")) # 通过标签来查找
    t_list = bs.select(".mnav") # 通过类名来查找
    t_list = bs.select("#u1") # 通过id来查找
    t_list = bs.select("a[class='bri']") # 通过属性来查找 <a 中  class='bri' 的标签
    t_list = bs.select("head > title") # 通过子标签来查找  <head 标签中  的 <title 标签
    t_list = bs.select(".mnav ~ .bri") # 通过类名来查找    查找和.mnav 是兄弟的标签 .bri
    print(t_list[0].get_text())
    print(t_list)



def name_is_exists(tag):
    return tag.has_attr("name")
if __name__ == '__main__':
    main1()
    # main2()