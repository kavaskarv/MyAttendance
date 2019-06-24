from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

path = 'C:\\Users\\sysadmin\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe' # change path as needed
# driver = webdriver.Chrome(executable_path = path)
url = 'file:///D:/webtop_automation/webtop.html'
# driver.get(url)
# username= driver.find_element_by_xpath('//*[@id="IDToken1"]').send_keys("username")
# pwd = driver.find_element_by_xpath('//*[@id="IDToken2 "]').send_keys("password")
# upload_field = driver.find_element_by_name('Login.Submit').click()
# alert_obj = driver.switch_to.alert
# time.sleep(3)
# alert_obj.accept()


# prefs = {
#     "profile.default_content_setting_values.plugins": 1,
#     "profile.content_settings.plugin_whitelist.adobe-flash-player": 1,
#     "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player": 1,
#     "PluginsAllowedForUrls": "ENTER THE URL HERE"
# }

prefs = {
    "profile.default_content_setting_values.plugins": 1,
    "profile.content_settings.plugin_whitelist.adobe-flash-player": 1,
    "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player": 1,
    "PluginsAllowedForUrls": "http:// www.google.com"

    
}

chrome_options = Options()
chrome_options.add_argument("--user-data-dir=C:\\Users\\sysadmin\\AppData\\Local\\Google\\Chrome\\User Data\\Default") # change to profile path
chrome_options.add_argument('--profile-directory=profile 1')
# chrome_options.add_argument('dom.ipc.plugins.enabled.libflashplayer.so')
# chrome_options.add_argument("profile.managed_plugins_allowed_for_urls");
chrome_options.add_experimental_option("prefs",prefs)

browser = webdriver.Chrome(executable_path=path,chrome_options=chrome_options)
print(dir(chrome_options)) # change the executable_path too
browser.get(url)
print("clicked")



# pyautogui.click(100, 600)
# pyauto.gui

