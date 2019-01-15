# 数据化搜索关键字
from selenium import webdriver
lists = ["python","学习课程","飞机票","skittles"]
for i in lists:
    b = webdriver.Firefox()
    b.get("http://www.baidu.com")
    b.find_element_by_id("kw").clear()
    b.find_element_by_id("kw").send_keys(i)
    b.find_element_by_id("su").click()

    b.quit()
    