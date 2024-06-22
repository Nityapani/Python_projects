# from appium import webdriver
# from selenium.webdriver.common.by import By
#
# # desired_capabilities = {
# #     "platformName": "Android",
# #     "platformVersion": "12.0",
# #     "deviceName": "Pixel 3",
# #     "browserName": "Firefox"
# # }
# #
# # driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)
# # driver.implicitly_wait(50)
# # driver.get("https://google.com")
# # session_data = driver.capabilities
# # # Print the session data
# # print(session_data)
# # desired_capabilities = {
# #     "platformName": "Android",
# #     "platformVersion": "12.0",
# #     "deviceName": "Pixel 3",
# #     "appPackage": "com.google.android.gm",
# #     "appActivity": "com.google.android.gm.ConversationListActivityGmail",
# # }
#
# # driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)
#
# # Perform your test steps here
#
# # Launch Gmail app
# driver.start_activity("com.google.android.gm", "com.google.android.gm.ConversationListActivityGmail")
# driver.implicitly_wait(50)
# driver.find_element(By.ID,"com.google.android.gm:id/welcome_tour_got_it").click()
# driver.find_element(By.ID,"com.google.android.gm:id/action_done").click()
