from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time

all_links = []
type_of_property = ['house', 'apartment']



options = Options()
options.headless = True
for propriete in type_of_property:
    for i in range(2, 280):
        url = "https://www.immoweb.be/en/search/{}/for-sale?countries=BE&page={}&orderBy=newest".format(propriete, i)
        browser = webdriver.Chrome()
        browser.get(url)

        time.sleep(5)

# accepts cookies pop-up
        i_accept = browser.find_element_by_id('uc-btn-accept-banner')
        i_accept.send_keys(Keys.RETURN)

        time.sleep(3)
        need = propriete.capitalize()
        links = browser.find_elements_by_link_text(need)

        for link in links:
            result = link.get_attribute('href')
            all_links.append(result)
            print(result + "... " + str(len(all_links)) )
        browser.close()
        time.sleep(5)


with open('/Users/adamflasse/Development/country2.txt', "w") as file:
    for e in all_links:
        file.write(e + "\n")