class ElementSelector(object):
    def button(element_name):
        return r"//input[(@name='%s' or @id='%s') and (@type='button' or @type='submit')] | //button[@name='%s' or @id='%s']" % (element_name, element_name, element_name, element_name)

    button = staticmethod(button)

    def link(element_name):
        return r"//a[(@name='%s' or @id='%s')]" % (element_name, element_name)

    link = staticmethod(link)

    def checkbox(element_name):
        return r"//input[(@name='%s' or @id='%s') and @type='checkbox']" % (element_name, element_name)		

    checkbox = staticmethod(checkbox)

    def select(element_name):
        return r"//select[@name='%s' or @id='%s']" % (element_name, element_name)		

    select = staticmethod(select)

    def textbox(element_name):
        return r"//input[(@name='%s' or @id='%s') and (@type='text' or not(@type))] | //textarea[@name='%s' or @id='%s']" % (element_name, element_name, element_name, element_name)

    textbox = staticmethod(textbox)

    def image(element_name):
        return r"//img[@name='%s' or @id='%s']" % (element_name, element_name)

    image = staticmethod(image)