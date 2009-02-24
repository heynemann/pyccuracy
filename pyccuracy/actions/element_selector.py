class ElementSelector(object):
    @staticmethod
    def button(element_name):
        return r"//input[(@name='%s' or @id='%s') and (@type='button' or @type='submit')] | //button[@name='%s' or @id='%s']" % (element_name, element_name, element_name, element_name)

    @staticmethod
    def link(element_name):
        return r"//a[(@name='%s' or @id='%s')]" % (element_name, element_name)

    @staticmethod
    def checkbox(element_name):
        return r"//input[(@name='%s' or @id='%s') and @type='checkbox']" % (element_name, element_name)		

    @staticmethod
    def select(element_name):
        return r"//select[@name='%s' or @id='%s']" % (element_name, element_name)		

    @staticmethod
    def textbox(element_name):
        return r"//input[(@name='%s' or @id='%s') and (@type='text' or not(@type))] | //textarea[@name='%s' or @id='%s']" % (element_name, element_name, element_name, element_name)

    @staticmethod
    def image(element_name):
        return r"//img[@name='%s' or @id='%s']" % (element_name, element_name)