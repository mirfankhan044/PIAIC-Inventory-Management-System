
from product import ProductManager

class Inventory:
    def __init__(self):
        self.product_manager = ProductManager()

    def check_stock(self, product_id):
        product = self.product_manager.products.get(product_id)
        if product and product.stock_quantity < 10:
            print("Stock is low. Please consider restocking.")
