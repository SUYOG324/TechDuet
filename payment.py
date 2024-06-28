import tkinter as tk
from tkinter import messagebox

# Dummy product data for each category
products = {
    "Electronics": ["Laptop", "Smartphone", "Headphones"],
    "Fashion": ["Shirt", "Jeans", "Shoes"],
    "Home Appliances": ["Refrigerator", "Microwave", "Washing Machine"],
    "Books": ["Novel", "Comics", "Science Fiction"]
}

# Function to handle final order confirmation with shipping address and payment method
def finalize_order(product, address, payment_method):
    if address and payment_method:
        messagebox.showinfo(
            "Order Confirmed",
            f"Your order for {product} has been confirmed!\n\n"
            f"Shipping Address:\n{address}\n\n"
            f"Payment Method: {payment_method}"
        )
    else:
        messagebox.showerror("Error", "Please enter a valid shipping address and select a payment method.")

# Function to confirm order and collect shipping address and payment method
def confirm_order(product):
    address_window = tk.Toplevel(root)
    address_window.title("Shipping Address")
    address_window.geometry("400x400")
    
    tk.Label(address_window, text="Enter your shipping address:", font=("Arial", 14)).pack(pady=10)
    
    address_entry = tk.Text(address_window, height=5, width=40)
    address_entry.pack(pady=10)
    
    tk.Label(address_window, text="Select payment method:", font=("Arial", 14)).pack(pady=10)
    
    payment_method_var = tk.StringVar(value="Credit Card")
    payment_methods = ["Credit Card", "Debit Card", "Net Banking", "Cash on Delivery"]
    
    for method in payment_methods:
        tk.Radiobutton(address_window, text=method, variable=payment_method_var, value=method).pack(anchor=tk.W)
    
    tk.Button(address_window, text="Confirm Order", 
              command=lambda: finalize_order(product, address_entry.get("1.0", tk.END).strip(), payment_method_var.get())).pack(pady=10)

# Function to display product details and order button
def product_detail(product):
    detail_window = tk.Toplevel(root)
    detail_window.title(f"{product} Details")
    detail_window.geometry("300x200")
    
    label = tk.Label(detail_window, text=f"Details of {product}", font=("Arial", 14))
    label.pack(pady=10)
    
    order_button = tk.Button(detail_window, text="Order", command=lambda: confirm_order(product))
    order_button.pack(pady=20)

# Function to display products in a selected category
def category_clicked(category):
    product_window = tk.Toplevel(root)
    product_window.title(f"{category} Products")
    product_window.geometry("300x200")
    
    label = tk.Label(product_window, text=f"Products in {category}", font=("Arial", 14))
    label.pack(pady=10)
    
    for product in products[category]:
        product_button = tk.Button(product_window, text=product, font=("Arial", 12), command=lambda p=product: product_detail(p))
        product_button.pack(pady=5)

# Create the main window
root = tk.Tk()
root.title("Flipkart Home")
root.geometry("300x300")

# Create and place the category buttons
categories = ["Electronics", "Fashion", "Home Appliances", "Books"]
for category in categories:
    button = tk.Button(root, text=category, width=20, height=2, command=lambda c=category: category_clicked(c))
    button.pack(pady=10)

# Run the application
root.mainloop()