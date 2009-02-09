from selenium import *
import subprocess
import os
from sys import platform
import time
import threading

class selenium_server(threading.Thread):
	out_file = None
	
	def run(self, log_file="out.txt"):
		self.out_file = open(log_file, mode='a')
		self.current_process = subprocess.Popen("java -jar ./lib/selenium-server/selenium-server.jar", stdout=self.out_file)
			
	def stop(self):
		self.out_file.close()
		print platform
		if platform == 'win32': 
			import ctypes
			ctypes.windll.kernel32.TerminateProcess(int(self.current_process._handle), -1)
		else:
			os.kill(self.current_process.pid, signal.SIGKILL)

class selenium_browser_driver:
	def start(self):
		self.selenium_server = selenium_server()
		self.selenium_server.start()
	
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
