import unittest
import sys
import os
sys.path.insert(0,os.path.abspath(__file__+"/../../"))
from pyccuracy.page import Page

class TestPageRegisteredElements(unittest.TestCase):
        
    def test_retrieve_element_by_key_only(self):
        page = Page()
        page.register_link("Algum link", "xpath")
        page.register_element("li", "Generico", "xpath2")
        
        link = page.get_registered_element_by_key_only("Algum link")
        li = page.get_registered_element_by_key_only("Generico")
        
        self.failIf(link!="xpath", "O elemento com nome de Algum link deveria resolver para xpath mas resolveu para %s" % link)
        self.failIf(li!="xpath2", "O elemento com nome de Generico deveria resolver para xpath2 mas resolveu para %s" % li)
    
if __name__ == "__main__":
    unittest.main()
