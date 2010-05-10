from pyccuracy import ActionBase

class DoesNothingAction(ActionBase):
    regex = "^does nothing$"
    
    def execute(self):
        pass