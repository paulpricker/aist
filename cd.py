import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time, unittest



class Test_CreateDonor(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.get('http://10.32.200.127')
		self.driver.find_element_by_id('Login').send_keys('admin')
		self.driver.find_element_by_id('Password').send_keys('77@dm1n')
		submit = self.driver.find_element_by_class_name('submit')
		submit.click()
		WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".donor-logo")))

	def test_create(self):
		driver = self.driver
		wait = WebDriverWait(driver, 10)
		driver.get('http://10.32.200.127/donor')
		newdonor = driver.find_element_by_xpath(".//*[@id='newdonor']")
		last = driver.find_element_by_xpath('//*[@id="LastName"]')
		first = driver.find_element_by_id('FirstName')
		wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='newdonor']")))
		newdonor.click()
		#Добавить assert
		wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='LastName']"))) #or element_to_be_clickable
		last.send_keys('Уколов')
		first.send_keys('Павел')
		driver.find_element_by_id('BirthDate').send_keys('11021990')
		driver.find_element_by_id('Gender').click()
		driver.find_element_by_id('IdentityDocument_Serie').send_keys('0956980716')
		driver.find_element_by_id('IdentityDocument_IssueDate').send_keys('09032010')
		driver.find_element_by_id('NextStep').click()
		#Добавить assert

	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()