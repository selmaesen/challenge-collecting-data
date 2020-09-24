from bs4 import BeautifulSoup
import requests
import re
import urllib3


source = requests.get("https://www.immoweb.be/en/classified/house/for-sale/heusden/9070/8951214?searchId=5f6b3fa532fe7")

soup = BeautifulSoup(source.text,'lxml')

house_container = soup.find("div", class_ = "classified__informations")
house_data = house_container.text.replace("  ","")
house_info = []
house_info = house_data.split('\n')

p= soup.find_all('span')
Price = p[1].text

#working on house location

#house_location = soup.find("div",{"class" : "classified__information--address"})
print(house_location)




house_details = soup.findAll("table", {'class' : "classified-table"})

item = []
itemvalue= []
    
for j in range(len(house_details)-1):
    house_general= house_details[j].findAll('tr')
    for i in range(len(house_general)-1) : 
        item.append(house_general[i].th.contents)
        itemvalue.append(house_general[i].td.contents)

item_s = []
itemvalue_s= []

for i in range(len(item)-1):
    item_s.append(str(item[i][0]).strip())
 
#print(item_s)

for x in range(len(itemvalue)-1):
    itemvalue_s.append(str(itemvalue[x][0].strip()))

#print(itemvalue_s)

Property_info  = dict(zip(item_s,itemvalue_s))
#print(Property_info)

#csv_file = open('cms_scrape.csv', 'w')
#csv_writer = csv.writer(csv_file)
#csv_writer.writerow('headline', 'summary','video_link')

