from selenium import *
from selenium_server import SeleniumServer
import time

class SeleniumBrowserDriver(object):
    def start(self):
        self.selenium_server = SeleniumServer()
        self.selenium_server.start()
        time.sleep(2) # hackish: used to work on Mac OS
    
    def start_test(self, url = "http://www.someurl.com"):
        self.selenium = selenium("localhost", 4444, "*firefox", url)
        self.selenium.start()
        
    def open(self, url):
        self.selenium.open(url)
    
    def type(self, input_selector, text):
        self.selenium.type(input_selector, text)
        
    def click_button(self, button_selector):
        self.selenium.click(button_selector)
    
    def wait_for_page(self, timeout = 20000):
        self.selenium.wait_for_page_to_load(timeout)
    
    def get_title(self):
        return self.selenium.get_title()
    
    def stop_test(self):
        self.selenium.stop()        
    
    def stop(self):
        self.selenium_server.stop()
