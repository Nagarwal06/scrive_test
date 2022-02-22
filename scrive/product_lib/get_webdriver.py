#!/usr/bin/python
"""
.. module:: get_webdriver

This return same webdriver instance for all testcases

"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Chrome_Options
from selenium.webdriver.firefox.options import Options as Firefox_Options

def driver_chrome(driver_name, driver_loc="C:/Users/chromedriver"):
    """
    Create Selenium driver object and returns it
    Args: driver_name: Name of webdriver.
    """
    global driver
    if driver_name.lower() == "chrome":
        chrome_options = Chrome_Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        chrome_options.add_argument('--ignore-certificate-errors')
        driver = webdriver.Chrome(executable_path=driver_loc, options=chrome_options)
        driver.maximize_window()
    elif driver_name == 'firefox':
        firefox_options = Firefox_Options()
        driver = webdriver.Firefox(executable_path=driver_loc, options=firefox_options)
    elif driver_name == 'safari':
        driver = webdriver.Safari(executable_path=driver_loc)
    elif driver_name == 'ie':
        driver = webdriver.Ie(executable_path=driver_loc)
    else:
        raise EnvironmentError("""Driver name did not match allowed options.
        Allowed Options: ["chrome", "firefox", "safari", "ie"]
        """.format(driver_name))
    return driver
