import sys
import os
sys.path.insert(0,os.path.abspath(__file__+"/../../"))
from pyccuracy.page import Page

class TestCustomPage (Page):
    def register(self):
        self.url = "test_custom_page.htm"
        self.register_button("My Button", "//div[@class='something']/button[@class='button']")
        self.register_checkbox("My Custom Checkbox", "//div[@class='something']/div[@name='other']/input[@type='checkbox' and @value='1']")
        self.register_div("Some Div", "//div[@class='something']/div[@name='other']")
        self.register_image("Some Image", "//img[@src='bogus_src']")
        self.register_link("My Link", "//a[@href='bogus_href']")
        self.register_select("Some Select", "//select[@alt='Some Select']")
        self.register_textbox("Some Textbox", "//div[contains(@class,'some')]//input[@type='text' and @class='textbox' and @name='some_textbox']")
