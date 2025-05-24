
from re import *
from validator import Validator
from register_form_fields import RegisterFormFields

class LoginValidator(Validator):
    def __init__(self, login):
        self.login = login
        self.LOGIN_MIN_LENGTH = 4

    def is_valid(self):
        return self.login is not None and self.login.strip != "" and len(self.login.strip()) >= self.LOGIN_MIN_LENGTH

    def field_name(self):
        return RegisterFormFields.LOGIN