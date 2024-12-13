import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self,getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("firstname is "+getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])
        log.info("lastname is " + getData["lastname"])
        homepage.getEmail().send_keys(getData["lastname"])
        homepage.getCheck().click()
        log.info("gender is " + getData["gender"])
        self.selectOptionByText(homepage.getControl(),getData["gender"])
        homepage.getSubmit().click()

        alertText = homepage.getSuccessMsg().text
        log.info("Success message received from application is "+alertText)
        assert("Success" in alertText)
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self,request):
        return request.param