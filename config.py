DRIVING_NUMBER = "xxxxxxxxxxxxxxx"
TEST_CENTER = "BALLYMENA"
DAYS = ["Monday", "Tuesday","Wednesday", 'Thursday', "Friday"]
DATE_OF_BIRTH = "03/10/1999"
TEST_CATEGORY = "Motorcar"
SPECIAL_REQUIREMENT = "No"
URL = "https://www.dvtaonlineni.gov.uk/public/bookDrivingTest_1CollectInfo.aspx"


if __name__ == "__main__":
    print("=======================")
    print("         Debug")
    print ("Driving Number: " + DRIVING_NUMBER)
    print("Test Center: " + TEST_CENTER)
    print("Days: " + str(DAYS))
    print("Date of birth: " + DATE_OF_BIRTH)
    print("Test Category: " + TEST_CATEGORY)
    print("Special Requirements: " + SPECIAL_REQUIREMENT)
    print("URL: " + URL)
    print("=======================")

    count = 8
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
    
    if count == 3:
        dates = "1st and 27th"
    elif count == 4 or count == 6 or count == 9 or count == 11:
        dates = "1st and 30th"
    else:
        dates = "1st and 31st"
    
    print("A Booking is avaliable in " + month + " between the dates " + str(dates))