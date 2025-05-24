from register_form_fields import RegisterFormFields
from validator import Validator

class FirstNameValidator(Validator):
    def __init__(self, first_name):
        self.first_name = first_name

    def is_valid(self):
        return self.first_name is not None and self.first_name != ""

    def field_name(self):
        return RegisterFormFields.FIRST_NAME