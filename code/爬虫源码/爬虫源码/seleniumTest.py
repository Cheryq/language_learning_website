from selenium import webdriver
from time import sleep
# 访问百度
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
# 最大化浏览器窗口
driver.maximize_window()
# 搜索
driver.find_element_by_id("kw").send_keys("C语言中文网")
driver.find_element_by_id("su").click()
sleep(3)
# 通过js代码设置滚动条位置，数值代表(左边距，上边距)
js="window.scrollTo(100,500);"
#执行js代码
driver.execute_script(js)
sleep(5)
driver.quit()