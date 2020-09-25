from bs4 import BeautifulSoup
import requests
import re
import urllib3
import json
import csv

#url for each property
source = requests.get("https://www.immoweb.be/en/classified/apartment-block/for-sale/liege/4020/8775843?searchId=5f6ddbba25af1")

soup = BeautifulSoup(source.text,'lxml')

#Price
p= soup.find_all('span')
Price = p[1].text

#No of Rooms
no_of_rooms = soup.find("span", class_= "overview__text").text
rooms = no_of_rooms.replace(" ","").strip()

# All the Information about the property
house_detail = soup.findAll("table", {'class' : "classified-table"})

item = []
itemvalue= []

try :
    
    for j in range(len(house_detail)-1):
        house_general= house_detail[j].findAll('tr')
        for i in range(len(house_general)-1) : 
            item.append(house_general[i].th.contents)
            itemvalue.append(house_general[i].td.contents)

except :
    pass

item_s = []
itemvalue_s= []

for i in range(len(item)-1):
    item_s.append(str(item[i][0]).strip())
 
#print(item_s)

for x in range(len(itemvalue)-1):
    itemvalue_s.append(str(itemvalue[x][0].strip()))

#print(itemvalue_s)

property_info  = dict(zip(item_s,itemvalue_s))
property_info['No_of_rooms'] = rooms
property_info['Price'] = Price

#print(property_info)



#belgium = pd.DataFrame({'Locality': titles,
#                           'Type of property' :
#                           'Subtype of property' :
#                           'Price': ,
#                           'Type of sale' :
#                           'Number of rooms': 
#                           'Area(m²)': ,
#                           'Fully equipped kitchen': ,
#                           'Furnished : ,
#                           'Open fire ': ,
#                           'Terrace': ,
#                           'facades': ,
#                           'Swimming pool': 
#                           'State of the building' : 
#                                                    })[    ]
#


#test to write in csv file
#with open('test.csv', 'w') as f:
##    for key in property_info.keys():
##        f.write("%s,%s\n"%(key,property_info[key]))
#

