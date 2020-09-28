from bs4 import BeautifulSoup
import requests
import re
import pandas
import csv
import os
from time import sleep
import time 
from random import randint
import warnings
from IPython.core.display import clear_output


fpath = 'listtt.txt'
with open(fpath,'r') as fp:
    for cnt, line in enumerate(fp):
        url = line

# Preparing the monitoring of the loop
        start_time = time.time()
        request = 0

        # Make a get request
        
        source = requests.get(url)
        # Throw a warning for non-200 status codes
        if source.status_code != 200:
            warnings.warn('Request: {}; Status code: {}'.format(requests, source.status_code))
            
        
        # Pause the loop
        sleep(randint(3,5))

            
        # Monitor the requests
        request += 1
        elapsed_time = time.time() - start_time
        print('Request:{}; Frequency: {} requests/s'.format(request, elapsed_time))
        clear_output(wait = True)
        
        # Break the loop if the number of requests is greater than expected
        if request > 72:
            warnings.warn('Number of requests was greater than expected.')
            

        # Parse the content of the request with BeautifulSoup
        
        soup = BeautifulSoup(source.text,'lxml')


        # Immoweb code
        try :

            house_code = soup.find("div", {'class' : "classified__information--immoweb-code"})
            codelist = house_code.text.split()
            code = codelist[3]
            print(code)
        except : 
            print("incode")
            code = "none"
        
        #Price
        try :
            price = soup.find("span",{"aria-hidden":"true"}).text

        
        except :
            pass
        #print (price)

        #Type of property (House/apartment) and the suptype if it is house 
        try :

            prop_types = ["House","Apartment"] 

            house_subtype = ["House","Town-house","Mansion","Mixed-use building","Pavilion","Villa","Farm house", "Apartment Block"
                          "Country cottage", "Castle", "Bungalow", "Chalet","Manor house","Exceptional property",
                          "Other property"]
            apartments_subtype = ["Apartment", "Studio" , "Penthouse", "Duplex" , "triplex", 'Loft', 'Service flat']

            type_prop = soup.find("div",{"class":"classified__header-content"}).find("h1",{"class":"classified__title"})
            type_prop = type_prop.text
            type_prop = type_prop.strip()


            for a_subtype in apartments_subtype :
                if type_prop.find(a_subtype) != -1 :
                    property_is = "Apartment"
                    property_subtype_is = a_subtype
                    break
                else :
                    for h_subtype in house_subtype : 
                        if h_subtype in type_prop :
                            property_is = "House"
                            property_subtype_is = h_subtype
                            break
                        else :
                            property_is = "Others"
                            property_subtype_is = "others"
       
          
        # To get the type of sale of the property
            type_of_sale = ["new build","New real estate project" , "public sale", "annuity sale" , "for sale" ]
            sale_type = " "

            for s in range(len(type_of_sale)-1) :

                if type_prop.find(type_of_sale[s]) != -1 and type_prop.find(type_of_sale[s]) != "for sale" :
                    sale_type = type_of_sale[s]
                elif type_prop.find(type_of_sale[s]) == -1  : 
                    sale_type = "for sale" 
            
        except : 
            pass    

        

        # the zip code of the property: we get it from url itself.
        try :
            locality = 0    
            list_url = url.split("/")

            for n in list_url:
                if len(n) == 4 :
                    match= re.search(r"\d{4}", n)
                    locality = n
        except :
            pass

        
        #No of Rooms
        try :
            no_of_rooms = soup.find("span", class_= "overview__text")
            rooms  = ""
         
            if no_of_rooms == "None" :
                rooms = "Not specified"
            else :
                rooms = no_of_rooms.text.replace(" ","").strip()
                for char in rooms :
                    if char.isdigit() == True :
                        rooms = char
                        break
               
        except :
            rooms = "Not specified"

        
        # All the Information about the property
        house_detail = soup.findAll("table", {'class' : "classified-table"})


        item = []
        itemvalue= []
        try:
            for j in range(len(house_detail)-1):
                house_general= house_detail[j].findAll('tr')
                for i in range(len(house_general)-1) : 
                    item.append(house_general[i].th.contents)
                    itemvalue.append(house_general[i].td.contents)

        except :
            pass
        
        item_s = []
        itemvalue_s= []

        try :

            for i in range(len(item)-1):
                item_s.append(str(item[i][0]).strip())


            for x in range(len(itemvalue)-1):
                itemvalue_s.append(str(itemvalue[x][0].strip()))

        #print(itemvalue_s)

            property_info  = dict(zip(item_s,itemvalue_s))
            property_info['No_of_rooms'] = rooms
            property_info['Price'] = price
            property_info['Locality'] = locality
            property_info['Type of Property'] = property_is
            property_info['Subtype of property'] = property_subtype_is
            property_info['Type of sale'] = sale_type
            property_info['Immoweb code'] = code
    
        except :
            pass

        
        try: 
            belgium_properties = ['Immoweb code','Locality','Type of Property','Subtype of property','Price',
                          'Type of sale', 'No_of_rooms','area', 'Kitchen type','Furnished ' ,
                               'Fireplace ' ,'Terrace' , 'Garden' ,'Facades' , 'Swimming pool', 'Building condition']
            belgium_dict = {}

            for element in belgium_properties : 
                for key in property_info.keys() :
                    if key.find(element) != -1 :
                        belgium_dict[element] = property_info[key]
                        break
                    else :
                        belgium_dict[element] = '0'
        except :
            pass
        

        try :
            def is_file_empty(file_name):
                '''Check if file is empty by reading first character in it'''

                # open file in read mode
                with open(file_name, 'r') as read_obj:
                # read first character
                    one_char = read_obj.read(1)
                # if not fetched then file is empty
                    if not one_char:
                        return True
                return False

        
            
            with open('immoweb_data.csv', 'a') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=belgium_dict.keys())
                file_name = 'immoweb_data.csv'
        # check if file exist and it is empty
                is_empty = is_file_empty(file_name)
                
                if is_empty:
                    writer.writeheader()
                writer.writerow(belgium_dict)

        except IOError:
            pass


        try:
            with open('immo_other.csv', 'a') as csvf:
                writer = csv.DictWriter(csvf, fieldnames=property_info.keys())
                writer.writeheader()
                writer.writerow(property_info)

        except IOError:
            pass


# End 
