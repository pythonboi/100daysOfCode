import sys
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep

failedTicket = []
ticRegex = []

server_Site = {}

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

myService = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://helpdesk.alithya.com/a/tickets/view/178891?default_query=0")

driver.maximize_window()

time.sleep(2)

driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div/div/div/div/div[2]/div[1]/div/button').click()

driver.implicitly_wait(10)

driver.find_element(By.ID, "i0116").send_keys("hafeez.tukuru@alithya.com")
driver.find_element(By.ID, "idSIButton9").click()

myPass = r"C:\Users\htukuru\PycharmProjects\100daysOfCode\Selenium\venv\pass.txt"

time.sleep(2)

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
ticketYellow = driver.find_elements(By.PARTIAL_LINK_TEXT, "[Warning]")

for ticket in tickets:

    failedTicket.append(ticket.text)

for ticket in ticketYellow:

    failedTicket.append(ticket.text)

print(failedTicket)

# This is for getting only the ticket numbers from the ticket discription
for readRegex in failedTicket:
    reGex = re.search(r"[-](\d+)", readRegex)

    ticRegex.append(reGex.group(1))

print(ticRegex)
print(len(ticRegex))

driver.implicitly_wait(10)

for count in ticRegex:

    driver.find_element(By.ID, "header_search").send_keys(count)

    driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[2]/div/div[4]/form/div/div/div/section/ul/li/a").click()
    time.sleep(3)
    # This is click to view more of the ticket description
    driver.find_element(By.XPATH, "/html/body/div[1]/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div/div/span/div/button").click()
    time.sleep(2)

    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #
    # getnoteText = driver.find_element(By.XPATH, "/html/body/div[1]/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div/div/span/div/div/table/tbody/tr[1]/td/table/tbody/tr[2]/td/table/tbody/tr[7]/td[2]/span").text
    # print(getnoteText)

    try:

        # getnoteText = driver.find_element(By.XPATH,
        #                                   "/html/body/div[1]/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div/div/span/div/div/table/tbody/tr[1]/td/table/tbody/tr[2]/td/table/tbody/tr[7]/td[2]/span").text
        # print(getnoteText)

        getnoteText = driver.find_element(By.XPATH, "//*[@class='view-more-component is-open has-view-more ']//table//tbody//td/span[contains(text(), 'Success')]").text
        print(getnoteText)

        if getnoteText == "Success" or getnoteText == "Warning":

            # Scroll down to the bottom page of the main window page
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # This click on the Add button
            driver.find_element(By.XPATH, "/html/body/div[1]/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/section/div/div[1]/button[3]/span[1]").click()

            # This is for the writing on the txt field
            driver.find_element(By.XPATH,
                                "/html/body/div[1]/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/section/div/div/div/div[3]/div[1]/div/div/div[3]/div/p").send_keys("The backup job was successful ")

            time.sleep(5)

            # This click the update button
            driver.find_element(By.XPATH, "/html/body/div[1]/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/section/div/div/div/div[5]/div/div[2]/div/div/button").click()

            time.sleep(5)

            #This is for clicking the drop down button for the Status
            driver.find_element(By.XPATH,
                                "/html/body/div[1]/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div[2]/div[1]/section[3]/div/div/section/section/div/div/div/form/div[1]/div/div[2]/div/div[1]/span[1]").click()

            # This is for selecting the close button
            driver.find_element(By.XPATH,
                                "//ul[@class='ember-power-select-options ember-power-select-single-list ember-view']/li[6]").click()

            time.sleep(3)

            scrollAgent = driver.find_element(By.XPATH, "/html/body/div[1]/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div[2]/div[1]/section[3]/div/div/section/section/div/div/div/form/div[1]/div/div[8]/div/div[1]/span[1]")
            driver.execute_script("arguments[0].scrollIntoView(true);", scrollAgent);

            time.sleep(3)

            # This is for selecting the Agent
            driver.find_element(By.XPATH, "/html/body/div[1]/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div[2]/div[1]/section[3]/div/div/section/section/div/div/div/form/div[1]/div/div[8]/div/div[1]/span[1]").click()

            #This is for selecting the Agent name/user
            driver.find_element(By.XPATH, "//ul[@class='ember-power-select-options ember-power-select-single-list ember-view']/li[4]").click()

            time.sleep(3)

            # This is for the Category selection
            driver.find_element(By.XPATH,
                                "/html/body/div[1]/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div[2]/div[1]/section[3]/div/div/section/section/div/div/div/form/div[1]/div/div[10]/div/div[1]/span[1]").click()

            driver.find_element(By.XPATH,
                                "//ul[@class='ember-power-select-options ember-power-select-single-list ember-view']/li[8]").click()

            time.sleep(2)

            # selecting the sub-category
            driver.find_element(By.XPATH,
                                "/html/body/div[1]/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div[2]/div[1]/section[3]/div/div/section/section/div/div/div/form/div[1]/div/div[11]/div[1]/div/div[1]/span[1]").click()

            driver.find_element(By.XPATH,
                                "//ul[@class='ember-power-select-options ember-power-select-single-list ember-view']/li[11]").click()

            time.sleep(2)

            # The update button
            driver.find_element(By.ID, "form-submit").click()
            #driver.find_element(By.XPATH, "/html/body/div[1]/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div[2]/div[1]/section[3]/div/div/section/div/div/button").click()

            time.sleep(5)



    except:
        print("Error found in the code")

