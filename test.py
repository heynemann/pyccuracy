from selenium import selenium
import unittest

class TestGoogle(unittest.TestCase):
    
    
    def setUp(self):
        self.selenium = selenium("localhost", \
            4444, "*firefox", "http://www.google.com/")
        self.selenium.start()
                
    def test_google(self):
        sel = self.selenium
        sel.open("http://www.google.com/")
        sel.type("q", "hello world")
        sel.click("btnG")
        sel.wait_for_page_to_load(5000)
        self.assertEqual("hello world - Pesquisa Google", sel.get_title())

    def test_google_for_something(self):
        sel = self.selenium
        sel.open("http://www.google.com/")
        sel.type("q", "Something")
        sel.click("btnG")
        sel.wait_for_page_to_load(5000)
        self.assertEqual("Something - Pesquisa Google", sel.get_title())
        
    def tearDown(self):
        self.selenium.stop()

if __name__ == "__main__":
    unittest.main()
