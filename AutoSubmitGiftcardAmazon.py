from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as ec
import time


print("Made By : ")
print("---------------------------------------------------")
print("  _____      _                 _  _    ___  _  _   ")
print(" / ____|    | |               | || |  / _ \| || |  ")
print("| |    _   _| |__   ___ _ __  | || |_| | | | || |_ ")
print("| |   | | | | '_ \ / _ \ '__| |__   _| | | |__   _|")
print("| |___| |_| | |_) |  __/ |       | | | |_| |  | |  ")
print(" \_____\__, |_.__/ \___|_|       |_|  \___/   |_|  ")
print("        __/ |                                      ")
print("       |___/                                       ")
print("---------------------------------------------------")
print("\n\n")
print("[-]If amazon ask for verification/OTP, you have to do it manually[-]")
print("[-]This program doesn't work if the redeem page use captcha[-]\n")
print("please input your information : ")

email = input("Email >> ")
password = input("Pass >> ")
gc_number = input("Number of giftcard >> ")
directory = input("Code file directory >> ")


options = webdriver.ChromeOptions()
options.add_argument("--incognito")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver.get("https://www.amazon.com/ap/signin?clientContext=131-4641921-7497613&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgc%2Fredeem%2F&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=amzn_gcfront_v2_us&openid.mode=checkid_setup&marketPlaceId=ATVPDKIKX0DER&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=amzn_gcfront_v2_us&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.pape.max_auth_age=3600&siteState=clientContext%3D144-1807701-9645427%2CsourceUrl%3Dhttps%253A%252F%252Fwww.amazon.com%252Fgc%252Fredeem%252F%2Csignature%3DduV3UfJbYbHeREFcPDmzxQt6fpIj3D")
usr = driver.find_element_by_id("ap_email")
usr.clear()
usr.send_keys(email)
pwd = driver.find_element_by_id("ap_password")
pwd.clear()
pwd.send_keys(password)
pwd.submit()

element = WebDriverWait(driver, 100).until(ec.presence_of_element_located((By.ID, "gc-redemption-input")))

for i in range(gc_number):
	driver.get("https://www.amazon.com/gc/redeem/")
	elem = driver.find_element_by_id("gc-redemption-input")
	elem.clear()
	code_file = open(directory, "r")
	code = code_file.readlines()
	code_file.close()
	elem.send_keys(code[i])
	elem.submit()
