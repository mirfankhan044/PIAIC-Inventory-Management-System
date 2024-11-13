
from auth import AuthService
from product import Product, ProductManager
from inventory import Inventory

def main():
    auth_service = AuthService()
    product_manager = ProductManager()
    inventory = Inventory()

    try:
        username = input("Enter username: ")
        password = input("Enter password: ")
        user = auth_service.authenticate(username, password)

        if user.role == "Admin":
            print("Welcome, Admin!")
            while True:
                action = input("Choose action: add/edit/delete/view/exit: ").lower()
                if action == "add":
                    # Logic for adding a product
                    pass
                elif action == "edit":
                    # Logic for editing a product
                    pass
                elif action == "delete":
                    # Logic for deleting a product
                    pass
                elif action == "view":
                    products = product_manager.view_all_products()
                    for product in products:
                        print(product)
                elif action == "exit":
                    break
        else:
            print("Welcome, User!")
            # Allow viewing products only
            products = product_manager.view_all_products()
            for product in products:
                print(product)

    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
