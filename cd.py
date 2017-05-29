import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class Set_Up_For_127(object):
	driver = webdriver.Firefox()
	driver.get('http://10.32.200.127')
	driver.find_element_by_id('Login').send_keys('admin')
	driver.find_element_by_id('Password').send_keys('77@dm1n')
	submit = driver.find_element_by_class_name('submit')
	submit.click()
	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".donor-logo")))


class Create(Set_Up_For_127):
	def __init__(self, lastname, firstname):
		self.lastname = lastname
		self.firstname = firstname
		Set_Up_For_127.driver.get('http://10.32.200.127/donor')
		#time.sleep(5)
		elementnewd = WebDriverWait(Set_Up_For_127.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='newdonor']")))
		elementnewd.click()
		#WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "LastName")))
		LastName = WebDriverWait(Set_Up_For_127.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='LastName']")))
		LastName.send_keys(self.lastname)
		FirstName = Set_Up_For_127.driver.find_element_by_id('FirstName')
		FirstName.send_keys(self.firstname)
		Set_Up_For_127.driver.find_element_by_id('BirthDate').send_keys('11021990')
		Set_Up_For_127.driver.find_element_by_id('Gender').click()
		Set_Up_For_127.driver.find_element_by_id('IdentityDocument_Serie').send_keys('0956980716')
		Set_Up_For_127.driver.find_element_by_id('IdentityDocument_IssueDate').send_keys('09032010')
		Set_Up_For_127.driver.find_element_by_id('NextStep').click()

	#def create_donor_second_page():
		#time.sleep(5)
		#region = driver.find_element_by_id('regFiasAddress_Region')
		#region.send_keys('Москва')
	"""
	Выяснить, почему обваливается ошибка при ожидании средствами селениума. WebDriverWait не исполняется. ELEMENT IS NOT VISIBLE; XPATH STR IS NOT CALLABLE.

	http://automated-testing.info/t/otlichie-find-element-ot-presence-of-element-located/4250/11 - здесь
	http://stackoverflow.com/questions/27927964/selenium-element-not-visible-exception
	http://selenium-python.readthedocs.io/waits.html
	https://iamalittletester.wordpress.com/2016/05/11/selenium-how-to-wait-for-an-element-to-be-displayed-not-displayed/
	https://blog.mozilla.org/webqa/2012/07/12/how-to-webdriverwait/

	"""
