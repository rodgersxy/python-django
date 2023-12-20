#open firefox and directs to instagram.com login page

from time import sleep
from selenium import webdriver

browser = webdriver.Firefox()

browser.get('https://www.instagram.com/')

sleep(15)