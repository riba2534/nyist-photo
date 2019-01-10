import re
import requests
from bs4 import BeautifulSoup
import lxml
import os



def get_url(url):
        zz=r'/upfile/201709/\d+\.JPG'
        pattern=re.compile(zz)
        try:
            r = requests.get(url)
            r.encoding = r.apparent_encoding
            img = re.findall(pattern, r.text)
            return img
        except:
            return 'error'

def save(list):
    for i in list:
        link='http://ngsying.com'+str(i)
        zz=r'201709\d+\.JPG'
        name=re.findall(zz,link)
        print(name[0])
        f = open(name[0], 'ab')  ##写入多媒体文件必须要 b 这个参数
        r=requests.get(link)
        f.write(r.content)  ##多媒体文件要是用conctent哦！
        f.close()

def main():
    os.chdir(os.getcwd() + '\\南阳理工所有照片')  ##切换到上面创建的文件夹
    for i in range(108,112):
        url = 'http://ngsying.com/show.asp?id='+str(i)
        list = get_url(url)
        save(list)

if __name__ == '__main__':
    main()
