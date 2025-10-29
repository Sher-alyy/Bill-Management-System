import tkinter as tk
from tkinter import messagebox

items = []
prices = []

def add_item():
    name = entry_item.get().strip()
    price = entry_price.get().strip()

    if not name or not price:
        messagebox.showwarning("Input Error", "Please enter both item name and price.")
        return

    try:
        price = float(price)
    except ValueError:
        messagebox.showerror("Invalid Input", "Price must be a number.")
        return

    items.append(name)
    prices.append(price)

    bill_area.insert(tk.END, f"{len(items)}. {name} - ₨{price:.2f}\n")
    entry_item.delete(0, tk.END)
    entry_price.delete(0, tk.END)

def generate_bill():
    if not items:
        messagebox.showinfo("Empty Bill", "No items added yet!")
        return

    total = sum(prices)
    bill_area.insert(tk.END, f"\n-----------------------------\nTotal Amount: ₨{total:.2f}\n")
    bill_area.insert(tk.END, "-----------------------------\n")
    messagebox.showinfo("Bill Generated", f"Total Bill: ₨{total:.2f}")

def clear_bill():
    items.clear()
    prices.clear()
    bill_area.delete(1.0, tk.END)

root = tk.Tk()
root.title("Bill Management System")

window_width = 700
window_height = 800
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.resizable(True, True)
root.config(bg="#f2f2f2")

title = tk.Label(root, text="🧾 Simple Bill Management System", font=("Arial", 18, "bold"), bg="#f2f2f2", fg="#333")
title.pack(pady=20)

frame = tk.Frame(root, bg="#f2f2f2")
frame.pack(pady=10)

tk.Label(frame, text="Item Name:", bg="#f2f2f2", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=8, sticky="e")
entry_item = tk.Entry(frame, width=30, font=("Arial", 12))
entry_item.grid(row=0, column=1, padx=10, pady=8)

tk.Label(frame, text="Item Price (₨):", bg="#f2f2f2", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=8, sticky="e")
entry_price = tk.Entry(frame, width=30, font=("Arial", 12))
entry_price.grid(row=1, column=1, padx=10, pady=8)

btn_frame = tk.Frame(root, bg="#f2f2f2")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add Item", command=add_item, bg="#4CAF50", fg="white", width=15, font=("Arial", 11, "bold")).grid(row=0, column=0, padx=10, pady=5)
tk.Button(btn_frame, text="Generate Bill", command=generate_bill, bg="#2196F3", fg="white", width=15, font=("Arial", 11, "bold")).grid(row=0, column=1, padx=10, pady=5)
tk.Button(btn_frame, text="Clear", command=clear_bill, bg="#f44336", fg="white", width=15, font=("Arial", 11, "bold")).grid(row=0, column=2, padx=10, pady=5)

bill_area = tk.Text(root, height=18, width=70, font=("Courier New", 11))
bill_area.pack(padx=10, pady=15)

root.mainloop()


