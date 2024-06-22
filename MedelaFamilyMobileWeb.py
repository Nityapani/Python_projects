import appium
import playwright
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium import webdriver as webdriver_chrome
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
import time

from selenium.webdriver.common.devtools.v121 import page

desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "12.0",
    "deviceName": "vivo 1907",
    "app": "C:\\Users\\91805\\Downloads\\6.2.1-release.apk",
    "appium:automationName": "UiAutomator2",
    "appPackage": "com.medela.mymedela.qa",
    "appActivity": "com.medela.mymedela.live.SplashActivity"
}

mobile_driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub",desired_capabilities=desired_capabilities)
mobile_driver.implicitly_wait(70)

mobile_driver.find_element(By.ID,"com.android.permissioncontroller:id/permission_allow_button").click()
mobile_driver.find_element(By.XPATH,'//android.view.ViewGroup[@content-desc="CONTINUE"]').click()
mobile_driver.find_element(By.XPATH,'//*[contains(@text,"HAVE AN ACCOUNT? SIGN-UP")]').click()
mobile_driver.find_element(By.XPATH,"//android.widget.EditText[@checkable='false']").click()
a="appiumtest72@yopmail.com"
mobile_driver.find_element(By.XPATH,"//android.widget.EditText[@checkable='false']").send_keys(a)
time.sleep(2)
mobile_driver.press_keycode(66)
time.sleep(2)
mobile_driver.find_element(By.XPATH,'//*[contains(@text,"Send verification")]').click()
mobile_driver.implicitly_wait(20)
chrome_driver = webdriver_chrome.Chrome()
# Use Chrome driver to access the web page and extract data
# Replace with your specific actions and data extraction logic
chrome_driver.maximize_window()
chrome_driver.get("https://yopmail.com")
time.sleep(7)
chrome_driver.find_element(By.XPATH,"//input[@id='login']").send_keys(a)
chrome_driver.find_element(By.XPATH,"//i[contains(text(),'')]").click()
chrome_driver.switch_to.frame(chrome_driver.find_element(By.XPATH,"//iframe[@id='ifmail']"))
Code=chrome_driver.find_element(By.XPATH,"//span[contains(text(),'Your code is')]").text
print(Code)
Verification_Code=Code[-6:]
Verification_code=str(Verification_Code)
print(Verification_Code)
element=mobile_driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ListView/android.view.View/android.view.View/android.widget.ListView/android.view.View[2]/android.widget.EditText")
element.click()
for i in Verification_code:
    i=int(i)
    if i==0:
        mobile_driver.press_keycode(7)
    elif i==1:
        mobile_driver.press_keycode(8)
    elif i==2:
        mobile_driver.press_keycode(9)
    elif i==3:
        mobile_driver.press_keycode(10)
    elif i==4:
        mobile_driver.press_keycode(11)
    elif i==5:
        mobile_driver.press_keycode(12)
    elif i==6:
        mobile_driver.press_keycode(13)
    elif i==7:
        mobile_driver.press_keycode(14)
    elif i==8:
        mobile_driver.press_keycode(15)
    else:
        mobile_driver.press_keycode(16)
mobile_driver.press_keycode(66)
mobile_driver.find_element(By.XPATH,"//android.widget.EditText[@password='true']").send_keys("Medela2024")
mobile_driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ListView/android.view.View[3]/android.widget.EditText").send_keys("Medela2024")
time.sleep(2)
mobile_driver.find_element(By.XPATH,'//*[contains(@text,"Sign")]').click()
time.sleep(7)
mobile_driver.find_element(By.XPATH,"//android.widget.EditText[@text='Your Name / Nickname *']").send_keys("Mom")
mobile_driver.implicitly_wait(10)
mobile_driver.find_element(By.XPATH,"//android.widget.EditText[@text='Baby Birth/Due Date *']").click()
mobile_driver.find_element(By.XPATH,"//android.widget.TextView[@text='10']").click()
mobile_driver.find_element(By.XPATH,"//android.widget.TextView[@text='OK']").click()
mobile_driver.implicitly_wait(10)
mobile_driver.find_element(By.XPATH,"//*[contains(@text,'Nickname')]").send_keys("Baby1")
mobile_driver.find_element(By.XPATH,"//android.widget.TextView[@text='Girl']").click()
mobile_driver.find_element(By.XPATH,"//android.widget.TextView[@text='NEXT']").click()
mobile_driver.find_element(By.XPATH,"//*[contains(@text,'HAVE A MEDELA PUMP')]").click()
print("User successfully Registered")
# time.sleep(15)

