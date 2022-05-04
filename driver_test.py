from copy import copy
from selenium import webdriver
from selenium.webdriver.common.by import By 

achecker = "https://achecker.achecks.ca/checker/index.php"
portugueschecker = "https://accessmonitor.acessibilidade.gov.pt/"

address="google.com"
# address = input("Enter an address: ")
if not address.startswith("https://"):
    address = "https://" + address
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('--window-size=1920,1080')
driver = webdriver.Chrome(options=options)

driver.get(achecker)
driver.find_element(by=By.ID,value="checkuri").send_keys(address)
driver.find_element(by=By.ID,value="validate_uri").click()

errors = driver.find_element(by=By.ID,value="AC_errors").find_elements(by=By.TAG_NAME,value="table")

errors_AC ={}
for i in errors:
    if i.find_element(by=By.XPATH, value="./preceding::h4[1]").text != "":
        if i.find_element(by=By.XPATH, value="./preceding::h4[1]").text.split(' ',2)[2] in errors_AC:
            errors_AC[i.find_element(by=By.XPATH, value="./preceding::h4[1]").text.split(' ',2)[2]].append(i.find_element(by=By.TAG_NAME, value="em").text)
        else:
            errors_AC[i.find_element(by=By.XPATH, value="./preceding::h4[1]").text.split(' ',2)[2]] = [i.find_element(by=By.TAG_NAME, value="em").text]

driver.find_element(by=By.ID,value="AC_menu_likely_problems").click()
likely_problems = driver.find_element(by=By.ID,value="AC_likely_problems").find_elements(by=By.TAG_NAME,value="table")

likely_problems_AC = {}
for i in likely_problems:
    if i.find_element(by=By.XPATH, value="./preceding::h4[1]").text != "":
        if i.find_element(by=By.XPATH, value="./preceding::h4[1]").text.split(' ',2)[2] in likely_problems_AC:
            likely_problems_AC[i.find_element(by=By.XPATH, value="./preceding::h4[1]").text.split(' ',2)[2]].append(i.find_element(by=By.TAG_NAME, value="em").text)
        else:
            likely_problems_AC[i.find_element(by=By.XPATH, value="./preceding::h4[1]").text.split(' ',2)[2]] = [i.find_element(by=By.TAG_NAME, value="em").text]

driver.find_element(by=By.ID,value="AC_menu_potential_problems").click()
potential_problems = driver.find_element(by=By.ID,value="AC_potential_problems").find_elements(by=By.TAG_NAME,value="table")

potential_problems_AC = {}
for i in potential_problems:
    if i.find_element(by=By.XPATH, value="./preceding::h4[1]").text != "":
        if i.find_element(by=By.XPATH, value="./preceding::h4[1]").text.split(' ',2)[2] in potential_problems_AC:
            potential_problems_AC[i.find_element(by=By.XPATH, value="./preceding::h4[1]").text.split(' ',2)[2]].append(i.find_element(by=By.TAG_NAME, value="em").text)
        else:
            potential_problems_AC[i.find_element(by=By.XPATH, value="./preceding::h4[1]").text.split(' ',2)[2]] = [i.find_element(by=By.TAG_NAME, value="em").text]

print(errors_AC)
print(likely_problems_AC)
print(potential_problems_AC)


driver.get(portugueschecker)
driver.find_element_by_xpath('//button[@lang="en"]').click()
driver.find_element_by_id("url").send_keys(address)
driver.find_element_by_name("url_validate").submit()


