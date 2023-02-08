from selenium import webdriver
from selenium.webdriver.common.by import By

def select():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get("https://demo.opencart.com/")
    driver.find_element(By.XPATH,"//a[text()='Components']").click()
    driver.find_element(By.PARTIAL_LINK_TEXT,"Monitors (2)").click()
    driver.find_element(By.PARTIAL_LINK_TEXT,"Samsung SyncMaster 941BW").click()
    driver.find_element(By.ID,"input-quantity").send_keys("2")
    driver.find_element(By.ID,"button-cart").click()
    expec=driver.find_element(By.XPATH,"//h1[contains(text(),'Samsung SyncMast')]").text
    return (expec)



def title():
    driver = webdriver.Edge()
    driver.implicitly_wait(30)
    driver.get("https://demo.opencart.com/")
    return (driver.title)

