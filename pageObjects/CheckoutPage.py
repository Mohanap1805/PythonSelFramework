from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfrimPage


class CheckoutPage:

    def __init__(self,driver):
        self.driver = driver
    #self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    cardTitle = (By.XPATH, "//div[@class='card h-100']")

    #product.find_element(By.XPATH, "div/h4/a")
    prodName = (By.XPATH, "div/h4/a")

    #find_element(By.XPATH, "div/button")
    addCartBtn = (By.XPATH,"div/button")

    #self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkOutBtn = (By.CSS_SELECTOR,"a[class*='btn-primary']")

    #self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']")
    checkOutBtn2 = (By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getProdName(self):
        return self.driver.find_element(*CheckoutPage.prodName)

    def getaddCartBtn(self):
        return self.driver.find_element(*CheckoutPage.addCartBtn)

    def getcheckOutBtn(self):
        return self.driver.find_element(*CheckoutPage.checkOutBtn)

    def getCheckOutBtn2(self):
        self.driver.find_element(*CheckoutPage.checkOutBtn2).click()
        confrimPage = ConfrimPage(self.driver)
        return confrimPage