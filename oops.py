from abc import ABCMeta, abstractmethod
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class Cart:
    @abstractmethod
    def add_to_cart():
        return 0

    @abstractmethod
    def add_to_cart_1():
        return 0

class ShoppingCart:
    def __init__(self):
        self.driver = webdriver.Edge()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def navigate_to_website(self):
        self.driver.get("https://demo.opencart.com/")

    def select_item(self):
        self.driver.find_element(By.XPATH, "//a[text()='Components']").click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Monitors (2)").click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Samsung SyncMaster 941BW").click()
        self.driver.find_element(By.ID, "input-quantity").send_keys("2")
        self.driver.find_element(By.ID, "button-cart").click()
    def register(self):
        self.driver.get("https://www.opencart.com/")
        self.driver.find_element(By.XPATH, "(//*[text()='Register'])[2]").click()
        self.driver.find_element(By.ID, "input-username").send_keys("RK")
        self.driver.find_element(By.ID, "input-firstname").send_keys("Radhika")
        self.driver.find_element(By.ID, "input-lastname").send_keys("Kavishwar")
        self.driver.find_element(By.ID, "input-email").send_keys("abc@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("abc123")
        self.driver.find_element(By.XPATH, "//button[text()='Register']")

class AddToCart(ShoppingCart,Cart):

    def add_to_cart(self):
        self.navigate_to_website()
        self.select_item()
        time.sleep(5)
    def add_to_cart_1(self):
        self.navigate_to_website()
        try:
            self.driver.find_element(By.XPATH, "//a[text()='Component']").click()
        except:
            print("Invalid Xpath,Component noy found")

        finally:
            print("add_to_cart is done and add_to_cart_1 is not done due to invalid xpath")


#Object created
opencart = AddToCart()
#Menu driven
while True:
    print("Enter 1 for add to cart function")
    print("Enter 2 for exception function")
    print("Enter 3 for register function")
    print("Enter 4 for exit ")
    userchoice=int(input())
    if userchoice==1:
        opencart.add_to_cart()
    elif userchoice==2:
        opencart.add_to_cart_1()
    elif userchoice==3:
        opencart.register()
    elif userchoice==4:
        quit()

