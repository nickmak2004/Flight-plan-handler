
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import time
try:
    #using default snap geckodriver becuase installed one caused issues
    driverPath = "/snap/bin/geckodriver"
    options = Options()
    service = Service(executable_path=driverPath)
    browser = webdriver.Firefox(service=service, options=options)
    browser.get("https://dispatch.simbrief.com/options/new")
    print("Starting sing in process")
    cookieConsentButton = browser.find_element(By.XPATH,"/html/body/div[13]/section/figure[1]/div[2]/div[2]")

    cookieConsentButton.click()
    time.sleep(1)
    singInButton = browser.find_element(By.ID,"login-button")

    singInButton.click()

    time.sleep(1)
    username = input("Enter your Navigraph username: ")
    password = input("Enter your Navigraph password: ")
    time.sleep(1)
    userName = browser.find_element(By.ID,"username").send_keys(username)
    time.sleep(1)
    passwordField = browser.find_element(By.ID,"password").send_keys(password)
    time.sleep(1)    
    signinIdButton = browser.find_element(By.ID,"login-id")
    print("Signing you in...")
    signinIdButton.click()
    print("Sign in process complete")
finally:
    try:
        print("Closing browser")
    except PermissionError:
        print("Permission error")
    except WebDriverException:
        print("Webdriver error")