from register_form_fields import RegisterFormFields
from validator import Validator
from re import *


class PasswordValidator(Validator):
    def __init__(self, password):
        self.password = password

    def is_valid(self):

        regex = r"^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+=-]).{4,}$"
        pattern = compile(regex)
        matcher = pattern.match(self.password)

        return self.password is not None and len(self.password) >= 4 and bool(matcher)

    def field_name(self):
        return RegisterFormFields.PASSWORD