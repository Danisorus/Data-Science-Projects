Hi,

For this project I decided to create a web scraper for one of my favorite kdrama websites. 

It pulls from the list of shows the following data:
-The show title
-The latest episode number
-The date/time it was added
-Whether or not if the episode is subbed or in its raw language

In this file you will find two python program:
1) gives you a csv file of the full list of all the shows ever added to the site (denoted full-list) ***as of 11/29/2021***
2) gives the a csv file of the first pages on the site  ***as of 11/29/2021)**

If you do not want to run the program yourself that is totally fine. just open the two csv files to view the results. However, run the code to get the lastest list of shows from the site. There is also chromedriver folder that holds the chromedriver executable in case you dont want to use the default web browser I chose and you want to use chrome.

Steps to change the web broswer:
-add this line of code above 'driver.get(my_url)'
driver = webdriver.Chrome(executable_path='/Chromedriver/chromedriver.exe')

Thanks for taking the time to view my work! :)
