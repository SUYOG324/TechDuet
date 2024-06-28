import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Flipkart Login")
root.geometry("300x200")

# Function to handle login
def handle_login():
    username = username_entry.get()
    password = password_entry.get()
    
    # Dummy validation logic (replace with actual validation)
    if username == "flipkart_user" and password == "flipkart_password":
        messagebox.showinfo("Login Success", "Welcome to Flipkart!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

# Create and place the widgets
username_label = tk.Label(root, text="Username:")
username_label.pack(pady=(20, 0))

username_entry = tk.Entry(root)
username_entry.pack(pady=(0, 10))

password_label = tk.Label(root, text="Password:")
password_label.pack(pady=(0, 0))

password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=(0, 10))

login_button = tk.Button(root, text="Login", command=handle_login)
login_button.pack(pady=(10, 10))

# Run the application
root.mainloop()