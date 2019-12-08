# Note this code have some bugs right now, we will improve it in future.

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time


def login_and_search():

    my_driver = webdriver.Chrome("C:\\chromedriver_win32\\chromedriver.exe")

    login_wait = WebDriverWait(my_driver, 30)

    my_driver.get("https://www.linkedin.com/uas/login")

    my_driver.maximize_window()

    email = my_driver.find_element_by_xpath('//*[@id="session_key-login"]')

    email.send_keys('amitsuneja007@gmail.com')

    time.sleep(2)

    password = my_driver.find_element_by_xpath('//*[@id="session_password-login"]')

    password.send_keys('****************************')

    time.sleep(2)

    login = my_driver.find_element_by_xpath('//*[@id="btn-primary"]')

    login.click()
    time.sleep(2)

    search = login_wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ember1135"]/input')))
    search.send_keys("hot")

    button = my_driver.find_element_by_xpath('//*[@id="nav-search-controls-wormhole"]/button')
    button.click()
    time.sleep(5)

    buttonpeople = login_wait.until(EC.visibility_of_element_located((By.XPATH, '//*[starts-with(@id, "ember")]/ul/li[1]/button')))
    buttonpeople.click()

    return my_driver


def get_people_detail(my_driver):
    my_selected_people_list = []

    my_soup = BeautifulSoup(my_driver.page_source, 'lxml')

    my_list_of_people_links = my_soup.find_all('a', class_="search-result__result-link ember-view")

    for person in my_list_of_people_links:
        my_selected_people_list.append("https://www.linkedin.com" + person['href'] + "detail/contact-info/")

    print(my_selected_people_list)
    print("total = {}".format(len(my_selected_people_list)))


get_people_detail(login_and_search())