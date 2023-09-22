from CashRegister import CashRegister
from Product import Product

class Store:
    def __init__(self):
        self.cash_register = CashRegister(0.00)
        self.products = [
            Product("Whiteboard Marker", 85, 1.50),
            Product("Whiteboard Eraser", 45, 5.00),
            Product("Black Pen", 100, 1.50),
            Product("Red Pen", 100, 1.50),
            Product("Blue Pen", 100, 1.50)
        ]

    def menu(self):
        while True:
            choice = input("Choice (s/r/v/c/p/x): ").lower()
            if choice == 's':
                self.sell()
            elif choice == 'r':
                self.restock()
            elif choice == 'v':
                self.view_stock()
            elif choice == 'c':
                self.view_cash()
            elif choice == 'p':
                self.prune_products()
            elif choice == 'x':
                print("Done")
                break
            else:
                self.help()

    def sell(self):
        product_name = input("Name: ")
        product = self.find_product(product_name)
        if product:
            print(f"Selling {product.get_name()}")
            stock_qty = int(input("Number: "))
            if product.has(stock_qty):
                self.cash_register.add(product.sell(stock_qty))
            else:
                print("Not enough stock")
        else:
            matching_products = self.find_products(product_name)
            if len(matching_products) > 1:
                print("Multiple products match:")
                for prod in matching_products:
                    print(prod)
            else:
                print("No such product")

    def find_product(self, name):
        for product in self.products:
            if product.get_name().lower() == name.lower():
                return product
        return None

    def find_products(self, part_name):
        return [product for product in self.products if part_name.lower() in product.get_name().lower()]

    def restock(self):
        product_name = input("Name: ")
        matching_product = self.find_product(product_name)
        if matching_product:
            print(f"Restocking {matching_product.get_name()}")
            stock_qty = int(input("Number: "))
            matching_product.restock(stock_qty)
        else:
            print("Adding new product")
            product_number = int(input("Number: "))
            product_price = float(input("Price: $"))
            self.products.append(Product(product_name, product_number, product_price))

    def view_stock(self):
        for product in self.products:
            print(product)

    def view_cash(self):
        print(self.cash_register)

    def prune_products(self):
        self.products = [product for product in self.products if not product.is_empty()]

    def help(self):
        print("Menu options")
        print("s = sell")
        print("r = restock")
        print("v = view stock")
        print("c = view cash")
        print("p = prune products")
        print("x = exit")

if __name__ == "__main__":
    store = Store()
    store.menu()