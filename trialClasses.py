import tkinter as tk

class ProductEntryWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Product Entry")

        self.create_widgets()

    def create_widgets(self):
        # Create widgets for adding a new product
        self.product_name_label = tk.Label(self.root, text="Product Name:")
        self.product_name_entry = tk.Entry(self.root)

        self.product_price_label = tk.Label(self.root, text="Price:")
        self.product_price_entry = tk.Entry(self.root)

        self.product_quantity_label = tk.Label(self.root, text="Quantity:")
        self.product_quantity_entry = tk.Entry(self.root)

        self.add_button = tk.Button(self.root, text="Add Product", command=self.add_product)

        # Pack widgets
        self.product_name_label.pack()
        self.product_name_entry.pack()
        self.product_price_label.pack()
        self.product_price_entry.pack()
        self.product_quantity_label.pack()
        self.product_quantity_entry.pack()
        self.add_button.pack()

    def add_product(self):
        # Retrieve product information from entry fields
        product_name = self.product_name_entry.get()
        product_price = float(self.product_price_entry.get())
        product_quantity = int(self.product_quantity_entry.get())

        # Add product to the inventory (simulate database update)
        # You can implement the actual database logic here
        print(f"Added Product: {product_name}, Price: {product_price}, Quantity: {product_quantity}")

class ProductUpdateWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Product Update")

        self.create_widgets()

    def create_widgets(self):
        # Create widgets for updating existing products
        self.select_product_label = tk.Label(self.root, text="Select Product:")
        self.product_options = ["Product 1", "Product 2", "Product 3"]  # Replace with actual product list
        self.selected_product = tk.StringVar(self.root)
        self.product_dropdown = tk.OptionMenu(self.root, self.selected_product, *self.product_options)

        self.update_price_label = tk.Label(self.root, text="New Price:")
        self.update_price_entry = tk.Entry(self.root)

        self.update_quantity_label = tk.Label(self.root, text="New Quantity:")
        self.update_quantity_entry = tk.Entry(self.root)

        self.update_button = tk.Button(self.root, text="Update Product", command=self.update_product)

        # Pack widgets
        self.select_product_label.pack()
        self.product_dropdown.pack()
        self.update_price_label.pack()
        self.update_price_entry.pack()
        self.update_quantity_label.pack()
        self.update_quantity_entry.pack()
        self.update_button.pack()

    def update_product(self):
        # Retrieve selected product and updated information
        selected_product = self.selected_product.get()
        new_price = float(self.update_price_entry.get())
        new_quantity = int(self.update_quantity_entry.get())

        # Update the selected product in the inventory (simulate database update)
        # You can implement the actual database logic here
        print(f"Updated Product: {selected_product}, New Price: {new_price}, New Quantity: {new_quantity}")

class InventoryManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")

        # Create instances of windows
        self.product_entry_window = ProductEntryWindow(self.root)
        self.product_update_window = ProductUpdateWindow(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryManagementApp(root)
    root.mainloop()