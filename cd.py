import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time, unittest
from selenium.webdriver.support.ui import Select



class Test_CreateDonor(unittest.TestCase):

	def setUp(self):
		'''Переход на страницу и логин'''
		self.driver = webdriver.Firefox()
		self.driver.get('http://10.32.200.127')
		self.driver.find_element_by_id('Login').send_keys('admin')
		self.driver.find_element_by_id('Password').send_keys('77@dm1n')
		submit = self.driver.find_element_by_class_name('submit')
		submit.click()
		WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".donor-logo")))
		# добавить assert

	def test_create(self):
		'''Проверка первой страницы pop-up'а'''
		driver = self.driver
		wait = WebDriverWait(driver, 20)
		driver.get('http://10.32.200.127/donor')
		wait.until(EC.presence_of_element_located((By.XPATH, ".//*[@id='newdonor']"))) #element_to_be_clickable
		newdonor = driver.find_element_by_xpath(".//*[@id='newdonor']")
		newdonor.click()
		wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[21]/div[2]/form/div/div[2]/div[1]/input"))) #or element_to_be_clickable
		last = driver.find_element_by_xpath('//*[@id="LastName"]') #//*[@id="LastName"]
		first = driver.find_element_by_id('FirstName')
		last.send_keys('Мэттерз')
		first.send_keys('Автотестовый')
		driver.find_element_by_id('BirthDate').send_keys('11021990')
		driver.find_element_by_id('Gender').click()
		driver.find_element_by_id('IdentityDocument_Serie').send_keys('0956980716')
		driver.find_element_by_id('IdentityDocument_IssueDate').send_keys('09032010')
		driver.find_element_by_id('NextStep').click()

		'''Проверка второй страницы pop-up'а'''
		wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='regFiasAddress_Region']")))
		# добавить assert
		assert driver.find_element_by_xpath('//*[@id="regFiasAddress_Street"]').is_enabled() == False #get_attribute('disabled') == True
		driver.find_element_by_id('regFiasAddress_Region').send_keys('Мос')
		wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[74]/div/div[2]/ul/li[1]")))
		select_region = driver.find_element_by_xpath('/html/body/div[74]/div/div[2]/ul/li[1]')
		select_region.click()
		driver.find_element_by_xpath('//*[@id="regFiasAddress_Street"]').send_keys('Строит')
		wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[80]/div/div[2]/ul/li[2]")))
		select_street = driver.find_element_by_xpath('/html/body/div[120]/div/div[2]/ul/li[2]')
		select_street.click()

		
	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()
'''

ЗАПРОС №1 - Дописать класс.
Класс должен выполнять без ошибок основную функциональность: заходить на сайт, логиниться, создавать донора.
Только после этого можно переходить к работе над Запросом №2.

ЗАПРОС №2 - Добавить проверки.
1)выделить контрольные точки, в которых тестировщик бы анализировал результат выполнения тест-кейса;
2) добавить в эти контрольные точки assertions.

ЗАПРОС №3 - Реализовать приём тестовых данных из отдельного модуля классом Test_CreateDonor.
1) необходимо продумать логику реализации приёма этим классом тестовых данных - как он будет принимать данные для теста;
2) необходимо продумать, каким будет файл с данными для теста (возможно, в формате json, либо тот же .py), каким образом он будет отдавать данные классу;
3) придумать тестовые данные и запустить тест.

'''