#!/usr/bin/python
"""
.. module:: signed_document_test

Sign the test document using entered name.

"""

import sys
from os.path import abspath, dirname, join

sys.path.insert(0, abspath(join(dirname(__file__), '../')))

'''import Statements'''
from selenium.webdriver.common.by import By
from product_lib.get_webdriver import *
from testcases import gui_constants as const
from product_lib.utility import Utility
import time

'''Object variables'''
utility_obj = Utility()

def setup_application():
    """
    Set-Up and Tear Down for the function.
    """

    global driver
    ''' Step 1 - Get the Driver '''
    driver = driver_chrome(const.BROWSER_NAME, const.DRIVER_LOCATION)

    ''' Step 2 - Navigate to Scrive document Page '''
    driver.get(const.WEB_URL)
    print("Open the Scrive web page successfully")


def fill_and_signed_document():
    """
    Test to fill the document and signed it.
    """

    '''Step 3 - Fill in the full name in the document.'''
    utility_obj.enter_text(driver, By.XPATH, const.DOCUMENT_NAME_XPATH, const.DOCUMENT_NAME)

    '''Step 4 - Click on Next'''
    utility_obj.click(driver, By.XPATH, const.NEXT_BTN_XPATH)

    '''Step 5 - Take a screenshot of the confirmation modal '''
    time.sleep(const.TIMEOUT)
    sign_modal_element = utility_obj.wait_and_find_element(driver, By.XPATH, const.SIGN_MODAL_XPATH)
    sign_modal_element.screenshot(const.SCREENSHOT_PATH)
    print("Captured the screenshot at {0} location".format(const.SCREENSHOT_PATH))

    '''Step 6 - Sign the document '''
    utility_obj.click(driver, By.XPATH, const.SIGN_BTN_XPATH)

    '''Step 7 - Verify that there is a text “Document signed” on the screen.'''
    sign_document_text = utility_obj.find_element_text(driver, By.XPATH, const.SIGNED_DOCUMENT_XPATH)
    assert sign_document_text == "Document signed!"
    print("Verification is completed")

def teardown():
    """
    Tear Down - Closes Browser.
    """
    '''Step 8 - Close the browser'''
    driver.close()
    driver.quit()
    print("Test Completed")

if __name__ == "__main__":
    setup_application()
    fill_and_signed_document()
    teardown()