<<<<<<< HEAD
## ImmoEliza project.

This is a script wich scrape ImmoWeb website for house's data such as the price of a house, the locality, numbers of rooms, area, ....

There is two parts of the script.

#Part one

The script "immoscrapGood.py" search for links in a list page showing all of their houses.
The goal here was to scrape into that dynamic list and take each house's link reference.
BeautifulSoup was not an option here because of the nature of the list.
So we've noticed that the url takes care of the index of the pages wich in this case was really helpful bacause we can iterate though that link.
Every links are stored in a text file that gonna be used for part two!

#Part two

This wasn't easy. We've scratched our heads hard on how to scrape each houses data. BeautifulSoup was working here because of the static content but it was really hard to gather all information in good shape due to how the website was coded.
But again Selenium worked.

The goal here is to iterate through each url we gathered with the first script and scrape the information through each pages.

I've had to "simulate" each windows opening because my computer had too much difficulties to repeat the process for about 12000 times. So I've made them headless.



So the script works fine, there are some data missing wich I've noticed quite too late. (24h after the script already begun)
There were 4000 errors due to, in my opinion, the urls dynamicly changing. 
So I've ended up with 8300 inputs.

I think that with some modifications (I'm thinking about the missing data) and with a up to date url file, the challenge would have been 100% complete.
=======
# Data Scraping Project

This project is the first project for BeCode AI/Data Operotor training, Bouman class. Adam Flusse, Ankita Haldia and Selma Esen have worked on this repository.
 
## Date

23/09/2020 - 25/09/2020

## The Mission

The real estate company "ImmoEliza" wants to create a machine learning model to make price predictions on real estate sales in Belgium. You must therefore create a dataset that holds the following columns :

Locality
Type of property (House/apartment)
Subtype of property (Bungalow, Chalet, Mansion, ...)
Price
Type of sale (Exclusion of life sales)
Number of rooms
Area
Fully equipped kitchen (Yes/No)
Furnished (Yes/No)
Open fire (Yes/No)
Terrace (Yes/No)
If yes: Area
Garden (Yes/No)
If yes: Area
Surface of the land
Surface area of the plot of land
Number of facades
Swimming pool (Yes/No)
State of the building (New, to be renovated, ...)
You must save everything in a csv file.

This data set should contain at least 10.000 input for all Belgium.


>>>>>>> origin/selma
