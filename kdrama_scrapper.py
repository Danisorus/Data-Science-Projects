#
# KDrama Web Scrapper
#
# Created by Daniel Augustine

from bs4 import BeautifulSoup as soup
from selenium import webdriver
from urllib.parse import urljoin

#create a csv file
filename = "kdramas.csv"
#open the file and write in it
f = open(filename, "w")	
headers = "Show, Episode, Time Added, Language\n"	#create headers to be added in the csv file
f.write(headers)	#write the headers to the csv file

my_url = 'https://www1.dramacool.sk/recently-added'		#url that is going to be scrapped

#opens url in web browser
driver = webdriver.Chrome(executable_path='C:/Users/danie/Desktop/WebScrapping/Chromedriver/chromedriver.exe')
driver.get(my_url)

#default time stamps needed for calculating the string length of the date show was added
time_template = '24 hours ago'
time_template2 = '60 minutes ago'

#function the scrapes the site and gathers the following data:
#show title, episode number, date/time the show was added to the site, and subtitle presence
#a list of the shows is passed in as a parameter
def show_scrapper(show_list):
	for s in show_list:
		
		#grab the title of the show
		legal = set(' ().,/?~ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijlkmnopqrstuvwxyz1234567890') #a set of legal characters allowed to printed 
		#checks to see if there is an illegal character present in a show title
		if UnicodeEncodeError:	#if there is one or more present replace it with the give acceptable character
			show_title = ''.join(char if char in legal else '-' for char in s.find('h3').text)
		else:	#else store the show title as is
			show_title = s.find('h3').text

		#grab the time slot and check if the date a show was added is in either a time format (ie. 3 hours ago) or a date format (ie. 11-23-2020)
		#if the time slot value is in a time format store it as a time, else store as a date
		if len(s.find('span',{'class':'time'}).text) <= len(time_template) or len(s.find('span',{'class':'time'}).text) <= len(time_template2):
			time_added = s.find('span',{'class':'time'}).text
		else:
			time_added = s.find('span',{'class':'time'}).text.split(" ")[0]

		#grab the episode number
		#check to see if the episode is in subbed or raw
		if s.find('span',{'class':'ep SUB'}):
			episode_txt = s.findAll('span')[2].text
			episode = s.findAll('span')[2]
			lang = episode['class'][3:]
		else:
			episode_txt = s.findAll('span')[2].text
			episode = s.findAll('span')[2]
			lang = episode['class'][3:]

		#writing to a new file
		f.write(show_title.replace(',', ' ') + "," + episode_txt + "," + time_added + "," + lang + "\n")

#function for parsing the html and locating the list of shows
def webpage_parser():
    #html parser
	page = driver.page_source
	page_soup = soup(page, "html.parser", multi_valued_attributes=None)

	#locating the list of shows
	containers = page_soup.findAll('div',{'class':'block tab-container'})[0]
	container = containers.find('div',{'class':'tab-content left-tab-1 selected'})		

	return container	#return the container the holds the shows to be used later

webpage_parser()	#call function

#find the total number of pages on the site
container2 = webpage_parser().findAll('ul')[1].findAll('li')
library_num = int(container2[-1].find('a',{'data-page':'1'}).get('href')[6:])


#go through the first 2 pages and scrape the data
for i in range(2):
    
	#get the list of shows
	container1 = webpage_parser().findAll('ul')[0]
	show_list = container1.findAll('li')	#list of shows

	#call function
	show_scrapper(show_list)

	#get the next page
	next_page = webpage_parser().find('ul',{'class':'pagination'}).find('li',{'class':'next'})

	if next_page:
    	#get the link of the next page
		page_link = next_page.find('a').get('href')
		my_url = urljoin(my_url,page_link)	#used to get the full link of the next page
		#open the next page
		driver.get(my_url)
	else:
    		break	#break once the last page has been reached
		
f.close()	#close the file