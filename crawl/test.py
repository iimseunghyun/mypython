from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
url = 'https://google.com'
driver.get(url)

driver.find_element_by_css_selector('.gLFyf.gsfi').send_keys('롱아일랜드아이스티')
driver.find_element_by_css_selector('.gLFyf.gsfi').send_keys(Keys.ENTER)

target = driver.find_elements_by_css_selector('.LC20lb')
for i in range(len(target)):
    target[i].click()
