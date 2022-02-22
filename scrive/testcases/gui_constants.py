import os

WEB_URL = "https://staging.scrive.com/t/9221714692410699950/7348c782641060a9"
BROWSER_NAME = "chrome"
DOCUMENT_NAME = "test_document"
PLATFORM = os.environ.get('PLATFORM', 'WIN')
SCREENSHOT_PATH = os.environ.get('SCREENSHOT_PATH', 'C:/Users/document_screenshot.png' if PLATFORM == 'WIN' else '/tmp/document_screenshot.png')
DRIVER_LOCATION = os.environ.get('DRIVER_LOCATION', r'C:\Program Files\Python37\chromedriver.exe' if PLATFORM == 'WIN' else '/tmp/scrive/chromedriver')
TIMEOUT = 5

# XPATH
DOCUMENT_NAME_XPATH = ".//input[@id='name']"
NEXT_BTN_XPATH = ".//span[contains(text(),'Next')]"
SIGN_MODAL_XPATH = ".//div[@class='main']//div[contains(@class,'above-overlay')]"
SIGN_BTN_XPATH = ".//div[@class='label']//span[contains(text(),'Sign')]"
SIGNED_DOCUMENT_XPATH = ".//h1[@class='follow']/span"
