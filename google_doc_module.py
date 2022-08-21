from selenium.webdriver.common.by import By

class GoogleDocFiller(By):
    """
    This module helps to low in material into a linked Google Document, via Google Forms
    """
    def __init__(self,form_url,driver,address,price,link):
        super().__init__()
        self.form_url= form_url
        self.driver= driver
        self.address= address
        self.price= price
        self.link= link

    def write(self):
        for n in range(len(self.price)):
            self.driver.get(self.form_url)

            address = self.driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/textarea')
            price = self.driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link = self.driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            submit_button = self.driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

            address.send_keys(self.address[n])
            price.send_keys(self.price[n])
            link.send_keys(self.link[n])
            submit_button.click()

