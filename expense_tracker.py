from pymongo import MongoClient
from urllib.parse import quote_plus

# Replace with your actual username and password
username = "UshaNandhini"
password = "Naveen2003"  # Ensure any special characters are encoded
encoded_password = quote_plus(password)

# Connection string with encoded password
connection_string = f"mongodb+srv://{username}:{encoded_password}@expensetracker.xx28n.mongodb.net/expensetracker?retryWrites=true&w=majority"

try:
    client = MongoClient(connection_string)
    db = client['expensetracker']
    collection = db['expensecollection']

    # Retrieve and print one document to test the connection
    document = collection.find_one()
    print("Connected successfully. Sample document:", document)

except Exception as e:
    print("Error connecting to MongoDB:", e)

import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
from bson.objectid import ObjectId

# Function to add expense
def add_expense():
    try:
        amount = float(amount_entry.get())
        category = category_entry.get()
        date = date_entry.get() if date_entry.get() else datetime.now().strftime("%Y-%m-%d")

        expense = {
            'amount': amount,
            'category': category,
            'date': date
        }

        collection.insert_one(expense)
        messagebox.showinfo("Success", "Expense added successfully!")
        clear_entries()
        display_expenses()
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid amount.")

# Function to clear input fields
def clear_entries():
    amount_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)
    global selected_expense_id
    selected_expense_id = None  # Reset selected ID

# Function to display expenses
def display_expenses():
    for row in expense_listbox.get_children():
        expense_listbox.delete(row)

    for expense in collection.find():
        expense_listbox.insert('', 'end', iid=str(expense['_id']), values=(expense['amount'], expense['category'], expense['date']))

# Function to select expense for editing
def select_expense(event):
    global selected_expense_id
    selected_item = expense_listbox.selection()
    if selected_item:
        item = expense_listbox.item(selected_item)
        values = item['values']
        amount_entry.delete(0, tk.END)
        amount_entry.insert(0, values[0])
        category_entry.delete(0, tk.END)
        category_entry.insert(0, values[1])
        date_entry.delete(0, tk.END)
        date_entry.insert(0, values[2])
        selected_expense_id = selected_item[0]  # Save the selected item's ID

# Function to update expense
def update_expense():
    global selected_expense_id
    if selected_expense_id:
        try:
            amount = float(amount_entry.get())
            category = category_entry.get()
            date = date_entry.get() if date_entry.get() else datetime.now().strftime("%Y-%m-%d")

            # Update the expense in the database
            collection.update_one({'_id': ObjectId(selected_expense_id)}, {'$set': {
                'amount': amount,
                'category': category,
                'date': date
            }})
            messagebox.showinfo("Success", "Expense updated successfully!")
            clear_entries()
            display_expenses()
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid amount.")
    else:
        messagebox.showerror("Error", "Select an expense to update.")

# Function to delete expense
def delete_expense():
    global selected_expense_id
    if selected_expense_id:
        collection.delete_one({'_id': ObjectId(selected_expense_id)})
        messagebox.showinfo("Success", "Expense deleted successfully!")
        clear_entries()
        display_expenses()
    else:
        messagebox.showerror("Error", "Select an expense to delete.")

# Create main window
root = tk.Tk()
root.title("Personal Expense Tracker")

# Create input fields
tk.Label(root, text="Amount:").grid(row=0, column=0)
amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1)

tk.Label(root, text="Category:").grid(row=1, column=0)
category_entry = tk.Entry(root)
category_entry.grid(row=1, column=1)

tk.Label(root, text="Date (YYYY-MM-DD):").grid(row=2, column=0)
date_entry = tk.Entry(root)
date_entry.grid(row=2, column=1)

# Add expense button
add_button = tk.Button(root, text="Add Expense", command=add_expense)
add_button.grid(row=3, column=0, columnspan=2)

# Update expense button
update_button = tk.Button(root, text="Update Expense", command=update_expense)
update_button.grid(row=4, column=0, columnspan=2)

# Delete expense button
delete_button = tk.Button(root, text="Delete Expense", command=delete_expense)
delete_button.grid(row=5, column=0, columnspan=2)

# Display expenses
tk.Label(root, text="Expenses:").grid(row=6, column=0, columnspan=2)
expense_listbox = ttk.Treeview(root, columns=("Amount", "Category", "Date"), show="headings")
expense_listbox.heading("Amount", text="Amount")
expense_listbox.heading("Category", text="Category")
expense_listbox.heading("Date", text="Date")
expense_listbox.grid(row=7, column=0, columnspan=2)

# Bind selection event to the listbox
expense_listbox.bind("<<TreeviewSelect>>", select_expense)

# Load existing expenses
display_expenses()

# Run the application
root.mainloop()

