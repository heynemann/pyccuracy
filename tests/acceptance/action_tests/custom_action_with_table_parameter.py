#
from pyccuracy.actions import ActionBase
from pyccuracy.errors import *

class RegisterUsersAction(ActionBase):
    regex = r'^(And )?I have the following registered users:$'

    def execute(self, context, table):
        user = table[0]
        assert(user['username']=='admin')
        assert(user['email']=='a@dd.cc')
        assert(user['password']=='aidimin')
        
class ProductsSetupAction(ActionBase):
    regex = r'^(And )?I have the following products:$'

    def execute(self, context, table):
        apple = table[0]
        assert(apple['name']=='Apple')
        assert(apple['price']=='1.65')

        banana = table[1]
        assert(banana['name']=='Banana')
        assert(banana['price']=='0.99')
        
