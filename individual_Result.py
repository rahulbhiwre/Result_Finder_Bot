from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Firefox()
driver.get('https://onlinesggs.org/app/web/')



username = driver.find_element_by_name("mobile")
password = driver.find_element_by_name("password")

username.send_keys("2018bcs114@sggs.ac.in")
password.send_keys("2018BCS114")

driver.find_element_by_name("sub").click()

window_after = driver.window_handles[0]
driver.switch_to.window(window_after)



select = Select(driver.find_element_by_id('status'))
select.select_by_value('Regular')
select = Select(driver.find_element_by_name('year'))
select.select_by_value('2 SEM1')
driver.find_element_by_name("submit").click()


path = '/home/rahul/Pictures/abc1.png'
time.sleep(2)
driver.save_screenshot(path)
driver.find_element_by_link_text("LogOut").click()