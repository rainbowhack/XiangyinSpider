import os

def readMids(midFile):
    midsFile = open(midFile,"r")
    midList = midsFile.readlines()
    print(len(midList))
    return midList

def rename(newName,check,counter):
    path="E:\音频实验数据\原始数据\language2";
    filelist=os.listdir(path)#该文件夹下所有的文件（包括文件夹）
    for files in filelist:#遍历所有文件
        Olddir=os.path.join(path,files);#原来的文件路径
     #   print(Olddir)
        OldName = os.path.join(files);
     #   print(OldName)
        if(OldName.split('.')[0]==check):
     #       filename=os.path.splitext(files)[0];#文件名
            filetype=os.path.splitext(files)[1];#文件扩展名
            Newdir=os.path.join(path,newname.replace('\n','')+'AAA'+str(counter)+filetype);#新的文件路径
            os.rename(Olddir,Newdir);#重命名


mids = readMids(r"E:\音频实验数据\原始数据\newdata\MetaName.txt")
counter = 1
for mid in mids:
    check = mid.split('AAA')[0]
    newname = mid.split('AAA')[1]
    #print(newname)
    counter = 1+counter
    print(counter)
    rename(newname,check,counter)