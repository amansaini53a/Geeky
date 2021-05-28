from appium import  webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'Pixel'
desired_caps['app'] = ('/Users/sujithreddy/Documents/Code2Lead/kwad.apk')
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

driver =webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

ele_id = driver.find_element_by_id("com.code2lead.kwad:id/EnterValue")
ele_id.click()

ele_classname = driver.find_element_by_class_name("android.widget.EditText").send_keys("Code2Lead")