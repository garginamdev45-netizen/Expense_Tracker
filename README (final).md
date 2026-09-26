# Personal Finance & Expense Tracker - Introduction to Problem solving and Programming Project

## 📌Overview
This is a Python based desktop application for tracking personal expenses with a GUI, designed to help users record and monitor daily spending without relying on spreadsheets or paid finance apps. The tool uses tkinter for the frontend and a local JSON file for backend storage, so all data is saved automatically and remains available across sessions without needing an internet connection.

## 📌Features
* Expense Logging: Record expenses with amount, category, date, and an optional note.
* Category Selection: Choose from predefined categories like Food, Transport, Rent, Shopping, etc., using a drop-down menu.
* Persistent Storage: Automatically saves all expenses to a local JSON file so data isn't lost when the app closes.
* Input Validation: Provides error handling for non-numeric or invalid amounts that prevents application crashes.
* Delete Entries: Remove incorrectly logged expenses directly from the list.
* Running Total: Displays the total amount spent across all recorded entries.
* User-Friendly GUI: Clean interface using Times New Roman font with a drop-down menu for categories and a scrollable list of entries.

## 📌Technologies/Tools Used
* Programming Language: Python 3.7
* GUI Framework: Tkinter
* Data Format: JSON (local file storage)
* Standard Library: os, datetime, json

## 📌Steps to Install & Run the Project
### 1. *Requirement:*
Make sure that Python is installed on your system. You can check this by running the following:
bash

    ''' python --version 3.7 '''
### 2. *Clone/Download the Repository:*
Download the project files to your local machine.
### 3. *Install Dependencies:*
This project only uses Python's standard library, so no extra installation is required.
### 4. *▶️ Run the Application:*
Go to your project directory and run the script:
 bash
      python Expense_Tracker.py
    
## 📌Instructions for Testing
Conduct the following tests to ensure that the application works as anticipated.

### 1. *Standard Entry Test:*
* Launch the app.
* In the Amount field, enter "500".
Select "Food" as the category and add a note like "Lunch".
* Click "Add Expense."

* Expected Output: The entry appears in the list below and the total updates to "Total Spent: 500.00".
### 2. *Input Validation Test:*
* Launch the application.
* Type in any string or leave the Amount field blank.

* Click "Add Expense."
* Expected Output: A warning pop-up showing "Please enter a valid numeric amount" or "Please enter an amount."
### 3. Persistence Test:
* Add a few expenses and close the application. 
* Reopen the application. 
* Expected Output: The previously added expenses should still be listed, loaded automatically from the saved expenses.json file.
### 4. Delete Entry Test:
* Select an expense from the list. 
* Click "Delete Selected." 
* Expected Output: The entry is removed from the list and the total updates accordingly.

## 📌Project structure
expense tracker
  * ├── Expense_Tracker.py
  * ├── expenses.json (created automatically on first run)
  * ├── README.md
  * ├── Report.pdf
  * └── screenrecordings

## 📌Screenshots
1.Entering the amount of expense and selecting its category from drop down
<img width="873" height="987" alt="image" src="https://github.com/user-attachments/assets/b31d25d1-3a75-4948-9bc8-f69145a4aebb" />

2.Adding the expense in the record
<img width="870" height="983" alt="image-1" src="https://github.com/user-attachments/assets/5ad6b474-b77a-420d-96ed-0518df3a16a2" />

3.If the amount entered is not numeric
<img width="1013" height="950" alt="image-2" src="https://github.com/user-attachments/assets/2ad2e373-7601-41c0-8f3e-9f1e26d25cc0" />

4.Deleting a record
<img width="872" height="970" alt="image-3" src="https://github.com/user-attachments/assets/2e1075d0-4d53-450f-bc82-4abb28e33329" />
