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
        if hasattr(self, "register"): self.register()

    def get_registered_element(self, element_type, element_key):
        if not element_type in self.registered_elements: return None
        if not element_key in self.registered_elements[element_type]: return None
        return self.registered_elements[element_type][element_key]

    def register_button(self, button_key, button_locator):
        self.register_element(Page.Button, button_key, button_locator)

    def register_checkbox(self, checkbox_key, checkbox_locator):
        self.register_element(Page.Checkbox, checkbox_key, checkbox_locator)

    def register_div(self, div_key, div_locator):
        self.register_element(Page.Div, div_key, div_locator)

    def register_image(self, image_key, image_locator):
        self.register_element(Page.Image, image_key, image_locator)

    def register_link(self, link_key, link_locator):
        self.register_element(Page.Link, link_key, link_locator)

    def register_select(self, select_key, select_locator):
        self.register_element(Page.Select, select_key, select_locator)

    def register_textbox(self, textbox_key, textbox_locator):
        self.register_element(Page.Textbox, textbox_key, textbox_locator)

    def register_element(self, element_type, element_key, element_locator):
        if not element_type in self.registered_elements: self.registered_elements[element_type] = {}
        self.registered_elements[element_type][element_key] = element_locator
