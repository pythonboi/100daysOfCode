import time
import re
#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains


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
ticketYellow = driver.find_elements(By.PARTIAL_LINK_TEXT, "[Warning]")

for ticket in tickets:

    failedTicket.append(ticket.text)

for ticket in ticketYellow:

    failedTicket.append(ticket.text)

print(failedTicket)

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

    try:

        getnoteText = driver.find_element(By.CSS_SELECTOR, "span[style='color: #00B050;']").text

        if getnoteText == "Success":

            driver.find_element(By.XPATH,
                                         "/html/body/div[1]/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div[2]/div[1]/section[3]/div/div/section/section/div/div/div/form/div[1]/div/div[2]/div/div[1]/span[1]").click()

            # This is selecting the close button
            driver.find_element(By.XPATH, "//ul[@class='ember-power-select-options ember-power-select-single-list ember-view']/li[5]").click()

            driver.implicitly_wait(5)

            # This is for scrolling down on the Properties section
            # scrollMe = driver.find_element(By.XPATH, "/html")

            # ac = ActionChains(driver)
            # ac.move_to_element(scrollMe).perform()

            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

            time.sleep(3)


            #driver.execute_script("arguments[0].scrollIntoView(true);", scrollMe);
            #
            # driver.implicitly_wait(5)

            driver.find_element(By.XPATH, "/html/body/div[1]/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/section/div/div[1]/button[3]/span[1]").click()
            #
            driver.implicitly_wait(5)
            # This is for the writing on the txt field
            driver.find_element(By.XPATH,
                                "/html/body/div[1]/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/section/div/div/div/div[3]/div[1]/div/div/div[3]/div/p").send_keys("The backup job was successful ")

            time.sleep(5)

            #
            driver.find_element(By.XPATH, "/html/body/div[1]/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/section/div/div/div/div[5]/div/div[2]/div/div/button").click()

            time.sleep(10)



    except:
        print("This is for Error or Warning status found")



# This is opening a new tab within the web-browser window

# driver.switch_to.new_window()
# driver.switch_to.window(driver.window_handles[1])


# time.sleep(40)



