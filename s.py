from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.instagram.com")
sleep(3)
driver.find_element_by_name('username').send_keys('user_find') #replace with your insta username 
sleep(1)
driver.find_element_by_name('password').send_keys('seen987') #replace with your insta pass
sleep(1)
driver.find_element_by_xpath("//button[@type='submit']").click()
sleep(10)
driver.get('https://www.instagram.com/manoj_34_manoj') #replace the username in last after .com
sleep(5)
driver.find_element_by_class_name("_abl-").click()#id click
sleep(3)
driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/button[3]').click()#report
sleep(3)
driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/button[2]/div').click()report account
sleep(3)
driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/button[2]/div').click()#its pretending to soemone
sleep(3) 
driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/fieldset/div[1]/label/div').click()#me 
sleep(3)
driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[6]').click()#submit report
sleep(3)
driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div[4]/button').click()#close
sleep(20)
