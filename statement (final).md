## 📌Program Statement
Managing personal finances is a common challenge, as many people struggle to track where their money goes on a day-to-day basis.
Without a simple recording system, small expenses often go unnoticed and add up, making it difficult to budget effectively or identify unnecessary spending.
Many existing solutions require signing up for finance apps that ask for bank access or personal financial details, which can raise privacy concerns for users who just want a simple local tracker.

## 📌Scope of the Project
This project aims to develop a Personal Finance & Expense Tracker, a client-side desktop application.
It bridges the gap between messy manual tracking (notebooks, scattered notes) and complex finance software.

The scope includes:
* Local Data Storage: Using a local JSON file to persist expense records without requiring internet access or external accounts.
* Data Processing: Logic to categorize expenses, validate input, and compute running totals.
* Resilience: The application handles a missing or empty data file gracefully and rejects invalid input before it is saved.

## 📌Target Users
* Students: Users who want to track daily spending on a limited budget.
* Working Professionals: People who want a quick way to monitor monthly expenses without complex accounting tools.
* Privacy Conscious Users: Individuals who prefer local data storage over cloud-based finance apps requiring bank access.
* General Users: People who need a fast and easy utility for everyday expense logging.

## 📌High-Level Features
* Expense Recording: Log expenses with amount, category, date, and notes.
* Smart Input Validation: A robust error-handling system that refuses to take non-numeric, empty, or negative inputs, thus preventing crashes.
* Persistent Local Storage: Expenses are saved automatically to a JSON file and reloaded the next time the app is launched.
* Modern GUI: A clean, user-friendly interface using Tkinter with Times New Roman styling, where inputs, controls, and results are clearly separated.