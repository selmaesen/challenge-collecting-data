### Data Scraping Project
This project is the first project for BeCode AI/Data Operotor training, Bouman class. Adam Flusse, Ankita Haldia and Selma Esen have worked on this repository.

# Date
23/09/2020 - 25/09/2020

# The Mission
The real estate company "ImmoEliza" wants to create a machine learning model to make price predictions on real estate sales in Belgium. You must therefore create a dataset that holds the following columns :

Locality Type of property (House/apartment) Subtype of property (Bungalow, Chalet, Mansion, ...) Price Type of sale (Exclusion of life sales) Number of rooms Area Fully equipped kitchen (Yes/No) Furnished (Yes/No) Open fire (Yes/No) Terrace (Yes/No) If yes: Area Garden (Yes/No) If yes: Area Surface of the land Surface area of the plot of land Number of facades Swimming pool (Yes/No) State of the building (New, to be renovated, ...) You must save everything in a csv file.

This data set should contain at least 10.000 input for all Belgium.

# Part one
The script "immoscrapGood.py" search for links in a list page showing all of their houses. The goal here was to scrape into that dynamic list and take each house's link reference. BeautifulSoup was not an option here because of the nature of the list. So we've noticed that the url takes care of the index of the pages whch in this case was really helpful because we can iterate though that link. Every links are stored in a text file that gonna be used for part two!

The text file which includes the urls: country2.txt

# Part two
We have to create a data scraping code which should work on each url/page of advertisement. We tried two different ways: Selenium and BeautifulSoup.

# Selenium:
The goal here is to iterate through each url we gathered with the first script and scrape the information through each pages.

I've had to "simulate" each windows opening because my computer had too much difficulties to repeat the process for about 12000 times. So I've made them headless.

So the script works fine, there are some data missing wich I've noticed quite too late. (24h after the script already begun) There were 4000 errors due to, in my opinion, the urls dynamicly changing. So I've ended up with 8300 inputs.

I think that with some modifications (I'm thinking about the missing data) and with a up to date url file, the challenge would have been 100% complete.

The code: immoscrapGood.py The csv file: house3.csv

# BeautifulSoup:
It was not easy to work on immoweb with BeautifulSoup because of the nature of website. For some informations BeautifulSoup worked wine like price and the type of the property. But for example for locallity we have used RegEx to get zip code from the url itself.

The code: immoeliza.py The csv file: immoweb_data.csvhouse3.csv

# Used libraries:
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
from selenium import webdriver from selenium.webdriver.firefox.options import Options 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.action_chains import ActionChains



