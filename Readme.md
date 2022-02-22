# **scrive_test**

###### Pre-Requisites:

1. Download Python 3 (https://www.python.org/downloads/release/python-368/),
Install Python 3 from MSI in windows.
2. Download Chrome WebDriver (https://chromedriver.storage.googleapis.com/index.html?path=97.0.4692.36/)
3. Move Chrome Driver in directory (C:\Program Files\Python36).
4. Open command prompt/terminal in Administrator mode.
5. Install Selenium using command -> pip3 install selenium
6. Install Pytest using command -> pip3 install pytest

Python Packages: Make sure to install these packages before use case execution.


###### Objective:
Main goal of Scrive_test is to create test automation suite to sign the test document using entered name.

###### Architecture

`product lib:
`It consists different page specific classes which consists product features and business logic.
POM (Page Object Model)

Each functionality has specific test cases, which uses indiviual page specific object.
Page specific objects → are the libraries having specific page functionalitites.

`testcases: 
`All test suite and test cases to be executed for different features.

**Project Structure:**
* scrive_test
  * product_lib
    * utility.py
    * get_webdriver.py
  * test_cases
    * signed_document_test.py


###### Step-by-step guide to run test using cmd:

Make sure all necessary packages are installed.
Change the DRIVER_LOCATION constant variable as per your driver installed location. 
Open cmd as in administrator mode.
Change the directory to project path i.e, scrive_test -> cd scrive_test
Run the command "python testcases\signed_document_test.py"
Wait for test to complete and see result in command prompt.


###### Step-by-step guide to run test on linux

Make sure all necessary packages are installed.
	- chromedriver, google-chrome, python3, pip3, selenium
Open terminal as a root user.
Change the directory to project path i.e, scrive_test -> cd scrive_test
Run the command "python3 testcases\signed_document_test.py"
Wait for test to complete and see result in command prompt.