
class Product:
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

    def __repr__(self):
        return f"Product({self.product_id}, {self.name}, {self.category}, {self.price}, {self.stock_quantity})"


class ProductManager:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.product_id] = product

    def edit_product(self, product_id, **kwargs):
        product = self.products.get(product_id)
        if product:
            for key, value in kwargs.items():
                setattr(product, key, value)

    def delete_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]

    def view_all_products(self):
        return list(self.products.values())
