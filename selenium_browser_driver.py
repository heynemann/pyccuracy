from selenium import *
from selenium_server import SeleniumServer
import time
import urllib

class SeleniumBrowserDriver(object):
    def __init__(self, browser = "*firefox"):
        self.__host = "localhost"
        self.__port = 4444
        self.__browser = browser
    
    def __wait_for_server_to_start(self):
        server_started = False
        while server_started == False: 
            try:
                url = "http://%s:%s/" % (self.__host, self.__port)
                request = urllib.urlopen(url)
                server_started = True
                request.close()
            except IOError, e:
                server_started = False
            time.sleep(2)

    def start(self):
        self.selenium_server = SeleniumServer()
        self.selenium_server.start()
        self.__wait_for_server_to_start()
    
    def start_test(self, url = "http://www.someurl.com"):
        self.selenium = selenium(self.__host, self.__port, self.__browser, url)
        self.selenium.start()
        
    def open(self, url):
        self.selenium.open(url)
    
    def type(self, input_selector, text):
        self.selenium.type(input_selector, text)
        
    def click_button(self, button_selector):
        self.selenium.click(button_selector)
		
	def is_button_visible(self, button_selector):
		return self.selenium.is_element_present(button_selector) and self.selenium.is_visible(button_selector)
    
    def wait_for_page(self, timeout = 20000):
        self.selenium.wait_for_page_to_load(timeout)
    
    def get_title(self):
        return self.selenium.get_title()
    
    def stop_test(self):
        self.selenium.stop()        
    
    def stop(self):
        self.selenium_server.stop()
