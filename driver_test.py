from selenium import webdriver

achecker = "https://achecker.achecks.ca/checker/index.php"
portugueschecker = "https://accessmonitor.acessibilidade.gov.pt/"

address = input("Enter an address: ")
if not address.startswith("https://www."):
    address = "https://www." + address
options = webdriver.ChromeOptions()
# options.add_argument('headless')
options.add_argument('--window-size=1920,1080')
driver = webdriver.Chrome(options=options)

driver.get(achecker)
driver.find_element_by_id("checkuri").send_keys(address)
driver.find_element_by_id("validate_uri").click()

# print(driver.find_element_by_id("AC_errors").text)

driver.get(portugueschecker)
driver.find_element_by_xpath('//button[@lang="en"]').click()
driver.find_element_by_id("url").send_keys(address)
driver.find_element_by_name("url_validate").submit()
