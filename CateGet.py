import os
import io
import sys
import time
import urllib.request
from bs4 import BeautifulSoup

def readMids(midFile):
    midsFile = open(midFile,"r")
    midList = midsFile.readlines()
    print(len(midList))
    return midList

def createFolder(mid,cate,location):

    path = r"E:/音频实验数据/原始数据/newdata/"+mid+cate+location+'.txt'
    path = path[0:len(path)-1]
    #print(path +"in function createFolder")
    #os.makedirs(path)
    file = open(path, 'w')
    file.write('eeee')
    file.close()
    return path


def requestIdData():
#    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
    mids = readMids(r"E:\音频实验数据\原始数据\mids.txt")
    for mid in mids:
        path = "http://phonemica.net/storyteller?mid=" + mid[0:len(mid) - 1]
        #print(path)
        request2 = urllib.request.Request(path)
        responseHtml2 = urllib.request.urlopen(request2)
        Soup = BeautifulSoup(responseHtml2, "html.parser")
    #    cate = Soup.select('a[//*[@id="container"]/div[3]/div/div[2]/p[2]/text()]')
    #    location = Soup.select('#container > div:nth-child(4) > div > div.uk-width-medium-1-2.uk-width-small-1-1 > p:nth-child(4) > small')
    #    print(location)
        IDData = Soup.select("p")
        cate = str(IDData[1])
        #print(cate.split(':')[1].split('<')[0].replace('\n','').replace('\t',''))
        location = str(IDData[2])
        print(mid.replace('\n','')+'AAA'+cate.split(':')[1].split('<')[0].replace('\n','').replace('\t','')+'BBB'+location.split('<small>')[1].split('</small>')[0].replace('\n','').replace('\t',''))
        #createFolder(mid.replace('\n',''),cate.split(':')[1].split('<')[0].replace('\n','').replace('\t','').strip(),location.split('<small>')[1].split('</small>')[0].replace('\n','').replace('\t','').strip())
        time.sleep(0.3)


requestIdData()