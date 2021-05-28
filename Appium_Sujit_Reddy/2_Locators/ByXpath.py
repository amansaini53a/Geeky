import time

from appium import  webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'Pixel'
desired_caps['app'] = ('/Users/sujithreddy/Documents/Code2Lead/kwad.apk')
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

driver =webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

#ele_xapth = driver.find_element_by_xpath('//android.widget.Button[@content-desc="Btn1"]') - Using Xpath_and Content-Des
#ele_xapth = driver.find_element_by_xpath('//android.widget.Button[@resource-id="com.code2lead.kwad:id/EnterValue"]')  - Using Xpath_and id
#ele_xapth = driver.find_element_by_xpath('//android.widget.Button[2]')  - Using Xpath_and index
#ele_xapth = driver.find_element_by_xpath('//android.widget.Button[@text="ScrollView"]')  - Using Xpath_and text
ele_xapth = driver.find_element_by_xpath('//android.widget.Button[@resource-id="com.code2lead.kwad:id/EnterValue"]')
ele_xapth.click()

driver.find_element_by_xpath('//android.widget.EditText').send_keys("Code2Lead") # - Using Xpath_and className

time.sleep(2000)

driver.quit()

