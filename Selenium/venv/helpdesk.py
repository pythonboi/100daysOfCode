import time
import re
#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

from time import sleep

failedTicket = []
ticRegex = []

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

myService = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://helpdesk.alithya.com/a/tickets/view/178891?default_query=0")

driver.maximize_window()

driver.implicitly_wait(2)

driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div/div/div/div/div[2]/div[1]/div/button').click()

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

driver.implicitly_wait(10)



for count in ticRegex:

    numb = driver.find_element(By.ID, "header_search").send_keys(count)
    print("The is printing nothing None")
    print(numb)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[2]/div/div[4]/form/div/div/div/section/ul/li/a").click()
    time.sleep(3)
    # This is click to view more of the ticket description
    driver.find_element(By.XPATH, "/html/body/div[1]/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div/div/span/div/button").click()
    time.sleep(2)
    if count in ticRegex:
        print("I got here")
        try:

            getnoteText = driver.find_element(By.CSS_SELECTOR, "span[style='color: #00B050;']").text
            print("I am here")
            print(getnoteText)

            if getnoteText == "Success":

                driver.find_element(By.CSS_SELECTOR, "span[class='ember-power-select-selected-item']").send_keys()
                sel = Select(driver.find_element(By.XPATH, "/html/body/div[1]/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div[2]/div[1]/section[3]/div/div/section/section/div/div/div/form/div[1]/div/div[2]/div/div[1]/span[1]").click())

                sel.select_by_visible_text("Closed")
        except:
            print("This is for Error or Warning status found")


    #print(getnoteText)


# This is opening a new tab within the web-browser window

# driver.switch_to.new_window()
# driver.switch_to.window(driver.window_handles[1])


# time.sleep(40)



