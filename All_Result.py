from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Firefox()
driver.get('https://onlinesggs.org/app/web/')

#s = '001002003004005006007008009010'
s = '006007008009010'

for i in range(5):

	initial_username  =  '2018bcs' 
	initial_password  =  '2018BCS'
	t=int(i*3)
	curr = s[t:(t+3)]
	user =  initial_username + curr
	passs  =  initial_password + curr

	username = driver.find_element_by_name("mobile")
	password = driver.find_element_by_name("password")

	username.send_keys(user)
	password.send_keys(passs)

	driver.find_element_by_name("sub").click()

	window_after = driver.window_handles[0]
	driver.switch_to.window(window_after)

	time.sleep(5)

	select = Select(driver.find_element_by_id('status'))
	select.select_by_value('Regular')
	select = Select(driver.find_element_by_name('year'))
	select.select_by_value('2 SEM1')
	driver.find_element_by_name("submit").click()

	uu= user
	one =  uu + '.png'
	path = '/home/rahul/Pictures/' + one

	time.sleep(3)

	driver.save_screenshot(path)
	driver.find_element_by_link_text("LogOut").click()

	time.sleep(3)