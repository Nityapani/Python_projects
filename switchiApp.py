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
    #  "automationName":"UiAutomator1"
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
a="nityaprakash.panigrahi@programming.com"
driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ListView/android.view.View[1]/android.view.View/android.widget.ListView/android.view.View/android.widget.EditText").send_keys(a)
driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ListView/android.view.View[1]/android.view.View/android.view.View/android.widget.Button").click()
time.sleep(10)
# Do something in the first app

# Start the second app
driver.start_activity("com.google.android.gm", "com.google.android.gm.ConversationListActivityGmail")
time.sleep(10)
driver.find_element(By.ID,"com.google.android.gm:id/viewified_conversation_item_view").click()
Text=driver.find_element(By.ID,"com.google.android.gm:id/senders").text
print(Text)
# Do something in the second app
# driver.find_element(By.ID,"emailVerificationCode").send_keys("12345")

# Switch back to the first app
driver.start_activity("com.medela.mymedela.qa", "com.medela.mymedela.live.SplashActivity")
# driver.implicitly_wait(50)
# driver.find_element(By.ID,"com.android.permissioncontroller:id/permission_allow_foreground_only_button").click()
# driver.find_element(By.ID,"com.android.permissioncontroller:id/permission_allow_button").click()
# driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup").click()
# driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View[4]/android.widget.TextView").click()
time.sleep(10)
# driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub",desired_capabilities=desired_capabilities)
# print(driver.current_package)
# driver.implicitly_wait(30)
driver.find_element(By.ID,"emailVerificationCode").send_keys("12345")
# Continue with the first app
# driver.start_activity("com.google.android.gm", "com.google.android.gm.ConversationListActivityGmail")
