# （第四条： 获取标签之间的数据）
from xml.dom import minidom
dom = minidom.parse("info.xml") #打开xml文件
root = dom.documentElement  #得到文档元素对象
provinces = dom.getElementsByTagName("province")
citys = dom.getElementsByTagName("city")
# 获得第二个province标签所对的值
p2 = provinces[1].firstChild.data
print(p2)             #firstChild属性返回被选节点的第一个节点     data 表示获取该节点的数据（类似于webdriver中的提供的text方法）

c1 = citys[0].firstChild.data
print(c1)

c2 = citys[1].firstChild.data
print(c2)

p3 = provinces[2].firstChild.data
print(p3)




# （第三条： 获取标签的属性值）
from xml.dom import minidom
dom = minidom.parse("info.xml")
root = dom.documentElement

logins = root.getElementsByTagName("login")
# 获得login第一个标签的username标签
           # getAttribute() 用于获取元素的属性
username = logins[0].getAttribute("username")
print(username)
# 获得login第一个标签的pwd标签
pwd = logins[0].getAttribute("pwd")
print(pwd)

username = logins[1].getAttribute("username")
print(username)
pwd = logins[1].getAttribute("pwd")
print(pwd)



# （第二条： 获得任意标签名）
from xml.dom import minidom
dom = minidom.parse("info.xml")

root = dom.documentElement
           # getElementsByTagName()  可以通过标签名获取标签
tagname = root.getElementsByTagName("browser")
print(tagname[0].tagName)

tagname = root.getElementsByTagName("login")
print(tagname[1].tagName)

tagname = root.getElementsByTagName("province")
print(tagname[2].tagName)




#读取xml文件（第一条： 获得标签信息）
from xml.dom import minidom
# 打开xml文件
dom = minidom.parse("info.xml")
# 得到文档元素
root = dom.documentElement      #documentElement 用于得到xml文件的唯一根元素

print(root.nodeName)
print(root.nodeValue)
print(root.nodeType)
