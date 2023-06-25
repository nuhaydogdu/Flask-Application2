from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

    
class MyPublications:
    def __init__(self):
        # Method implementation goes here
        # You can access instance attributes and perform other operations
        #self.my_browser = None  # Initialize my_browser attribute
        pass
    
    def update_my_list(self):
        my_options = webdriver.ChromeOptions()
        my_service = Service(ChromeDriverManager().install())
        self.my_browser = webdriver.Chrome(service=my_service, options=my_options)  # Assign my_browser instance to the attribute
        my_link = "http://boracanbula.com.tr/"
        self.my_browser.get(my_link)  # Use self.my_browser to access the my_browser instance
        time.sleep(5)
        my_page_source = self.my_browser.page_source  # Use self.my_browser to access the my_browser instance
        my_soup = BeautifulSoup(my_page_source, 'html.parser')
        my_second_span = my_soup.select('div#articles ul li span:nth-of-type(2)')
        my_author_span = my_soup.select('div#articles ul li span:nth-of-type(1)')
        my_object = {
            "author_span": my_author_span,
            "second_span": my_second_span
        }
        self.my_browser.close()
        return my_object