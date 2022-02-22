# **scrive_test**

###### Pre-Requisites:

1. Python 3 Installed (https://www.python.org/downloads/release/python-368/)
2. Download Browser WebDriver e.g. For Chrome:- https://chromedriver.storage.googleapis.com/index.html?path=97.0.4692.36/
3. Move Browser Driver in directory (C:\Program Files\Python36).
4. Open command prompt/terminal in Administrator mode.
5. Install Selenium using command -> pip3 install selenium.

###### Objective:
Create test automation suite to sign test document using entered name.

###### Architecture

`product lib:
`Utility class having common functions to support test execution.
`Web Driver as per user argument i.e. Chrome, Firefox or IE.

`testcases: 
`All test suite and test cases which are to be executed for different features.

**Project Structure:**
* scrive_test
  * product_lib
    * utility.py
    * get_webdriver.py
  * test_cases
    * signed_document_test.py
    * gui_constants.py


###### Step-by-step guide to run test using cmd on windows:
* Make sure all necessary packages are installed.
* Either place the driver at location "C:\Program Files\Python36" or update gui_constants.py variable "DRIVER_LOCATION" with driver location.
* Open cmd prompt in administrator mode.
* Change the directory to project path i.e, scrive -> cd scrive
* Run the command "python testcases\signed_document_test.py"
* Wait for test to complete and see result in command prompt.
* Screenshot will be saved at location "C:/Users/document_screenshot.png".

###### Step-by-step guide to run test on linux
* Make sure all necessary packages are installed.
  * chromedriver, google-chrome, python3, pip3, selenium
* Either place the driver at location "/tmp/scrive/" or update gui_constants.py variable "DRIVER_LOCATION" with driver location.
* Open terminal as a root user.
* Change the directory to project path i.e, scrive -> cd scrive
* Run the command "python3 testcases\signed_document_test.py"
* Wait for test to complete and see result in command prompt.
* Screnshot will be saved at location "/tmp/document_screenshot.png".

**Note**: By default, test will be executed for Chrome Browser. Update variable BROWSER_NAME in gui_constants.py file. Allowed Options: ["chrome", "firefox", "ie"]
