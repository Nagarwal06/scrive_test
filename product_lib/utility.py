#!/usr/bin/python
"""
.. module:: utility

Utilities to be used across pages.
"""

#import statements
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Utility():
    """
    Class contains function that support various common functions requires in test.
    """

    def wait_and_find_element(self, driver, selectorName, selectorVal):
        """
        Wait for element to be visible and then return element.

        :param driver: webDriver reference variable
        :param selectorName: selector parameters like BY.CSS or BY.XPATH
        :param selectorVal: CSS or XAPTH of the element.

        :return: Returns only one element
        """
        global refresh_tout
        refresh_tout = 20

        WebDriverWait(driver, refresh_tout).until(EC.visibility_of_element_located((selectorName, selectorVal)))

        return driver.find_element(selectorName, selectorVal)


    def click(self, driver, selectorName, selectorVal):
        """
        Wait for element to be visible and then click on that element
        :param driver: webDriver reference variable
        :param selectorName: selector parameters like BY.CSS or BY.XPATH
        :param selectorVal: CSS or XAPTH of the element.
        :return:
        """

        element = self.wait_and_find_element(driver, selectorName, selectorVal)
        WebDriverWait(driver, refresh_tout).until(EC.element_to_be_clickable(element))
        element.click()


    def enter_text(self, driver, selectorName, selectorVal, text="Test User"):
        """
        Wait for element to be visible and then enter text in that element.
        :param driver: webDriver reference variable
        :param selectorName: selector parameters like BY.CSS or BY.XPATH
        :param selectorVal: CSS or XAPTH of the element.
        :param text: text to be entered.
        :return:
        """

        element = self.wait_and_find_element(driver, selectorName, selectorVal)
        element.send_keys(text)


    def  find_element_text(self, driver, selectorName, selectorVal):
        """
        Wait for Element to be visible and then returns text of that element.
        :param driver: webDriver reference variable
        :param selectorName: selector parameters like BY.CSS or BY.XPATH
        :param selectorVal: CSS or XAPTH of the element.
        """
        time.sleep(10)
        element = self.wait_and_find_element(driver, selectorName, selectorVal)
        return element.text