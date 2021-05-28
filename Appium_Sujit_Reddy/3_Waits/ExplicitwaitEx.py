from appium import  webdriver
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'Pixel'
desired_caps['app'] = ('/Users/sujithreddy/Documents/Code2Lead/kwad.apk')
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

driver =webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

#list of Selenium Exceptions
#https://www.selenium.dev/selenium/docs/api/py/common/selenium.common.exceptions.html
wait = WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,ElementNotSelectableException,NoSuchElementException])

#ele = wait.until(lambda  x: x.find_element_by_id("com.code2lead.kwad:id/EnterValue"))
#ele.click()

#ele = wait.until(lambda  x: x.find_element_by_class_name("android.widget.EditText")).send_keys("Code2Lead")
#ele = wait.until(lambda  x: x.find_element_by_android_uiautomator('UiSelector().description("Btn3")'))
ele = wait.until(lambda  x: x.find_element_by_android_uiautomator('text("ENTER SOME VALUE")'))
ele.click()

time.sleep(4000)
driver.quit()

