import sys
import os
sys.path.insert(0,os.path.abspath(__file__+"/../../"))
from pyccuracy.page import Page

class TestCustomPage (Page):
    def __init__(self):
        super(TestCustomPage, self).__init__()
        self.url = "test_custom_page.htm"
        
