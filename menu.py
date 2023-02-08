import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Edge()
driver.implicitly_wait(30)

driver.get("https://demo.opencart.com/")


def title():
    driver.get("https://demo.opencart.com/")
    return (driver.title)



# driver.find_element(By.LINK_TEXT,"Acknowledgments, Licensing and Certification").click()
'''driver.find_element(By.PARTIAL_LINK_TEXT,"Acknowledgments").click()
time.sleep(5)'''