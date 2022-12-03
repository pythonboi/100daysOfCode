import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from time import sleep



# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)

# serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
#
# driver = webdriver.Chrome(service=serv_obj)

#  driver = webdriver.Chrome()

# m = driver.get("https://login.microsoftonline.com/8d0d81ba-ed03-4c6f-9248-a3b3967ca35c/saml2?SAMLRequest=pVJdj9MwEPwrkd%2Bd769abaVy5XQVB1c1BSRekGNvrtY5dvA6HP33pCmI44F74XV3Z3ZmNEvkvR7YZvQnc4BvI6APfvTaIJsXKzI6wyxHhczwHpB5wZrN%2B3uWhjEbnPVWWE1eQF5HcERwXllDgt12RW4Pb5u7zw%2BHd83XhaxEDlVOk7oQNJeipYu0rWiWVZmUbZxLWZLgEzic0CsykU0UiCPsDHpu%2FDSK05QmKY3TY1KwtGB58YUE28mRMtzPqJP3A7Io0vZRmbBXwlm0nbdGKwOhsH1Uy1jWScspyDijuSi7SUZeU5612aKsBM8KEV18piTY%2F7L%2FRhmpzOPrztvrEbK743FP9w%2FNkQSb32ncWINjD64B910J%2BHi4%2F6OVa%2BVPZ0498D7sz50DPD1b94SzXhyiy4soncTlVZmXWZkVxSKu40hwrVsunsh6eRHM5rTc%2Br95e%2FBccs%2BX0Uva5bVIHybju%2B3eaiXOwa11Pff%2FziUJk3miJO3mUzYaHECoToGc4tHaPt844B5WxLsRSBCtr1%2F%2Fbuz6Jw%3D%3D&RelayState=https%3A%2F%2Falithya-team.myfreshworks.com%2Fsp%2FSAML%2F296747646363559080%2Flogin&sso_reload=true")

# driver.get("https://helpdesk.alithya.com/a/dashboard/default")

# username = driver.find_element(By.NAME, "loginfmt").send_keys("hafeez.tukuru@alithya.com")
# clickNext = driver.find_element(By.ID, "idSIButton9").click()
#
# Pass= driver.find_element(By.ID, "i0118").send_keys("FastRideMatters#87")

#signIN = driver.find_element(By.ID, "idSIButton9").click()


# driver.find_element(By.CSS_SELECTOR, "css-ix6cs0-PrimaryText" ).click()


driver = webdriver.Chrome()

myService = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://helpdesk.alithya.com/a/tickets/view/178891?default_query=0")

driver.maximize_window()

driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/div/div/div/div/div[2]/div[1]/div/button").click()

driver.implicitly_wait(10)

driver.find_element(By.ID, "i0116").send_keys("hafeez.tukuru@alithya.com")
driver.find_element(By.ID, "idSIButton9").click()
driver.find_element(By.ID, "i0118").send_keys("FastRideMatters#87")
driver.find_element(By.XPATH, "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[4]/div[2]/div/div/div/div/input").click()

driver.implicitly_wait(20)


# driver.find_element(By.NAME, "username").send_keys("hafeez.tukuru@alithya.com")
# driver.find_element(By.ID, "password").send_keys("FastRideMatters#87")
# driver.find_element(By.CLASS_NAME, "css-o1ejds").click()


#driver.find_element(By.TAG_NAME, "/support/login")

time.sleep(40)
#/html/body/div[4]/div[2]/div/div/div/div/div/div[2]/div[1]/div/button


