import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service('C:/Users/Виктор/PycharmProjects/chromedriver_win32(1)/chromedriver.exe')
driver: WebDriver = webdriver.Chrome(service=s)
driver.get("https://qa.neapro.site")
driver.set_window_size(1024, 600)
driver.minimize_window()
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(1) input").send_keys("ptiza92@mail.ru")
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(2) input").send_keys("spring-09")
driver.find_element(By.CSS_SELECTOR, ".btn").click()
time.sleep(30)
# Открыть форму блока Паспорт
driver.find_element(By.CSS_SELECTOR, ".form:nth-child(2) .document-tile:nth-child(1) > .document-name").click()
driver.find_element(By.ID, "surname").clear()
driver.find_element(By.ID, "surname").send_keys("Скандинавский")
driver.find_element(By.ID, "name").clear()
driver.find_element(By.ID, "name").send_keys("Тестировщик")

driver.find_element(By.ID, "patronymic").clear()
driver.find_element(By.ID, "patronymic").send_keys("Багович")