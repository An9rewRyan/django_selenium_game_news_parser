from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox( executable_path='geckodriver.exe')
driver.get("https://vk.com/feed")

name = str(input('Ану вводи, кому писать будешь(лучше не ошибись нахуй):'))
number = str(input('Ану вводи, свой номер(лучше не ошибись нахуй):'))
pass_ = str(input('Ану вводи, свой пароль(я ВСЕ помню):'))

elem = driver.find_element_by_id("email")
elem.send_keys("{}".format(number))

elem = driver.find_element_by_id("pass")
elem.send_keys("{}".format(pass_))

elem = driver.find_element_by_id("login_button")
elem.send_keys(Keys.ENTER)

time.sleep(3)

driver.get("https://vk.com/im")

elem = driver.find_element_by_xpath("//span[text()='{}']".format(name)).click()

elem= driver.find_element_by_id("im_editable0")

elem.send_keys('Привет, меня зовут Selenium!(от пользователя {})'.format(number))
elem.send_keys(Keys.ENTER)

assert "No results found." not in driver.page_source
