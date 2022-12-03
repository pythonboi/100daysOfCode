import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from time import sleep

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
#driver = webdriver.Chrome(chrome_options=options, service="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver = webdriver.Chrome(options=chrome_options)

myService = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://helpdesk.alithya.com/a/tickets/view/178891?default_query=0")

driver.maximize_window()

driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/div/div/div/div/div[2]/div[1]/div/button").click()

driver.implicitly_wait(10)

driver.find_element(By.ID, "i0116").send_keys("hafeez.tukuru@alithya.com")
driver.find_element(By.ID, "idSIButton9").click()

myPass = r"C:\Users\htukuru\PycharmProjects\100daysOfCode\Selenium\venv\pass.txt"

with open(myPass, 'r') as file:
    passGet = file.read()

    driver.find_element(By.ID, "i0118").send_keys(passGet)
driver.find_element(By.XPATH, "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[4]/div[2]/div/div/div/div/input").click()

driver.implicitly_wait(10)


getTitle = driver.title
myTitle = "Sign in to your account"

if getTitle == myTitle:
    driver.find_element(By.XPATH, "/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[2]/input").click()



driver.implicitly_wait(20)



time.sleep(40)



