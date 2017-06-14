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
		wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='newdonor']")))
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
		#Добавить assert
		#http://software-testing.ru/forum/index.php?/topic/28840-problemy-s-select-vypadaiuschij-spisok/
		wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='regFiasAddress_Region']")))
		assert driver.find_element_by_xpath('//*[@id="regFiasAddress_Street"]').is_enabled() == False #get_attribute('disabled') == True
		driver.find_element_by_id('regFiasAddress_Region').send_keys('Мос')
		wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[74]/div/div[2]/ul/li[1]")))
		select_region = driver.find_element_by_xpath('/html/body/div[74]/div/div[2]/ul/li[1]')
		select_region.click()
		
	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()