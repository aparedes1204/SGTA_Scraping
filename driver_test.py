from selenium import webdriver

achecker = "https://achecker.achecks.ca/checker/index.php"
portugueschecker = "https://accessmonitor.acessibilidade.gov.pt/"

address = input("Enter an address: ")
if not address.startswith("https://www."):
    address = "https://www." + address
options = webdriver.ChromeOptions()
#options.add_argument('headless')
options.add_argument('window-size=1200x600')
driver = webdriver.Chrome(options=options)

driver.get(achecker)
driver.find_element_by_id("checkuri").send_keys(address)
driver.find_element_by_id("validate_uri").click()

#print(driver.find_element_by_id("AC_errors").text)

driver.get(portugueschecker)
f = open("home.html", "w")
for b in driver.find_elements_by_xpath("//button"):
    f.write(b.text)
f.close()
driver.find_element_by_id("url").send_keys(address)
driver.find_element_by_name("url_validate").submit()
