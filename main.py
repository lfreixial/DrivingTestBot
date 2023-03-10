
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
time.sleep(5)

#Drop down
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

time.sleep(5)
Output = driver.find_element_by_class_name("slotListDiv").text
#print(Output)

time.sleep(5)
while foundDate == False:

    if "Sorry, there are no appointments" in Output and foundDate == False:
        time.sleep(5)
        Output = driver.find_element_by_class_name("slotListDiv").text
        BACK_BUTTON = driver.find_element_by_name("navButtons$prevButton")
        BACK_BUTTON.click()
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

        SEARCH_BUTTON = driver.find_element_by_name('navButtons$nextButton')
        SEARCH_BUTTON.click()
        time.sleep(5)
        
    else:
        foundDate = True

