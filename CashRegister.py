class CashRegister:
    def __init__(self, cash=0.00):
        self.cash = cash

    def add(self, money):
        self.cash += money

    def __str__(self):
        return "Cash: ${:,.2f}".format(self.cash)