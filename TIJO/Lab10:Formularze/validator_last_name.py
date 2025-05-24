from register_form_fields import RegisterFormFields
from validator import Validator

class LastNameValidator(Validator):
    def __init__(self, last_name):
        self.last_name = last_name

    def is_valid(self):
        return self.last_name is not None and self.last_name != ""

    def field_name(self):
        return RegisterFormFields.LAST_NAME