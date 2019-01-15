# 读取text文件
use_file = open("use_info.txt","r")
lines = use_file.readlines()#使用readlines 方法读取txt文件
use_file.close()

for line in lines:
    username = line.split("，")[0]
    pwd = line.split("，")[1]
    print(username,pwd)
from xml.dom import minidom