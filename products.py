import tkinter as tk
from tkinter import messagebox

# Dummy product data for each category
products = {
    "Electronics": ["Laptop", "Smartphone", "Headphones"],
    "Fashion": ["Shirt", "Jeans", "Shoes"],
    "Home Appliances": ["Refrigerator", "Microwave", "Washing Machine"],
    "Books": ["Novel", "Comics", "Science Fiction"]
}

# Function to handle category button click
def category_clicked(category):
    product_window = tk.Toplevel(root)
    product_window.title(f"{category} Products")
    product_window.geometry("300x200")
    
    label = tk.Label(product_window, text=f"Products in {category}", font=("Arial", 14))
    label.pack(pady=10)
    
    for product in products[category]:
        product_label = tk.Label(product_window, text=product, font=("Arial", 12))
        product_label.pack(pady=5)

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