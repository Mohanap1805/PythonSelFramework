import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfrimPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkOutPage = homePage.shopItems()

        products = checkOutPage.getCardTitles()
        log.info("getting all card titles")
        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            log.info(productName)
            if productName == "Blackberry":
                product.checkOutPage.getaddCartBtn().click()

        checkOutPage.getcheckOutBtn().click()
        confrimPage = checkOutPage.getCheckOutBtn2()

        log.info("Entering country name as India")
        confrimPage.getSelectCountry().send_keys("ind")
        self.verifyLinkPresence("India")
        confrimPage.getselectName2().click()
        confrimPage.getcheckBox().click()
        confrimPage.getsubmitBtn().click()

        successMsg = confrimPage.getsuccessMsg().text
        log.info("Text message received from application is "+successMsg )
        assert "Success! Thank you!" in successMsg

