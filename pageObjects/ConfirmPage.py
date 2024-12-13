from selenium.webdriver.common.by import By


class ConfrimPage:

    def __init__(self,driver):
        self.driver = driver

    #self.driver.find_element(By.ID, "country")
    selectCountry = (By.ID, "country")

    #By.LINK_TEXT, "India"
    selectName = (By.LINK_TEXT,"India")

    #self.driver.find_element(By.LINK_TEXT, "India").click()
    selectName2 = (By.LINK_TEXT,"India")

    #self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
    checkBox = (By.XPATH,"//div[@class='checkbox checkbox-primary']")

    #self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
    submitBtn = (By.XPATH,"//input[@type='submit']")

    #successMsg = self.driver.find_element(By.CLASS_NAME, "alert-success").text
    successMsg = (By.CLASS_NAME,"alert-success")

    def getSelectCountry(self):
        return self.driver.find_element(*ConfrimPage.selectCountry)

    def getselectName2(self):
        return self.driver.find_element(*ConfrimPage.selectName2)

    def getcheckBox(self):
        return self.driver.find_element(*ConfrimPage.checkBox)

    def getsubmitBtn(self):
        return self.driver.find_element(*ConfrimPage.submitBtn)

    def getsuccessMsg(self):
        return self.driver.find_element(*ConfrimPage.successMsg)