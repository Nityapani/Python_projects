from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction

from appium import webdriver

desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "12.0",
    "deviceName": "Pixel 3",
    "appPackage": "com.google.android.gm",
    "appActivity": "com.google.android.gm.ConversationListActivityGmail"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)

# Now the Gmail app should be open on the device
driver.implicitly_wait(20)
driver.start_activity('com.google.android.apps.messaging','.main.MainActivity')
driver.implicitly_wait(20)
driver.start_activity("com.google.android.gm", "com.google.android.gm.ConversationListActivityGmail")
driver.implicitly_wait(20)
#driver.find_element(By.ID,"com.google.android.gm:id/viewified_conversation_item_view").click()
#driver.start_activity('com.google.android.apps.messaging','.main.MainActivity')
