from register_form_fields import RegisterFormFields
from validator import Validator
from re import *


class PeselValidator(Validator):
    def __init__(self, pesel):
        self.pesel = pesel

    def is_valid(self):
        if not self.pesel or len(self.pesel) != 11:  
            return False

        wagi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]  
        suma = 0

        for i, j in zip(wagi, self.pesel[:10]):
            suma += i * int(j)  

        M = suma % 10
        cyfra_kontrolna = 0 if M == 0 else 10 - M  

        return cyfra_kontrolna == int(self.pesel[10])

    def field_name(self):
        return RegisterFormFields.PESEL