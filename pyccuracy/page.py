class Page(object):
    '''Class that defines a page model.'''
    
    def __init__(self, url):
        '''Initializes the page with the given url.'''
        self.url = url
        self.registered_elements = {}
        
    def get_registered_element(self, element_type, element_key):
        if not element_type in self.registered_elements: return None
        if not element_key in self.registered_elements[element_type]: return None
        return self.registered_elements[element_type, element_key]
