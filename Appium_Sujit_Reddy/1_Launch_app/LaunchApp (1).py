from appium import webdriver

# Part 1 "Desired Capabilities"
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'Pixel3XL'
desired_caps['app'] = ('/Users/sujithreddy/Documents/Code2Lead/Appium_Demo_APK/Android_Demo_App.apk')
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

# Part 2 "WebDriver object"
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

# Part 3 "Action on the App"

ele_id = driver.find_element_by_id("com.code2lead.kwad:id/EnterValue")
ele_id.click()





"""
Part-1 : 
1. Create a Dictionary variable "desired_caps = {}" and assign Appium Desired Capabilities to it, 
In the form of Key and value pair

Note : For More information on Dictionary data type please go through the Python Basics videos.

Part-2 :
1. Create the object for WebDriver class "driver" to access all the methods in WebDriver class and 
pass the localhost and Port number in the form of url to connect to the server and "desired_caps" dictionary variable 
as well to establish a connection to the device.

Part-3 :
1. By using created WebDriver object "driver" now we can access all the methods to perform on App.
and assign it to a variable "ele_id" to perform futher action on it.

"""
