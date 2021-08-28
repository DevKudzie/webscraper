#A couple of things to note are that this project is not complete yet, so as of now you are most likely to encounter errors
# This is my first project using Selenium by the way
#if this interests you and you find time, fix the following issues 
#issues
# 1 Click pagination and move to next page when first page is done
# 2 Figure out how to close a child window when you have collected the data for it. ~ this might possibly change how the loop works. The code works as is now, but you'll probably have a 100 tabs open when you loop through 99 hotels

from selenium import webdriver
import csv
from selenium.webdriver.common.keys import Keys
import time

#Get the url for the location whose Hotels you are looking for
url = "https://www.tripadvisor.com/Hotels-g293761-Victoria_Falls_Matabeleland_North_Province-Hotels.html"
driver = webdriver.Chrome("/Users/Kush/Desktop/chromedriver_win32/chromedriver")
driver.get(url)

time.sleep(2)
popup= driver.find_element_by_class_name("_1fwLpEHv")
popup.click()
time.sleep(2)
hotel_names = driver.find_elements_by_xpath(".//div[@class='listing_title']")

#loop through the page results
i=0
for hotelname in hotel_names:
    i = i+1
    hotel_name = hotelname.text
    hotel = driver.find_element_by_link_text(hotel_name)
    price = driver.find_element_by_xpath(".//div[@class='price __resizeWatch']").text

    tripadvisor_link = hotel.get_attribute('href')
    hotel.click()
    pwd = driver.window_handles[0]
    chwd = driver.window_handles[i]
    driver.switch_to.window(chwd)
    popup2= driver.find_element_by_class_name("_1fwLpEHv")
    time.sleep(1)
    popup2.click()
    # start collection data


    # default path to file to store data
    path_to_file = "/Users/kush/Desktop/accomodation.csv"
    csvFile = open(path_to_file, 'a', encoding="utf-8")
    csvWriter = csv.writer(csvFile)

    #Collect The data and insert it into the csv file
    description = driver.find_element_by_class_name("cPQsENeY").text
    rating = driver.find_element_by_class_name("_3cjYfwwQ").text
    numrating = driver.find_element_by_class_name("_3jEYFo-z").text

    time.sleep(2)
    show_more = driver.find_element_by_class_name("_80614yz7")
    show_more.click
    time.sleep(2)
    amenities = driver.find_elements_by_xpath(".//div[@class='_2rdvbNSg']")
    amenities = ','.join([str(amenity.text) for amenity in amenities])
    
    #This writes the file you have selected
    csvWriter.writerow([hotel_name, price, description, rating, numrating,tripadvisor_link, amenities])
    driver.close
    driver.switch_to.window(pwd)
    driver.close
    
   #This is for clicking the pagination, Haven't configured the loop for that yet.
# next = driver.find_elements_by_xpath(".//a[@class='nav next ui_button primary']")
# next.click
# time.sleep(5)
