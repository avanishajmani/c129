

#used to interact with webpage and automation testing(selenium)
from selenium import webdriver
#bs4 is a python module used for parsing (anyalysing) html text and then performing actions on it
from bs4 import BeautifulSoup
#importing time library so that the webpage can load propely before we start scraping
import time
#importing csv library so that we cna export the data that we ascrape into csv
import csv
#storing the website link
START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"
#ask the browser url to get the browser link so we can feed imformation and connect with chrome
browser = webdriver.Chrome("C:/Users/avani_i7gmgli/Downloads/chromedriver")
browser.get(START_URL)

time.sleep(10)



def scrape():
    #take the tags from the table to get data from it
    headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]
    planet_data = []
    #main loop which will run 428 and take over every single of piece of data that you seperate from the webpage or extract
    for i in range(0, 428):
        #extract the source using bs4 (browser page is the address of the webpage) using the function that is designed to analyse this designated webpage 
        soup = BeautifulSoup(browser.page_source, "html.parser")
        #identify differnt tags being used

        for each_ul_tag in soup.find_all("ul", attrs={"class", "exoplanet"}):
            li_tags = each_ul_tag.find_all("li")
            temp_list = []
            for each_index, each_li_tag in enumerate(li_tags):
                if each_index == 0:
                    #a means anchor tag for each li tag we are identifying the first li tag at index 0 seperately 
                    #this is done because the li tag at index 0 contains another html element : ANCHOR <a>...</a> which has dynanmic information which means it takes you to another page
                    #to separeate this we need to identify the anchor tag within the li tag at index 0
                    temp_list.append(each_li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(each_li_tag.contents[0])
                    except:
                        temp_list.append("")
            planet_data.append(temp_list)
            #xpath is another way of finding a path this the xpath that helps you identify the command .click allows you to click and go onto the next data
        nextButton = browser.findElement(By.xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a'))
        nextButton.click()
    with open("scrapper_2.csv", "w") as f:
        
        csvwriter = csv.writer(f)
        #writing the tags ie name light years from earth etc
        csvwriter.writerow(headers)
        #wrting all the data which is contained in the tags which is why plural rows
        csvwriter.writerows(planet_data)




scrape()