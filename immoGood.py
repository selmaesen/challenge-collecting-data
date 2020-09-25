from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time

all_links = []
type_of_property = ['house', 'apartment']

def just_do_it(page_min, page_max):
    
    for i in range(page_min, page_max):
        url = "https://www.immoweb.be/en/search/{}/for-sale?countries=BE&page={}&orderBy=newest".format(propriete, i)
        browser = webdriver.Chrome()
        browser.get(url)

        time.sleep(3)
        need = propriete.capitalize()
        links = browser.find_elements_by_link_text(need)

        for link in links:
            result = link.get_attribute('href')
            with open('/Users/adamflasse/Development/country2.txt', 'a') as file:
                file.write(result +  "\n")
            all_links.append(result)
            print(result + "... " + str(len(all_links)) )
        browser.close()
        time.sleep(5)


while len(all_links) < 10005:
    for propriete in type_of_property:
        just_do_it(2, 100)
        time.sleep(10)
        just_do_it(101, 200)
        time.sleep(10)
        just_do_it(201, 280)
        
    
    