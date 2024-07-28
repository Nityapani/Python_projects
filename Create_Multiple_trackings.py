from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium import webdriver as webdriver_chrome
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
import time
import pyautogui
from selenium.webdriver.support.wait import WebDriverWait
from datetime import datetime
# from selenium.webdriver.common.devtools.v121 import page

desired_capabilities = {
  "platformName": "iOS",
  "appium:deviceName": "iPhone 12",
  "appium:platformVersion": "17.5.1",
  "appium:automationName": "XCUITest",
  "appium:udid": "00008101-001E00D22182001E",
  "appium:app": "/Users/nityaprakashpanigrahi/Downloads/MyMedela.ipa",
  "appium:bundleId": "com.medela.mymedela.q",
  "appium:xcodeOrgId": "JH7VLN8YGT",
  "appium:xcodeSigningId": "iPhone Developer",
  "appium:noReset": True,
  "appium:xcodeVersion": "15.4",
  "allowInvisibleElements":True,
  "newCommandTimeout": 120  # Set the command timeout to 120 seconds
}
mobile_driver = webdriver.Remote(command_executor="http://127.0.0.1:4723",desired_capabilities=desired_capabilities)
mobile_driver.implicitly_wait(10)
mobile_driver.find_element(By.XPATH,'(//XCUIElementTypeOther[@name="CONTINUE"])[2]').click()
time.sleep(2)
mobile_driver.switch_to.alert.accept()
print(mobile_driver.get_window_rect())
Email='newaccount@mailto.plus'
time.sleep(2)
mobile_driver.find_element(By.XPATH,'//XCUIElementTypeTextField[@name="Email *"]').click()
mobile_driver.find_element(By.XPATH,'//XCUIElementTypeTextField[@name="Email *"]').send_keys(Email)
mobile_driver.find_element(By.XPATH,'//XCUIElementTypeSecureTextField[@name="Password *"]').send_keys("qwerty@123")
mobile_driver.find_element(By.XPATH,'//XCUIElementTypeButton[@name="LOG-IN"]').click()
print("*User successfully Logged in*")
time.sleep(10)
for i in range (0,201):
  time.sleep(3)
  actions = ActionChains(mobile_driver)
  actions.w3c_actions = ActionBuilder(mobile_driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
  actions.w3c_actions.pointer_action.move_to_location(345, 700)
  actions.w3c_actions.pointer_action.pointer_down()
  actions.w3c_actions.pointer_action.pause(0.1)
  actions.w3c_actions.pointer_action.release()
  actions.perform()
  mobile_driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Diaper").click()
  mobile_driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Both_icon").click()
  mobile_driver.find_element(By.XPATH, '(//XCUIElementTypeOther[@name="Add Note"])[3]').send_keys("This is a Test")
  actions = ActionChains(mobile_driver)
  actions.w3c_actions = ActionBuilder(mobile_driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
  actions.w3c_actions.pointer_action.move_to_location(361, 489)
  actions.w3c_actions.pointer_action.pointer_down()
  actions.w3c_actions.pointer_action.pause(0.1)
  actions.w3c_actions.pointer_action.release()
  actions.perform()
  mobile_driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="SAVE").click()
  time.sleep(3)
  actions = ActionChains(mobile_driver)
  actions.w3c_actions = ActionBuilder(mobile_driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
  actions.w3c_actions.pointer_action.move_to_location(345, 700)
  actions.w3c_actions.pointer_action.pointer_down()
  actions.w3c_actions.pointer_action.pause(0.1)
  actions.w3c_actions.pointer_action.release()
  actions.perform()
  mobile_driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Bottle").click()
  mobile_driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="mix milk selector").click()
  mobile_driver.swipe(340, 450, 120, 450, 300)
  mobile_driver.find_element(By.XPATH, '(//XCUIElementTypeOther[@name="Add Note"])[3]').send_keys("This is a Test")
  actions = ActionChains(mobile_driver)
  actions.w3c_actions = ActionBuilder(mobile_driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
  actions.w3c_actions.pointer_action.move_to_location(361, 489)
  actions.w3c_actions.pointer_action.pointer_down()
  actions.w3c_actions.pointer_action.pause(0.1)
  actions.w3c_actions.pointer_action.release()
  actions.perform()
  mobile_driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="SAVE").click()
  print(i)