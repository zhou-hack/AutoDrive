# '''
#                        _oo0oo_
#                       o8888888o
#                       88" . "88
#                       (| -_- |)
#                       0\  =  /0
#                     ___/`---'\___
#                   .' \\|     |// '.
#                  / \\|||  :  |||// \
#                 / _||||| -:- |||||- \
#                |   | \\\  - /// |   |
#                | \_|  ''\---/''  |_/ |
#                \  .-\__  '-'  ___/-. /
#              ___'. .'  /--.--\  `. .'___
#           ."" '<  `.___\_<|>_/___.' >' "".
#          | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#          \  \ `_.   \_ __\ /__ _/   .-` /  /
#      =====`-.____`.___ \_____/___.-`___.-'=====
#                        `=---='
#
#
#      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#            佛祖保佑     永不宕机     永无BUG
# '''


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

userIDandPassword = []
userInput = str(input("请输入账号名与密码 中间使用空格隔开: "))
userIDandPassword.append(userInput.split(" "))
userID = userIDandPassword[0][0]
userPassword = userIDandPassword[0][1]

print("用户名: ",userID, "\n密码: ",userPassword)

# 配置 Chrome 选项
options = webdriver.ChromeOptions()
options.add_argument("--disable-application-cache")  # 禁用应用缓存
options.add_argument("--enable-features=NetworkServiceInProcess")  # 强制启用网络服务
options.add_argument("--disable-web-security")  # 可能会绕过部分安全策略
options.add_argument("--allow-third-party-cookies")  # 允许第三方 Cookie
options.add_argument("--incognito")  # 仍然保持无痕模式
options.add_argument("--verbose")
options.add_argument("--proxy-server=http://127.0.0.1:7899")

# 指定 Chrome 浏览器的路径 此处将使用Chrome4Test v131
# options.binary_location = "C:/Users/Jinbin/Desktop/chrome-win64/chrome.exe"


# 变量存储
# MainPage
page2Class = "https://2-class.com/"

# 课时链接
Course1 = "https://2-class.com/courses/exams/1789"
Course2 = "https://2-class.com/courses/exams/1790"
# Course3 = "https://2-class.com/courses/exams/1860"

# 杂项
def wait():
    time.sleep(1)

# 使用 ChromeDriverManager 自动下载和管理驱动
# 真是服了这死人驱动
service = Service(ChromeDriverManager().install())

# Chrome 启动!
driver = webdriver.Chrome(service=service, options=options)

# 载入主页便于登录
driver.get(page2Class)


# 别急 开始执行
# 自动寻找页面元素并点击 
# "ant-btn ant-btn-primary" 
# 主页"登录"按钮
wait()
 
# 点击登录
login_button = driver.find_element(By.CLASS_NAME, "ant-btn")  # 根据按钮的 CLASS_NAME 属性定位
login_button.click()

# 查找用户输入框后 点击用户输入框并且输入用户名
# user_inputcage = driver.find_element(By.CLASS_NAME, "ant-input-lg")
user_inputcage = driver.find_element(By.XPATH, '//div[@class="ant-form-item-control-wrapper"]//input[@type="text"]')
user_inputcage.click()
user_inputcage.send_keys(userID)


# 查找密码输入框 并且输入密码
# password_inputcage = driver.find_element(By.CLASS_NAME, "ant-input-lg")[1]
password_inputcage = driver.find_element(By.XPATH, '//div[@class="ant-form-item-control-wrapper"]//input[@type="password"]')
password_inputcage.click()
password_inputcage.send_keys(userPassword)

# 提交账号密码实现登录
submit_button = driver.find_element(By.CLASS_NAME, "submit-btn")
submit_button.click()
time.sleep(2)


# 不是 我直接跳转答题不就得了 我服了
# # 进入"我的课程"
# # PLANA 点击按钮进入
# # mycourse_button = driver.find_element(By.CLASS_NAME, "ant-btn")
# # 直接调用登录按钮进行进入 bcsclassElementName==
# # login_button.click()
# # 懒得用这个了 有Cookie留存直接用url跳转得了
# driver.get("https://2-class.com/admin/student_course")

# 跳转答题

# 1
driver.get(Course1)
wait()
exam_start_button = driver.find_element(By.CLASS_NAME, "exam-box-start")
exam_start_button.click()

# 1.开始答题
# 定位到父容器
parent = driver.find_element(By.CLASS_NAME, "ant-radio-group")

# 在父容器中查找第一个 radio input
radio_buttons = parent.find_elements(By.CLASS_NAME, "ant-radio-input")
def selectA():
    radio_buttons[0].click()  # 点击第1个选项
def selectB():
    radio_buttons[1].click()  # 点击第2个选项
def selectC():
    radio_buttons[2].click()  # 点击第3个选项
def selectD(): 
    radio_buttons[3].click()  # 点击第4个选项

nextTopic = driver.find_element(By.CLASS_NAME, "exam-content-btn-next")
selectC()
nextTopic.click()

selectA()
nextTopic2 = driver.find_element(By.CLASS_NAME, "ant-btn-primary")
nextTopic2.click()

selectB()
nextTopic2.click()

selectC()
nextTopic2.click()

checkboxes = driver.find_elements(By.CLASS_NAME, "ant-checkbox-input")
if len(checkboxes) > 0:
    def multiChoiceA():
        checkboxes[0].click()
    def multiChoiceB():
        checkboxes[1].click()
    def multiChoiceC():
        checkboxes[2].click()
    def multiChoiceD():
        checkboxes[3].click()
else:
    print("未找到任何 checkbox 元素")
    
multiChoiceA()
multiChoiceB()
multiChoiceC()
# input("断电2 Line148")
examSubmit_button = driver.find_element(By.CLASS_NAME, "ant-btn-primary")
examSubmit_button.click()
wait()
print("=====Done====")
print("1/2")
wait()

# 第一题答题结束 开始第二题

driver.get(Course2)
wait()
exam_start_button = driver.find_element(By.CLASS_NAME, "exam-box-start")
exam_start_button.click()
wait()

# 在父容器中查找第一个 radio input
# 再找一次 怕出问题
parent = driver.find_element(By.CLASS_NAME, "ant-radio-group")

radio_buttons = parent.find_elements(By.CLASS_NAME, "ant-radio-wrapper")
def selectA():
    radio_buttons[0].click()  # 点击第1个选项
def selectB():
    radio_buttons[1].click()  # 点击第2个选项
def selectC():
    radio_buttons[2].click()  # 点击第3个选项
def selectD(): 
    radio_buttons[3].click()  # 点击第4个选项

nextTopic = driver.find_element(By.CLASS_NAME, "exam-content-btn-next")
selectC()
# wait()
nextTopic.click()

selectC()
# wait()
# 再找一次 怕出问题
nextTopic2 = driver.find_element(By.CLASS_NAME, "ant-btn-primary")
nextTopic2.click()

selectB()
# wait()
nextTopic2.click()

selectC()
# wait()
nextTopic2.click()

selectD()
examSubmit_button = driver.find_element(By.CLASS_NAME, "ant-btn-primary")
examSubmit_button.click()

print("=====Done====")
print("2/2")
print("Author: her3dev")

# print(driver.title)
time.sleep(1)
exit()



# 第二部分无法正常点击，但是可以正常下一题与提交
# Fixed @ 2024.11.17 08:56 AM
# 原来是我答案给错了




