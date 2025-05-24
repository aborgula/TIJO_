class InsufficientFundsException(Exception):
    pass

class InvalidPinException(Exception):
    pass

class InvalidPinException(Exception):
    pass

class ATM:

    def __init__(self, pin: int = 1234, saldo: float = 0.0):
        self.pin = pin
        self.saldo = saldo

    def check_balance(self, pin: int) -> float:

        if pin != self.pin:
            raise ValueError("nieprawidlowy pin")
        else:
            return self.saldo

    def deposit(self, pin: int, amount: float) -> float:

        if pin!= self.pin:
            raise ValueError("niepoprawny pin")
        else:
            self.saldo += amount
            return self.saldo

    def withdraw(self, pin: int, amount: float) -> float:
        """
        WypĹaca Ĺrodki z konta uĹźytkownika.

        :param pin: PIN uĹźytkownika.
        :param amount: Kwota do wypĹacenia.
        :return: Aktualne saldo po wypĹacie.
        :raises InsufficientFundsException: JeĹli saldo jest niewystarczajÄce.
        :raises InvalidPinException: JeĹli podany PIN jest nieprawidĹowy.
        """
        if(pin != self.pin):
            raise InvalidPinException("niepoprawny pin")
        elif(self.saldo < amount):
            raise InsufficientFundsException("niewystarczajace srodki")
        else:
            self.saldo -= amount
            return self.saldo

