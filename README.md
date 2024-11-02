A GUI-based expense tracker application developed using Python, Tkinter, and MongoDB. This tool provides an easy interface for users to record, update, and manage their daily expenses.

**Table of Contents**
-> Features
-> Technologies Used
-> Installation
-> Usage
-> File Structure

**Features**
Add Expenses: Enter expense details such as amount, category, and date.
Update Expenses: Edit previously added expenses.
Delete Expenses: Remove any expense from the list.
View Expenses: Displays all expenses in a tabular view, allowing easy tracking.

**Technologies Used**
Python: Main language for the application.
Tkinter: GUI library for creating the user interface.
MongoDB: Database to store expense records.
pymongo: Python driver for MongoDB.

**Installation**
Prerequisites
MongoDB Atlas: Set up a free MongoDB Atlas cluster and configure it to allow connections.
Python 3.x: Ensure Python is installed on your machine.
pymongo: Install the pymongo package

**Usage**
Adding an Expense
Enter the amount, category, and date (optional).
Click "Add Expense" to save it to the database.
Updating an Expense
Select an expense from the list, make changes to the fields, and click "Update Expense".
Deleting an Expense
Select an expense and click "Delete Expense" to remove it.
Viewing Expenses
The Treeview table shows all expenses by amount, category, and date.

**File Structure**
expense_tracker.py: The main application script containing all functions and UI components.
README.md: Documentation and instructions for setting up and running the application.

