from selenium import webdriver

USERNAME = 'maruf'
PASSWORD = '123456'

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://beta.breakingmars.com/login')

user_input = driver.find_element_by_class_name('ant-input')
user_input.send_keys(USERNAME)

password_input = driver.find_element_by_class_name('ant-input-affix-wrapper ant-input-password ant-input')
password_input.send_keys(PASSWORD)

login_button = driver.find_element_by_class_name('ant-btn ant-btn-primary ant-btn-block')
login_button.click()
# driver.manage(). Timeouts().implicitywait(10,Timeout,SECONDS);