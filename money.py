# pylint: disable=unidiomatic-typecheck,unnecessary-pass


class DifferentCurrencyError(Exception):
    pass


class Currency:
    """
    Represents a currency. Does not contain any exchange rate info.
    """

    def __init__(self, name, code, symbol=None, digits=2):
        """
        Parameters:
        - name -- the English name of the currency
        - code -- the ISO 4217 three-letter code for the currency
        - symbol - optional symbol used to designate currency
        - digits -- number of significant digits used
        """
        self.name = name
        self.code = code
        self.symbol = symbol
        self.digits = digits

    def __str__(self):
        """
        Should return the currency code, or code with symbol in parentheses.
        """
        if self.symbol != None:
            return f"{self.code} ({self.symbol})"
        else:
            return f"{self.code}"

    def __eq__(self, other):
        """
        All fields must be equal to for the objects to be equal.
        """
        return (type(self) == type(other) and self.name == other.name and
                self.code == other.code and self.symbol == other.symbol and
                self.digits == other.digits)


class Money:
    """
    Represents an amount of money. Requires an amount and a currency.
    """

    def __init__(self, amount, currency):
        """
        Parameters:
        - amount -- quantity of currency
        - currency -- type of currency
        """
        self.amount = amount
        self.currency = currency
        pass

    def __str__(self):
        """
        Should use the currency symbol if available, else use the code.
        Use the currency digits to determine number of digits to show.
        """
        sig_digits = self.currency.digits
        if self.currency.symbol != None:
            return f"{self.currency.symbol}{self.amount:.{sig_digits}f}"
        else:
            return f"{self.currency.code} {self.amount:.{sig_digits}f}"

    def __repr__(self):
        return f"<Money {str(self)}>"

    def __eq__(self, other):
        """
        All fields must be equal to for the objects to be equal.
        """

        return (type(self) == type(other) and self.amount == other.amount and
                self.currency == other.currency)

    def __add__(self, other):
        """
        Add two money objects of the same currency. If they have different
        currencies, raise a DifferentCurrencyError.
        """
        if self.currency == other.currency:
            return Money(self.amount + other.amount, self.currency)
        else:
            raise DifferentCurrencyError

    def __sub__(self, other):
        """
        Subtract two money objects of the same currency. If they have different
        currencies, raise a DifferentCurrencyError.
        """
        if self.currency == other.currency:
            return Money(self.amount - other.amount, self.currency)
        else:
            raise DifferentCurrencyError

    def __mul__(self, other):
        """
        Multiply a money object by a number to get a new money object.
        """
        return Money(self.amount*other, self.currency)

    def __truediv__(self, other):
        """
        Divide a money object by a number to get a new money object.
        """

        return Money(self.amount/other, self.currency)