time.sleep(10)
mobile_driver.find_element(By.XPATH,"//android.view.ViewGroup[@content-desc='tracking_button']").click()
mobile_driver.find_element(By.XPATH,'//android.view.ViewGroup[@content-desc="OK"]').click()
mobile_driver.find_element(By.XPATH,'//android.view.ViewGroup[@content-desc="Diaper"]').click()
mobile_driver.find_element(By.XPATH,'//android.view.ViewGroup[@content-desc="Both_icon"]').click()
mobile_driver.find_element(By.XPATH,"//*[contains(@text,'Note')]").send_keys("This is a Test")
mobile_driver.find_element(By.XPATH,'//android.view.ViewGroup[@content-desc="SAVE"]').click()
mobile_driver.find_element(By.XPATH,"//android.view.ViewGroup[@content-desc='tracking_button']").click()
mobile_driver.find_element(By.XPATH,'//android.view.ViewGroup[@content-desc="Bottle"]').click()
mobile_driver.find_element(By.XPATH,'//android.view.ViewGroup[@content-desc="milk formula selector"]').click()
mobile_driver.find_element(By.XPATH,"//*[contains(@text,'Note')]").send_keys("This is a Test")
mobile_driver.find_element(By.XPATH,'//android.view.ViewGroup[@content-desc="SAVE"]').click()
time.sleep(2)
mobile_driver.find_element(By.XPATH,"//*[contains(@text,'Never show this')]").click()
mobile_driver.find_element(By.XPATH,"//android.view.ViewGroup[@content-desc='tracking_button']").click()
mobile_driver.find_element(By.XPATH,'//android.view.ViewGroup[@content-desc="Sleep"]').click()
mobile_driver.find_element(By.XPATH,'//android.view.ViewGroup[@content-desc="START"]').click()
mobile_driver.find_element(By.XPATH,"//*[contains(@text,'Note')]").send_keys("This is a Test")
time.sleep(5)
mobile_driver.find_element(By.XPATH,'//android.view.ViewGroup[@content-desc="SAVE"]').click()
mobile_driver.find_element(By.XPATH,"//android.view.ViewGroup[@content-desc='tracking_button']").click()
mobile_driver.find_element(By.XPATH,'//android.view.ViewGroup[@content-desc="Length"]').click()
time.sleep(2)
mobile_driver.swipe(890,880,200,880,300)
time.sleep(2)
mobile_driver.find_element(By.XPATH,"//*[contains(@text,'Note')]").send_keys("This is a Test")
mobile_driver.find_element(By.XPATH,'//android.view.ViewGroup[@content-desc="SAVE"]').click()
mobile_driver.find_element(By.XPATH,"//android.view.ViewGroup[@content-desc='tracking_button']").click()
mobile_driver.find_element(By.XPATH,'//android.view.ViewGroup[@content-desc="Weight"]').click()
mobile_driver.find_element(By.XPATH,"//android.widget.EditText[@text='0']").click()
mobile_driver.press_keycode(9)
mobile_driver.press_keycode(66)
mobile_driver.find_element(By.XPATH,"//*[contains(@text,'Note')]").send_keys("This is a Test")
mobile_driver.find_element(By.XPATH,'//android.view.ViewGroup[@content-desc="SAVE"]').click()
mobile_driver.find_element(By.XPATH,"//android.view.ViewGroup[@content-desc='tracking_button']").click()
mobile_driver.find_element(By.XPATH,'//android.view.ViewGroup[@content-desc="Breastfeeding"]').click()
time.sleep(3)
mobile_driver.find_element(By.XPATH,'//android.view.ViewGroup[@content-desc="Both"]').click()
mobile_driver.find_element(By.XPATH,"//*[contains(@text,'Note')]").send_keys("This is a Test")
time.sleep(3)
mobile_driver.find_element(By.XPATH,'//android.view.ViewGroup[@content-desc="SAVE"]').click()
mobile_driver.find_element(By.XPATH,"//android.view.ViewGroup[@content-desc='tracking_button']").click()
mobile_driver.find_element(By.XPATH,'//android.view.ViewGroup[@content-desc="Pumping"]').click()
mobile_driver.find_element(By.XPATH,'//android.view.ViewGroup[@content-desc="START"]').click()
time.sleep(3)
mobile_driver.find_element(By.XPATH,'//android.view.ViewGroup[@content-desc="PAUSE"]').click()
mobile_driver.swipe(340,1860,340,800,300)
time.sleep(2)
mobile_driver.swipe(800,1000,250,1000,300)
time.sleep(2)
mobile_driver.find_element(By.XPATH,"//*[contains(@text,'Note')]").send_keys("This is a Test")
mobile_driver.find_element(By.XPATH,'//android.view.ViewGroup[@content-desc="SAVE"]').click()
mobile_driver.implicitly_wait(10)
mobile_driver.find_element(By.XPATH,"//android.widget.TextView[@text='STATS']").click()
mobile_driver.find_element(By.XPATH,'//android.view.ViewGroup[@content-desc="NOT NOW"]').click()
mobile_driver.find_element(By.XPATH,"//android.widget.TextView[@text='MORE']").click()
mobile_driver.find_element(By.XPATH,"//android.widget.TextView[@text='My Profile']").click()
mobile_driver.find_element(By.XPATH,"//android.widget.TextView[@text='LOG OUT']").click()
mobile_driver.find_element(By.XPATH,"//android.widget.TextView[@text='OK']").click()
print("User successfully Logged out")
mobile_driver.find_element(By.XPATH,"//android.widget.TextView[@text='CONTINUE']").click()
mobile_driver.find_element(By.XPATH,"//android.widget.EditText[@index='0']").send_keys(a)
mobile_driver.find_element(By.XPATH,"//android.widget.EditText[@index='2']").send_keys("Medela2024")
mobile_driver.find_element(By.XPATH,"//android.widget.Button[@text='LOG-IN']").click()
time.sleep(5)
print("User successfully logged in")





