import appium
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
import time


desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "12.0",
    "deviceName": "Pixel 3",
    "app": "C:\\Users\\91805\\Downloads\\6.0.04.d-qa-release.apk",
    "appPackage": "com.medela.mymedela.qa",
    "appActivity": "com.medela.mymedela.live.SplashActivity",
    # "–session-override":True
    # "appPackage": "com.medela.mymedela.live",
    # "appActivity": ".SplashActivity"
    #"appActivity": "android.intent.action.MAIN"
    # "noReset":True
}
driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub",desired_capabilities=desired_capabilities)
driver.implicitly_wait(50)
driver.find_element(By.ID,"com.android.permissioncontroller:id/permission_allow_foreground_only_button").click()
driver.find_element(By.ID,"com.android.permissioncontroller:id/permission_allow_button").click()
driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup").click()
driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View[4]/android.widget.TextView").click()
#a="nityaprakash.panigrahi@programming.com"
# driver.background_app(5)
# time.sleep(5)
# driver.launch_app()

# driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ListView/android.view.View[1]/android.view.View/android.widget.ListView/android.view.View/android.widget.EditText").send_keys(a)
# driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ListView/android.view.View[1]/android.view.View/android.view.View/android.widget.Button").click()
# time.sleep(10)
driver.start_activity("com.google.android.gm", "com.google.android.gm.ConversationListActivityGmail")
driver.implicitly_wait(50)
driver.find_element(By.ID,"com.google.android.gm:id/viewified_conversation_item_view").click()
driver.background_app(5)
time.sleep(5)
driver.launch_app()

# Text=driver.find_element(By.ID,"com.google.android.gm:id/senders").text
# print(Text)
# quit()
# driver.open_notifications()
# driver.implicitly_wait(50)
# driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.FrameLayout[3]").is_displayed()
# driver.find_element(By.ID,"android:id/expand_button_icon").click()
# print(driver.session_id)
# driver.quit()
# width = driver.get_window_size()['width']
# height = driver.get_window_size()['height']
# start_x = width // 2
# start_y = height // 4
# end_x = width // 2
# end_y = height * 3 // 4
#
# # Swipe from top to bottom
# driver.swipe(start_x, start_y, end_x, end_y, duration=800)

# desired_capabilities = {
#     "platformName": "Android",
#     "platformVersion": "12.0",
#     "deviceName": "Pixel 3",
#     "appPackage": "com.google.android.gm",
#     "appActivity": "com.google.android.gm.ConversationListActivityGmail",
# }
#
# driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)
#
#
# # Perform your test steps here
#
# # Launch Gmail app

# # driver.quit()
# driver.switch_to.context("com.medela.mymedela.qa")
# driver.start_activity('com.google.android.apps.messaging','.main.MainActivity')
# driver.implicitly_wait(20)
# driver.start_activity("com.medela.mymedela.qa", ".MainActivity")
# desired_capabilities = {
#     "platformName": "Android",
#     "platformVersion": "12.0",
#     "deviceName": "Pixel 3",
#     "app": "C:\\Users\\91805\\Downloads\\6.0.04.d-qa-release.apk",
#     "appPackage": "com.medela.mymedela.qa",
#     "appActivity": "com.medela.mymedela.live.SplashActivity",
#
# }
# driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub",desired_capabilities=desired_capabilities)
# driver.implicitly_wait(20)
# # driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub",desired_capabilities=desired_capabilities)
# print(driver.current_package)
# # driver.implicitly_wait(30)
# desired_capabilities = {
#     "platformName": "Android",
#     "platformVersion": "12.0",
#     "deviceName": "Pixel 3",
#     "app": "C:\\Users\\91805\\Downloads\\6.0.04.d-qa-release.apk",
#     "appPackage": "com.medela.mymedela.qa",
#     "appActivity": "com.medela.mymedela.live.SplashActivity",
# }

# driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)
# driver.find_element(By.ID,"emailVerificationCode").is_displayed()
# driver.background_app()