from appium import  webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'Pixel'
desired_caps['app'] = ('/Users/sujithreddy/Documents/Code2Lead/kwad.apk')
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

driver =webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

element = driver.find_element_by_id("com.code2lead.kwad:id/EnterValue")
print("Is Displayed : ",element.is_displayed())
print("Is Enabled : ",element.is_enabled())
print("Is selected : ",element.is_selected())
print("Size : ",element.size)
print("Location : ",element.location)