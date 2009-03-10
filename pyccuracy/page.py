class Page(object):
    '''Class that defines a page model.'''
    
    Button = "button"
    Checkbox = "checkbox"
    Div = "div"
    Image = "image"
    Link = "link"
    Page = "page"
    Select = "select"
    Textbox = "textbox"
    
    def __init__(self):
        '''Initializes the page with the given url.'''
        self.registered_elements = {}
    
    def get_registered_element(self, element_type, element_key):
        if not element_type in self.registered_elements: return None
        if not element_key in self.registered_elements[element_type]: return None
        return self.registered_elements[element_type][element_key]
        
    def register_button(self, button_key, button_locator):
        self.register_element(Page.Button, button_key, button_locator)
        
    def register_element(self, element_type, element_key, element_locator):
        if not element_type in self.registered_elements: self.registered_elements[element_type] = {}
        if not element_key in self.registered_elements[element_type]: self.registered_elements[element_type] = {}
        self.registered_elements[element_type][element_key] = element_locator
