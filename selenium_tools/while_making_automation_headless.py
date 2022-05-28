# Programme : while_making_autimation_headless
# Description : This method make the automation invisible to the user
# Date : 23/05/2022
# Author : Christophe Lagaillarde
# Version : 1.0

from selenium import webdriver


def while_making_automation_headless() -> webdriver:
    options = webdriver.EdgeOptions()
    options.headless = True
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    driver = webdriver.Edge(executable_path="msedgedriver.exe", options=options)
    return driver