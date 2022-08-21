##DESCRIPTION
##the following script is designed to scrape several websites for housing rental prices and then to compile it into a spreadsheet for our usage.

##IMPORTS
    # External modules
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

    # python files
import rental_requirements
import computer_details
    # internal modules
import google_doc_module

# selenium rightmove/zillow webscraper

url = 'https://www.rightmove.co.uk'
driver = webdriver.Chrome(executable_path=computer_details.chrome_driver_path)
driver.get(url)
searchBar = driver.find_element(By.CLASS_NAME,"ksc_inputText")
searchBar.send_keys(rental_requirements.location)

    # Sale or rent decision - change sale_rent_choice value
sale_rent_choice="rent"
j=1
if sale_rent_choice == "rent" :
    j+=1
sale_or_rent_xpath = f'//*[@id="_3OuiRnbltQyS534SB4ivLV"]/div/div/div/button[{j}]'
button=driver.find_element(By.XPATH,sale_or_rent_xpath)
button.click()

    # Filling in form
for i in rental_requirements.dictionary:
    element = driver.find_element(By.XPATH, f'//*[@id="{rental_requirements.dictionary[i][0]}"]')
    select = Select(element)
    select.select_by_value(rental_requirements.dictionary[i][1])

    # Enter search
button = driver.find_element(By.XPATH, '//*[@id="submit"]')
button.click()

    # Storing all search results

price = driver.find_elements(By.CLASS_NAME, "propertyCard-priceValue")
prices =[]
for x in price:
    prices.append(x.text)

address = driver.find_elements(By.CSS_SELECTOR, "address")
addresses =[]
for x in address:
    addresses.append(x.text)

url_link = driver.find_elements(By.CSS_SELECTOR, ".propertyCard-link")
url_links=[]
for x in url_link:
    url_links.append(x.get_attribute('href'))


# Create Spreadsheet using Google Form
google_link ="https://docs.google.com/forms/d/e/1FAIpQLSfZHd_UE9ZlSpqWb7ZT84UBaBeHg5L3TDK30sbIQwyWq9O1rw/viewform?usp=sf_link"
googler=google_doc_module.GoogleDocFiller(
    form_url=google_link,
    driver=driver,
    address=addresses,
    price=prices,
    link=url_links
)
googler.write()

driver.close()

