from selenium import webdriver
import csv
from selenium.webdriver.common.keys import Keys
import time

url = "https://www.tripadvisor.com/Hotels-g293761-Victoria_Falls_Matabeleland_North_Province-Hotels.html"
driver = webdriver.Chrome("/Users/Kush/Desktop/chromedriver_win32/chromedriver")
driver.get(url)

time.sleep(2)
popup= driver.find_element_by_class_name("_1fwLpEHv")
popup.click()
time.sleep(2)
hotel_names = driver.find_elements_by_xpath(".//div[@class='listing_title']")
i=0
for i in range(0, 3):

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


        description = driver.find_element_by_class_name("cPQsENeY").text
        rating = driver.find_element_by_class_name("_3cjYfwwQ").text
        numrating = driver.find_element_by_class_name("_3jEYFo-z").text

        time.sleep(2)
        show_more = driver.find_element_by_class_name("_80614yz7")
        show_more.click
        time.sleep(2)
        amenities = driver.find_elements_by_xpath(".//div[@class='_2rdvbNSg']")
        amenities = ','.join([str(amenity.text) for amenity in amenities])

        csvWriter.writerow([hotel_name, price, description, rating, numrating,tripadvisor_link, amenities])
        driver.close
        driver.switch_to.window(pwd)
        driver.close
    next = driver.find_elements_by_xpath(".//a[@class='nav next ui_button primary']")
    next.click
    time.sleep(5)
