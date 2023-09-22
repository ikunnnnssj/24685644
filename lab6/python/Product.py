class Product:
    def __init__(self, name, stock, price):
        self.name = name
        self.stock = stock
        self.price = price

    def get_name(self):
        return self.name

    def is_empty(self):
        return self.stock == 0

    def has(self, n):
        return self.stock >= n

    def sell(self, n):
        self.stock -= n
        return self.price * n

    def restock(self, n):
        self.stock += n

    def __str__(self):
        return "{} - {} at ${:,.2f}".format(self.name, self.stock, self.price)
