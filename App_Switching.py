from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction


desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "12.0",
    "deviceName": "Pixel 3",
    "app": "C:\\Users\\91805\\Downloads\\6.0.04.d-qa-release.apk",
    "appPackage": "com.medela.mymedela.qa",
    "appActivity": "com.medela.mymedela.live.SplashActivity",
    "appWaitForLaunch": False,
    "noReset":True
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities=desired_capabilities)
driver.implicitly_wait(50)
# driver.find_element(By.ID,"com.android.permissioncontroller:id/permission_allow_foreground_only_button").click()
# driver.find_element(By.ID,"com.android.permissioncontroller:id/permission_allow_button").click()
driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup").click()
driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View[4]/android.widget.TextView").click()
a="nityaprakash.panigrahi@programming.com"
driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ListView/android.view.View[1]/android.view.View/android.widget.ListView/android.view.View/android.widget.EditText").send_keys(a)
driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ListView/android.view.View[1]/android.view.View/android.view.View/android.widget.Button").click()
print(driver.current_activity)
print(driver.current_package)
driver.background_app(15)
# Perform actions on your app
# For example, clicking buttons, entering text, etc.
# Start Gmail app
driver.start_activity("com.google.android.gm", "com.google.android.gm.ConversationListActivityGmail")
driver.implicitly_wait(50)
driver.find_element(By.ID,"com.google.android.gm:id/viewified_conversation_item_view").click()
Text=driver.find_element(By.ID,"com.google.android.gm:id/senders").text
print(Text)
driver.background_app(10)
# Perform actions to fetch the OTP
# For example, reading the email body to extract the OTP
# Start your main app again
driver.start_activity("com.android.chrome", "org.chromium.chrome.browser.customtabs.CustomTabActivity")
# driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities=desired_capabilities)
driver.implicitly_wait(30)
driver.find_element(By.ID,"emailVerificationCode").click()
# driver.start_activity("com.google.android.gm", "com.google.android.gm.ConversationListActivityGmail")

# Perform actions to enter the OTP and complete the sign-up process
# For example, finding the OTP field and entering the OTP
print(driver.session_id)
# actions = TouchAction(driver)
# actions.tap()
# actions.move_to(10, 100)
# actions.release()
# actions.perform()
TouchAction(driver).long_press(element).release().perform()

# Scroll/Swipe gesture using TouchAction class
TouchAction(driver).press(startX,startY).wait(1000)
driver.move_to(endX,endY).release().perform()