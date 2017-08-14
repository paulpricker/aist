# -*- coding: utf-8 -*-
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

	@classmethod
	def setUpClass(cls):

		'''Переход на страницу и логин'''

		cls.driver = webdriver.Firefox()
		cls.driver.maximize_window()
		cls.driver.get('http://10.32.200.127')
		cls.driver.find_element_by_id('Login').send_keys('admin')
		cls.driver.find_element_by_id('Password').send_keys('77@dm1n')
		submit = cls.driver.find_element_by_class_name('submit')
		submit.click()
		cls.wait = WebDriverWait(cls.driver, 20)
		cls.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".donor-logo")))

	def test_create_first_page(self):

		'''Проверка первой страницы pop-up'а'''

		self.driver.get('http://10.32.200.127/donor')
		self.wait.until(EC.presence_of_element_located((By.XPATH, ".//*[@id='newdonor']")))
		newdonor = self.driver.find_element_by_xpath(".//*[@id='newdonor']")
		newdonor.click()
		newdonor.click()
		self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="LastName"]')))
		'''if driver.find_element_by_xpath('//*[@id="LastName"]').is_displayed() != True:
			newdonor.click()'''
		#Добавить TimeOut Exception
		ln = "Машинный"
		fn = "Яша"
		mn = "Афанасьевич"
		global full_name 
		full_name = ln + ' ' + fn + ' ' + mn
		last = self.driver.find_element_by_xpath('//*[@id="LastName"]')
		first = self.driver.find_element_by_id('FirstName')
		middle = self.driver.find_element_by_id('MiddleName')
		save_button = self.driver.find_element_by_id('NextStep')
		save_button.click()
		self.wait.until(EC.presence_of_element_located((By.XPATH, ".//*[@id='newdonor-popup-form']/div/div[1]/ul")))
		self.validation_messages = ["Поле 'Фамилия' обязательно для заполнения", 
		"Поле 'Имя' обязательно для заполнения", 
		"Поле 'Дата рождения' обязательно для заполнения", 
		"Поле 'Пол' обязательно для заполнения", 
		"Поле 'Серия' обязательно для заполнения", 
		"Поле 'Номер' обязательно для заполнения"]
		self.validations = self.driver.find_element_by_xpath(".//*[@id='newdonor-popup-form']/div/div[1]/ul")
		self.messages = self.validations.find_elements_by_tag_name("li")
		self.count = 0
		for message in self.messages:
			self.assertEqual(message.text, self.validation_messages[self.count])
			self.count = self.count + 1
		
		last.send_keys(ln)
		first.send_keys(fn)
		middle.send_keys(mn)
		self.driver.find_element_by_id('BirthDate').send_keys('11021990')
		self.driver.find_element_by_xpath('//*[@id="step1"]/div[4]/label[2]').click()
		self.driver.find_element_by_id('IdentityDocument_Serie').send_keys('0956980716')
		self.driver.find_element_by_id('IdentityDocument_IssueDate').send_keys('09032010')
		save_button.click()

		'''Обработать все предупреждающие и запрещающие проверки в отдельном тест-кейсе'''
		
		'''Проверка валидации выбранного пола'''
		self.wait.until(EC.presence_of_element_located((By.ID, "confirm-popup_wnd_title")))
		sex_popup = self.driver.find_element_by_id('confirm-popup')
		self.assertEqual(sex_popup.text, "Пол донора не соответствует отчеству. Вы уверены?")
		self.driver.find_element_by_xpath('//*[@id="confirm-popup-no"]').click()
		self.driver.find_element_by_id('NextStep').click()

		'''Проверка второй страницы pop-up'а'''

	def test_create_second_page(self):
		self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='regFiasAddress_Region']")))
		self.assertEqual(self.driver.find_element_by_xpath('//*[@id="step2"]/div[1]').text, "КОНТАКТНАЯ ИНФОРМАЦИЯ")
		assert self.driver.find_element_by_xpath('//*[@id="regFiasAddress_Street"]').is_enabled() == False #get_attribute('disabled') == True
		save_button = self.driver.find_element_by_xpath('//*[@id="save-newdonor"]')
		#assert save_button.click()
		self.driver.find_element_by_id('regFiasAddress_Region').send_keys('Мос')
		self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="regFiasAddress_Region_listbox"]/li[1]')))
		select_region = self.driver.find_element_by_xpath('//*[@id="regFiasAddress_Region_listbox"]/li[1]')
		select_region.click()
		time.sleep(2)
		#assert save_button.click()
		select_street = self.driver.find_element_by_xpath('//*[@id="regFiasAddress_Street"]')
		select_street.click()
		select_street.send_keys('Строит')
		self.wait.until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="regFiasAddress_Street_listbox"]/li[2]'), 'Строителей ул'))
		#assert save_button.click()
		self.driver.find_element_by_xpath('//*[@id="regFiasAddress_Street_listbox"]/li[2]').click()
		time.sleep(2)
		self.driver.find_element_by_xpath('//*[@id="regFiasAddress_House"]').send_keys('13')
		time.sleep(2)
		save_button.click()
		save_button.click() #потом добавить клик по пустому полю вместо второго клика на кнопку
		time.sleep(6)

		'''Проверка сохранения'''
		
		self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="SimpleSearchText"]')))
		search_minicard = self.driver.find_element_by_xpath('//*[@id="donor-details"]/div[1]/div[5]/div[2]/a').text
		search_grid = self.driver.find_element_by_xpath('/html/body/div[4]/div[4]/div/div[1]/div/div[2]/div[1]/table/tbody/tr[1]/td[2]').text
		self.assertEqual(search_minicard, full_name)
		self.assertEqual(search_grid, full_name)

	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()

if __name__ == '__main__':
	unittest.main()
'''
TESTCASE: https://aj.srvdev.ru/browse/AIST-6128 .

TICKET #1 - Дописать класс.
Класс должен выполнять без ошибок основную функциональность: заходить на сайт, логиниться, создавать донора.
Только после этого можно переходить к работе над Запросом №2.
RESOLUTION: Done V

TICKET №2 - Добавить проверки (Is blocked by TICKET #1).
1) выделить контрольные точки, в которых тестировщик бы анализировал результат выполнения тест-кейса;
2) добавить в эти контрольные точки assertions.
RESOLUTION: In progress...

TICKET #3 - Реализовать приём тестовых данных из отдельного модуля классом Test_CreateDonor (Is blocked by TICKET #2).
1) необходимо продумать логику реализации приёма этим классом тестовых данных - как он будет принимать данные для теста;
2) необходимо продумать, каким будет файл с данными для теста (возможно, в формате json, либо тот же .py), каким образом он будет отдавать данные классу;
3) придумать тестовые данные и запустить тест.

TICKET #4 - Добившись стабильной работы теста, свести всё к PageObject (Is blocked by TICKET #3).
'''