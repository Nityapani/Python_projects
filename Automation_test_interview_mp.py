#To Print all the links with href attribute and the title of the page
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.makemytrip.com/')
driver.implicitly_wait(30)
title=driver.title
print("Tittle of the page is : "+title)
links = driver.find_elements(By.TAG_NAME,"link")
print(links)
for link in links:
    print(link.get_attribute('href'))
    print(link.text)

driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.amazon.in/')
driver.implicitly_wait(30)
title=driver.title
print("Tittle of the page is : "+title)
driver.find_element(By.XPATH,"//i[@class = 'hm-icon nav-sprite']").click()
driver.quit()