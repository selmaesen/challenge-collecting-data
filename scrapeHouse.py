from selenium import webdriver
import re
import time 


def do_it(url):
    options = webdriver.ChromeOptions()
    options.add_argument("headless")

    browser = webdriver.Chrome(options=options)
    browser.get(url)

    # get 3 lists of web elements
    result = browser.find_elements_by_class_name('classified-table__row')

    result2 = browser.find_elements_by_class_name('classified-table__header')
    result3 = browser.find_elements_by_class_name('classified-table__data')



    dictionary = {}
    # go through each webElement and checks if they are in the same row then it adds the key and the value in a dictionary
    for i in range(len(result) - 5):
        res = result[i].text
        type_of_data = result2[i].text
        data = result3[i].text
        if (type_of_data in res) and (data in res):
            dictionary[type_of_data] = data

    

    # get price variable
    price = browser.find_element_by_class_name('sr-only').text
    # get the type of property this is
    type_of_property = browser.find_element_by_class_name('classified__title').text 
    if 'House' in type_of_property:
        type_of_property = 'House'
    elif 'Apartment' in type_of_property:
        type_of_property = 'Apartment'

    # get locality
    try :
        raw_locality = browser.find_element_by_class_name('classified__information--address-clickable').text
        locality_list = re.findall(r'\d{4}', raw_locality)
        locality = locality_list[0]
    except:
        locality = 'Not specified'

    

    #number of facades
    if 'Facades' in dictionary:
        facades = dictionary['Facades']

    #number of rooms 
    if 'Bedrooms' in dictionary:
        rooms = dictionary['Bedrooms']
    else:
        rooms = 'Not specified'

    #kitchen type
    if 'Kitchen type' in dictionary:
        kitchen_type = dictionary['Kitchen type']
    else:
        kitchen_type = 'Not specified'

#state of the building

    if 'Building condition' in dictionary:
        building_state = dictionary['Building condition']
    else:
        building_state = 'Not specified'

    if type_of_property == 'House':
        garden = "1"
    else: 
        garden = "0"

    
    if 'Living area' in dictionary:
        area = dictionary['Living area'].replace("\nsquare meters", "")
    else:
        area = 'Not specified'

    if 'Swimming pool' in dictionary:
        pool = '1'
    else :
        pool = '0'

    if 'Fireplace' in dictionary:
        fireplace = '1'
    else:
        fireplace = '0'


    file = open('/Users/adamflasse/Development/python/projects/Scraping/house3.txt', "a") 
    file.write(locality +','+ type_of_property +','+ price +','+ area +','+ building_state +','+ rooms +','+ facades +','+ kitchen_type +','+ garden +','+ fireplace +','+ pool + "\n")
    file.close()

    time.sleep(1)
    browser.close()




with open('/Users/adamflasse/Development/python/projects/Scraping/country2.txt', "r") as fichier:
    files = open('/Users/adamflasse/Development/python/projects/Scraping/house3.txt', "a")
    files.write('Locality,type of property,price,area,building state,rooms,facades,kitchen type,garden,fireplace,swimming pool\n')
    files.close()
    i = 0
    e = 0
    for line in fichier:
        try:
            do_it(line)
        except:
            e += 1
            print('There are ' + str(e) + ' errors')
            continue
        i += 1
        if i % 75 == 0:
            time.sleep(100)
        print(i)
    
    print('Done')



    