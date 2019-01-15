# 数据去动画测试 ，参数化登录麦子学院
from selenium import webdriver
from public import Login

class LoginTest():
    def __init__(self):
        self.b = webdriver.Firefox()
        self.b.get("http://www.maiziedu.com")

# asmin用户登录
    def test_asmin_login(self):
        username = "asmin"
        pwd = "123"
        Login().user_login(self.b,username,pwd)
        self.b.quit()
# zhoushan用户登录
    def test_zhoushan_login(self):
        username = "zhoushan"
        pwd = "123456"
        Login().user_login(self.b,username,pwd)
        self.b.quit()

LoginTest().test_asmin_login()#调用asmin登录模块
LoginTest().test_zhoushan_login()#调用