import urllib.request
import urllib.parse

#写入文件
def writeToFile(path,info):
    with open(path + '\\b.html', "w",encoding='utf-8') as file_object:
        file_object.write(info)


def main():
    url = 'https://www.bilibili.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
    }
    req = urllib.request.Request(url=url,headers=headers)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf--8')
    writeToFile('C:\\Users\\24278\\Desktop',html)
    print(html)

if __name__ == '__main__':
    main()