from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

while True:

    # create a new instance of the Chrome driver
    driver = webdriver.Chrome()

    # navigate to the login page
    driver.get("https://portal.ftp.infogenesisasp.com/human.aspx?r=2070971366&arg12=home")

    # find the username and password input fields and fill them in
    username_field = driver.find_element(By.ID, "form_username")
    password_field = driver.find_element(By.ID,"form_password")
    username_field.send_keys("wascc.ftpadmin")
    password_field.send_keys("aglow-fmxcu=T")

    # submit the form
    submit_button = driver.find_element(By.ID,"submit_button")
    submit_button.click()

    # check if login was successful
    if "Welcome" in driver.page_source:
        print("Login successful.")
        select_element = driver.find_element(By.ID,"field_gotofolder")
        select = Select(select_element)
        select.select_by_visible_text("/ Home / wascc.ftpadmin / Export / Hilton")
        checkbox1 = driver.find_element(By.XPATH, "//input[@type='checkbox' and @aria-label='Daily_BQT_Extract-Hilton.csv']")
        checkbox1.click()
        checkbox2 = driver.find_element(By.XPATH, "//input[@type='checkbox' and @aria-label='Daily_GA_Extract.csv']")
        checkbox2.click()
        checkbox3 = driver.find_element(By.XPATH, "//input[@type='checkbox' and @aria-label='GL_GeneralLedger.csv']")
        checkbox3.click()
        checkbox4 = driver.find_element(By.XPATH, "//input[@type='checkbox' and @aria-label='OHD_Header.txt']")
        checkbox4.click()
        
        download_button = driver.find_element(By.ID, "DownloadButton")
        download_button.click()

        time.sleep(15)

        break
    else:
        print("Login failed.")
        time.sleep(3)

    # close the browser
    driver.quit()
