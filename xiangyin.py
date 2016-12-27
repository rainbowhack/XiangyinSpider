import os
import io
import sys
import time
import urllib.request
from bs4 import BeautifulSoup


# 定义下载函数downLoadPicFromURL（本地文件夹，网页URL）
def downLoadPicFromURL(dest_dir, mid):
    # url = "http://phonemica.net/files/543748472bd553180882ab9c/0.mp3"
    path = "http://phonemica.net/files/"+mid[0:len(mid)-1]+"/0.mp3"
    try:
        urllib.urlretrieve(path, dest_dir)
        print("dddffe")
    except:
        print
        '\tError retrieving the URL:', dest_dir

def findAllMid( Total , Sub,counter):

    midValue = ''
    while(counter!=-1):
       counter = str(Total).find(str(Sub))
       midValue = Total[counter+4:counter+28]
#       print(midValue)
       writeMid(midValue,r"F:/language")
       Total = Total[counter+28:]

    return True

def writeId(sex,age,loc,cla,filedir,file):
    destDir = os.path.join(filedir, file + ".txt")
    IDTxt = open(destDir, "a")
    IDTxt.write(str(sex) + "\n")
    IDTxt.write(age + "\n")
#    IDTxt.write(str(cla) + "\n")
    IDTxt.write(str(loc) + "\n")
    IDTxt.close()
    return True

def createFolder(mid):

    path = r"F:/language/"+mid
    path = path[0:len(path)-1]
    print(path +"in function createFolder")
    os.makedirs(path)
    return path

def writeMid(mid,dir):
    dirinput = os.path.join(dir,"mid.txt")
    print(dirinput)
    midTxt = open(dirinput,"a")
    midTxt.write(mid+"\n")
    midTxt.close()

def requestMid():
    request = urllib.request.Request("http://www.phonemica.net/map")
    responseHtml = urllib.request.urlopen(request)
    soup = BeautifulSoup(responseHtml,"html.parser")
    scriptStr = str(soup.find_all('script'))
    targetStr = 'mid='
    return scriptStr,targetStr

def getAllMid():
    scriptStr = requestMid()[0]
    targetStr = requestMid()[1]
    findAllMid(scriptStr,targetStr,0)
    return True

def readMids(midFile):
    midsFile = open(midFile,"r")
    midList = midsFile.readlines()
    print(len(midList))
    return midList

def requestIdData():
#    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
    mids = readMids(r"C:\Users\fighting\Desktop\language\mid.txt")
    for mid in mids:
        path = "http://phonemica.net/storyteller?mid="+mid[0:len(mid)-1]
        request2 = urllib.request.Request(path)
        responseHtml2 = urllib.request.urlopen(request2)

        soup2 = BeautifulSoup(responseHtml2,"html.parser")
        IDData = soup2.select("p")
        #container > div:nth-child(4) > div > div.uk-width-medium-1-2.uk-width-small-1-1 > p:nth-child(2) > label.managebirthyear
        #p:nth-of-type(1)>label.managebirthyear
        #container > div:nth-child(4) > div
        sexage = str(IDData[0])
        cate = str(IDData[1])
        location = str(IDData[2])
        #这里是年龄和性别
        age = sexage[48:52]
        sex = sexage[95:96]
        #这里是方言种类分类
        cla = cate[40:len(cate)-4]
        # 这里是地理位置
        mp3FolderPath = createFolder(str(mid))
        print(mp3FolderPath+"mp3PathTest")
        writeId(sex,age,location,cla,mp3FolderPath,mid[0:len(mid)-1])
        print("Done in sample" + mid)
#        downLoadPicFromURL(mid,mp3FolderPath)
        mp3Path = "http://phonemica.net/files/" + mid[0:len(mid) - 1] + "/0.mp3"
        print(mp3Path)
        urllib.request.urlretrieve(mp3Path, os.path.join(mp3FolderPath,mid[0:len(mid)-1]+".mp3"))
        time.sleep(30)


#request2 = urllib.request.Request("http://phonemica.net/storyteller?mid=543748472bd553180882ab9c")
#responseHtml2 = urllib.request.urlopen(request2)
#soup2 = BeautifulSoup(responseHtml2,"html.parser")

#print(soup2)
#IDData = soup2.select("p")
#container > div:nth-child(4) > div > div.uk-width-medium-1-2.uk-width-small-1-1 > p:nth-child(2) > label.managebirthyear
#p:nth-of-type(1)>label.managebirthyear
#container > div:nth-child(4) > div
#sexage = str(IDData[0])
#cate = str(IDData[1])
#location = str(IDData[2])
#这里是年龄和性别
#print(sexage[48:52])
#print(sexage[95:96])

#这里是方言种类分类
#print(cate[40:len(cate)-4])

#这里是地理位置
#print(location)
#print(location[44:len(location)-12])
#print(location[len(location)-30:len(location)-12])
#创建相应的目录
#os.makedirs(r"F:\langusge\dsfa")
#IdFile = open("F:\langusge\dddd.txt","w")

def formatsexage(sexage):
    sexage[96:]
    return True

#print(scriptStr.find(targetStr))
#print(scriptStr[31915:31915+28])
#print(soup.find_all('script'))
#print(soup.prettify())

#下载音频

# 下载网页文件到本地文件夹
# 设置下载后存放的存储路径'C:\Users\yinyao\Desktop\Python code'
#path = r"F:\langusge\dsfa"
#file_name = "000.mp3"  # 文件名，包含文件格式
#dest_dir = os.path.join(path, file_name)

# 设置下载链接的路径
#url = "http://phonemica.net/files/543748472bd553180882ab9c/0.mp3"

#urllib.request.urlretrieve(url, dest_dir)

#readMids(r"C:\Users\fighting\Desktop\language\mid.txt")

requestIdData()


