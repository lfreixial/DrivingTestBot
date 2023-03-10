
import config

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import datetime
from twilio.rest import Client


options = FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)

driver.get(config.URL)

html = driver.page_source
soup = BeautifulSoup(html)

foundDate = False


DRIVING_LICENCE_NUMBER_ID = "BSP_Driver_DriverNo"
DATE_OF_BIRTH_ID = "BSP_Driver_DateOfBirth"
DRIVING_LICENCE_NUMBER_ID_BOX = driver.find_element_by_name(DRIVING_LICENCE_NUMBER_ID)
DATE_OF_BIRTH_ID_BOX = driver.find_element_by_name(DATE_OF_BIRTH_ID)

#Radio button
if config.TEST_CATEGORY == "Motorcar":
    TEST_CATEGORY_ID_BOX = driver.find_element_by_id("BSP_DriverTestCategory_ID_option0")
elif config.TEST_CATEGORY == "Small Sized Motorcycle":
    TEST_CATEGORY_ID_BOX = driver.find_element_by_id("BSP_DriverTestCategory_ID_option1")
elif config.TEST_CATEGORY == "Medium Sized Motorcycle":
    TEST_CATEGORY_ID_BOX = driver.find_element_by_id("BSP_DriverTestCategory_ID_option2")
elif config.TEST_CATEGORY == "Large Sized Motorcyle":
    TEST_CATEGORY_ID_BOX = driver.find_element_by_id("BSP_DriverTestCategory_ID_option3")
else:
    TEST_CATEGORY_ID_BOX = driver.find_element_by_id("BSP_DriverTestCategory_ID_option4")
    
if config.SPECIAL_REQUIREMENT == "No":
    SPECIAL_REQUIREMENT_ID_BOX = driver.find_element_by_id("drvSpecialRequirements_option0")
    print("No")
else:
    SPECIAL_REQUIREMENT_ID_BOX = driver.find_element_by_id("drvSpecialRequirements_option1")
    print("Yes")


DRIVING_LICENCE_NUMBER_ID_BOX.send_keys(config.DRIVING_NUMBER)
DATE_OF_BIRTH_ID_BOX.send_keys(config.DATE_OF_BIRTH)
SPECIAL_REQUIREMENT_ID_BOX.click()
TEST_CATEGORY_ID_BOX.click()


NEXT_BUTTON = driver.find_element_by_name("navButtons$nextButton")
NEXT_BUTTON.click()

changed_url = "https://www.dvtaonlineni.gov.uk/public/bookDrivingTest_3aTestCentreResults.aspx"

WebDriverWait(driver, 10).until(EC.url_changes(changed_url))
print("DONE")

select = Select(driver.find_element_by_id('slotTestCentre'))
select.select_by_visible_text(config.TEST_CENTER)

todaysDay = datetime.datetime.today().day
count = datetime.datetime.today().month
print(count)




max_month = Select(driver.find_element_by_id('slotSearchEndDate_month'))
max_month.select_by_value(str(count))

max_day = Select(driver.find_element_by_id("slotSearchEndDate_day"))
if count == 8 or count == 10 or count == 12:
    max_day.select_by_value('31')
else:
    max_day.select_by_value('30')


day = Select(driver.find_element_by_id('slotSearchStartDate_day'))
day.select_by_value(str(todaysDay))


month = Select(driver.find_element_by_id('slotSearchStartDate_month'))
month.select_by_value(str(count))


if "Monday" in config.DAYS:
    MondayCheck = driver.find_element_by_id("chkMonday")
    MondayCheck.click()
if "Tuesday" in config.DAYS:
    TuesdayCheck = driver.find_element_by_id("chkTuesday")
    TuesdayCheck.click()
if "Wednesday" in config.DAYS:
    WednesdayCheck = driver.find_element_by_id("chkWednesday")
    WednesdayCheck.click()
if "Thursday" in config.DAYS:
    ThursdayCheck = driver.find_element_by_id("chkThursday")
    ThursdayCheck.click()
if "Friday" in config.DAYS:
    FridayCheck = driver.find_element_by_id("chkFriday")
    FridayCheck.click()
if "Saturday" in config.DAYS:
    SaturdayCheck = driver.find_element_by_id("chkSaturday")
    SaturdayCheck.click()

SEARCH_BUTTON = driver.find_element_by_name('navButtons$nextButton')
SEARCH_BUTTON.click()

changed_url1 = "https://www.dvtaonlineni.gov.uk/public/bookDrivingTest_3aTestCentreResults.aspx"
WebDriverWait(driver, 10).until(EC.url_changes(changed_url1))
Output = driver.find_element_by_class_name("slotListDiv").text
errMessage = "Sorry, there are no appointments"
while foundDate == False:
    WebDriverWait(driver, 10).until(EC.url_changes(changed_url1))
    Output = driver.find_element_by_class_name("slotListDiv").text
    if "Sorry, there are no appointments" not in Output:
        # Your Account SID from twilio.com/console
        account_sid = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        # Your Auth Token from twilio.com/console
        auth_token  = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        client = Client(account_sid, auth_token)
        month = ""
        if count == 1:
            month = "January"
        elif count == 2:
            month = "February"
        elif count == 3:
            month = "March"
        elif count == 4:
            month = "April"
        elif count == 5:
            month = "May"
        elif count == 6:
            month = "June"
        elif count == 7:
            month = "July"
        elif count == 8:
            month = "August"
        elif count == 9:
            month = "September"
        elif count == 10:
            month = "October"
        elif count == 11:
            month = "November"
        else:
            month = "December"
        dates = ""
        if count == 3:
            dates = "1st and 27th"
        elif count == 4 or count == 6 or count == 9 or count == 11:
            dates = "1st and 30th"
        else:
            dates = "1st and 31st"
        message = client.messages.create(
            from_="xxxxxxxxxxxxxxxxxxxx", 
            to="xxxxxxxxxxxxxxxxxxx",
            body="A Booking is avaliable in " + month + " between the dates " + str(dates))
        errMessage = ""
        print(message.sid)


    BACK_BUTTON = driver.find_element_by_name("navButtons$prevButton")
    BACK_BUTTON.click()
    changed_url2 = "https://www.dvtaonlineni.gov.uk/public/bookDrivingTest_3TestCentre.aspx"
    WebDriverWait(driver, 10).until(EC.url_changes(changed_url2))
    count = count + 1

    if count > 12:
        count = datetime.datetime.today().month

    print("Count: " + str(count))

    if count == 8 or count == 10 or count == 12:
        max_month = Select(driver.find_element_by_id('slotSearchEndDate_month'))
        max_month.select_by_value(str(count))
    
    max_day = Select(driver.find_element_by_id("slotSearchEndDate_day"))
    if count == 8 or count == 10 or count == 12:
        max_day.select_by_value('31')
    else:
        max_day.select_by_value('30')

    max_month = Select(driver.find_element_by_id('slotSearchEndDate_month'))
    max_month.select_by_value(str(count))

    day = Select(driver.find_element_by_id('slotSearchStartDate_day'))
    if count != datetime.datetime.today().month:
        day.select_by_value('1')
    else:
        day.select_by_value(str(todaysDay))

    month = Select(driver.find_element_by_id('slotSearchStartDate_month'))
    month.select_by_value(str(count))

    #sleep to not get hit with api calls
    time.sleep (20)
    SEARCH_BUTTON = driver.find_element_by_name('navButtons$nextButton')
    SEARCH_BUTTON.click()        
