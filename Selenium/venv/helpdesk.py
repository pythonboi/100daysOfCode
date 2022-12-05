import time
import re
#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from time import sleep
#failedTicket = ["AlithyaMontreal - [Failed] offsite AL-MTLW-FS01-IM\\Backup Job ALMTLW-FS...  #INC-99781', 'AlithyaMontreal - [Failed] offsite AL-MTL-WS-MON-IM\\Backup-AL-MTL-WS-M...  #INC-99780', 'AlithyaMontreal - [Failed] Offsite Northstar_Dev3-IM\\Backup Job...  #INC-99779', 'AlithyaMontreal - [Failed] offsite ALMTLW-DC01-IM\\Backup Job ALMTLW-DC...  #INC-99777', 'AlithyaMontreal - [Failed] Offsite-NorthStar_dev1-IM\\Back...  #INC-99776', 'AlithyaMontreal - [Failed] offsite AL-MTLW-FS01-IM\\Backup Job ALMTLW-FS...  #INC-99771', 'AlithyaMontreal - [Failed] Offsite Northstar_Dev3-IM\\Backup Job...  #INC-99767', 'AlithyaMontreal - [Failed] offsite AL-MTL-WS-MON-IM\\Backup-AL-MTL-WS-M...  #INC-99766', 'AlithyaMontreal - [Failed] Offsite Geoahall-IM\\Backup Job GeoAHall (1 VMs)  #INC-99765"]
failedTicket = []
ticRegex = []
#
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

myService = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://helpdesk.alithya.com/a/tickets/view/178891?default_query=0")

driver.maximize_window()

driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div/div/div/div/div[2]/div[1]/div/button').click()

#

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

driver.implicitly_wait(15)

tickets = driver.find_elements(By.PARTIAL_LINK_TEXT, "[Failed]")


for ticket in tickets:

    failedTicket.append(ticket.text)

print(failedTicket)

# time.sleep(5)

for readRegex in failedTicket:
    reGex = re.search(r"[-](\d+)", readRegex)

    ticRegex.append(reGex.group(1))

print(ticRegex)
print(len(ticRegex))


#[-](\d+)

# for tick in failedTicket:
#     driver.switch_to.new_window(tick)
#     driver.execute_script()
#     driver.implicitly_wait(15)
#     driver.close()

#/html/body/div[1]/div[8]/div[2]/div[1]/div/div/div[1]/div[3]/div[3]/section[2]/div[2]/div[1]/table/tbody/tr[1]/td[6]/div/a

#driver.implicitly_wait(20)

#ember-view subject-cell ember-tooltip-target



# time.sleep(40)



