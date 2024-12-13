from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage:

    def __init__(self,driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    #self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()

    #driver.find_element(By.CSS_SELECTOR, "[name='name']").send_keys("Rahul")
    name = (By.CSS_SELECTOR, "[name='name']")

    #driver.find_element(By.NAME, "email").send_keys("shetty")
    email = (By.NAME, "email")

    #driver.find_element(By.ID, "exampleCheck1").click()
    check = (By.ID, "exampleCheck1")

    #driver.find_element(By.ID,"exampleFormControlSelect1")
    control = (By.ID,"exampleFormControlSelect1")

    #driver.find_element(By.XPATH, "//input[@value='Submit']")
    submit = (By.XPATH, "//input[@value='Submit']")

    successMsg = (By.CSS_SELECTOR, "[class*='alert-success']")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckoutPage(self.driver)
        return checkOutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getCheck(self):
        return self.driver.find_element(*HomePage.check)

    def getControl(self):
        return self.driver.find_element(*HomePage.control)

    def getSubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccessMsg(self):
        return self.driver.find_element(*HomePage.successMsg)


