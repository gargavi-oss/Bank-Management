# 🏦 Bank Management System (Python)

A **menu-driven Bank Management System** built using **Python**, **Object-Oriented Programming**, and **JSON file handling**.
This project simulates basic banking operations such as account creation, deposit, withdrawal, updating details, and account deletion, with data persistence.

---

## 🚀 Features

* Create a new bank account
* Deposit money (with limits)
* Withdraw money (balance validation)
* View account details
* Update account information
* Delete bank account
* Data stored permanently using a JSON file
* PIN-based account authentication

---

## 🛠️ Technologies Used

* **Python 3**
* **JSON** (for database storage)
* **OOP concepts**
* `pathlib`, `random`, `string` modules

---

## 📂 Project Structure

```
Bank-Management-System/
│
├── data.json          # Stores bank account data
├── bank.py            # Main Python program
└── README.md          # Project documentation
```

---

## ▶️ How to Run the Project

1. Make sure Python is installed:

   ```bash
   python --version
   ```

2. Clone the repository:

   ```bash
   git clone https://github.com/your-username/Bank-Management-System.git
   ```

3. Navigate to the project folder:

   ```bash
   cd Bank-Management-System
   ```

4. Run the program:

   ```bash
   python bank.py
   ```

---

## 🧾 Menu Options

```
Press 1 → Create Account
Press 2 → Deposit Money
Press 3 → Withdraw Money
Press 4 → Check Account Details
Press 5 → Update Account Details
Press 6 → Delete Account
Any other key → Exit
```

---

## 🔐 Account Rules

* Minimum age: **18 years**
* PIN must be **4 digits**
* Deposit limit: **₹1 – ₹10,000**
* Withdrawal cannot exceed available balance
* Account access requires **Account Number + PIN**

---

## 📌 Notes

* Account numbers are auto-generated and randomized
* All data is stored in `data.json`
* Double underscore (`__`) methods are used for internal functionality
* This project is intended for **learning and practice purposes**

---

## 🧑‍💻 Author

**Avi**
Python & Programming Enthusiast

---

## ⭐ Future Improvements

* Input validation with exception handling
* Unique account number enforcement
* Transaction history
* PIN hashing for better security
* GUI or Web version

---

## 📜 License

This project is open-source and free to use for educational purposes.
Feel free to fork and improve it ⭐
