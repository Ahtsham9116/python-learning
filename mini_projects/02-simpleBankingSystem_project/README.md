<div align="center">

# 🏦 Banking System

### A menu-driven banking management app built with core Python (OOP)

![Python](https://img.shields.io/badge/Python-3.6%2B-3776AB?style=flat&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat)
![Platform](https://img.shields.io/badge/Platform-CLI-lightgrey?style=flat)

A terminal-based banking system that lets you create accounts, deposit and withdraw funds, and track transaction history — built to practice object-oriented Python.

</div>

---

## 📖 Overview

**Banking System** is a terminal-based application written in pure Python, with no external dependencies. It models a simple bank using two classes — `BankAccount` and `Bank` — and lets you manage multiple accounts through a numbered menu: creating accounts, depositing and withdrawing funds, and reviewing transaction history.

I built it as a mini-project to practice object-oriented programming — designing classes that manage their own state (`BankAccount`), composing them inside a manager class (`Bank`), and wrapping the whole thing in a validated, menu-driven input loop.

> **Note:** All data is stored in memory only. Accounts and transactions reset every time the program exits — there's no file or database persistence yet (see [Future Improvements](#-future-improvements)).

---

## ✨ Features

- 🏦 Create new bank accounts with a unique account number
- 💰 Deposit funds, with validation that rejects zero/negative amounts
- 💸 Withdraw funds, with insufficient-funds and invalid-amount protection
- 📊 Check an account's current balance
- 📜 View an account's full transaction history (numbered, with running balance)
- 🧾 Display an account's details (number, holder, balance)
- 👥 View all accounts at once, with a running total account count
- 🔁 Menu-driven loop — perform multiple operations without restarting
- ✅ Input validation on every text and numeric entry
- 🚪 Clean exit option from the main menu

---

## 🛠️ Technologies Used

- **Python 3** — the entire project is written in standard Python, using classes, dictionaries, lists, and tuples to model accounts and transactions

No third-party packages, `pip install` requirements, or even standard-library imports — the project runs with a plain Python installation.

---

## 📁 Project Structure

```
banking-system/
│
├── banking_system.py      # Main application file — BankAccount, Bank, and menu logic
└── README.md               # Project documentation (this file)
```

> **Note:** Adjust the path above once this folder is placed inside your repository's mini-projects directory.

---

## ⚙️ Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/Ahtsham9116/python-learning.git
cd python-learning
```

Then navigate into this project's folder (adjust the path to match where you place it, e.g. inside your mini-projects directory).

No additional installation steps are required — the project uses only Python's standard library.

**Requirements:**
- Python 3.6 or higher (required for f-string formatting used in the code)

---

## ▶️ How to Run

Run the script directly from your terminal:

```bash
python banking_system.py
```

On some systems (macOS/Linux), you may need to use `python3` instead:

```bash
python3 banking_system.py
```

---

## 🧮 Example Usage

When you run the program, you'll see a numbered menu of operations:

```
===================================
    Banking System Menu    
===================================
1. Create account
2. Deposit
3. Withdraw
4. Check balance
5. View transaction history
6. Display account info
7. View all accounts
8. Exit
Enter your choice: 1
Enter account number: 101
Enter account holder name: Ahtsham
Account created for Ahtsham with account number 101.
```

Depositing into that account:

```
Enter your choice: 2
Enter account number: 101
Enter deposit amount: 500
Deposited: $500.0. New balance: $500.0.
```

The menu keeps reappearing after every action, so you can perform multiple operations across multiple accounts in a single session.

---

## 🛡️ Error Handling

The program validates input at every step and avoids crashing on common mistakes:

| Scenario | Behavior |
|---|---|
| Invalid menu choice (e.g. letters, out-of-range numbers) | Displays an error message and re-shows the menu |
| Empty account number or holder name | Re-prompts until a non-empty value is entered |
| Non-numeric deposit/withdrawal amount | Re-prompts until a valid number is entered |
| Zero or negative deposit/withdrawal amount | Blocked with a clear error message |
| Withdrawal amount greater than balance | Blocked with an "insufficient funds" message |
| Operating on a non-existent account number | Displays "Account not found" |

This is handled through two reusable input functions — `get_non_empty_input()` and `get_valid_amount()` — which wrap user input in a loop, so invalid entries never crash the program.

---

## 📚 What I Learned

This project was a chance to practice structuring a program around objects rather than just functions and globals:

- Designing a class (`BankAccount`) that owns and protects its own state
- Composing objects inside a manager class (`Bank`) that looks accounts up by key
- Using a dictionary as a simple in-memory "database" of accounts
- Recording transactions as a list of tuples and formatting them for display
- Writing reusable input-validation helpers instead of repeating `try`/`except` logic in every menu branch
- Structuring a growing `if`/`elif` menu loop so each branch stays short and readable

---

## 🚀 Future Improvements

- 💾 Persist accounts and transactions to a file or database (currently everything resets on exit)
- 🔐 PIN or password protection before sensitive actions
- 🔁 Fund transfers between two accounts
- 📈 Interest calculation or multiple account types (savings vs. checking)
- 🧪 Automated unit tests for account operations and edge cases
- 🖥️ A graphical interface using Tkinter

---

## 👤 Author

**Muhammad Ahtsham Javed**

- GitHub: [@Ahtsham9116](https://github.com/Ahtsham9116)
- LinkedIn: [m-ahtsham-javed](https://www.linkedin.com/in/m-ahtsham-javed)
- Repository: [python-learning](https://github.com/Ahtsham9116/python-learning)

Feel free to explore the code, fork the repository, or reach out with suggestions.

---

## 📄 License

This project is licensed under the **MIT License**.

---

<div align="center">

⭐ If you found this project useful or interesting, consider giving it a star on GitHub!

</div>
