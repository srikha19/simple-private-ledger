# 🧱 Advanced Private Blockchain Ledger System (Python + PyQt5)
## 👨‍🎓 Intern Details
- Name: Srikha kommineni
- Intern ID: CITS1430
## 📌 Project Overview
This project is a **mini blockchain-based ledger system** built using Python.  
It simulates real blockchain concepts such as:

- Proof of Work (Mining)
- SHA-256 Hashing
- Block Linking (Chain Structure)
- Tamper Detection
- Transaction Storage
- GUI-based Blockchain Explorer

It also includes a **PyQt5 desktop application** to interact with the blockchain visually.

---

## 🚀 Features

### 🔐 Blockchain Core Features
- Secure block creation
- SHA-256 cryptographic hashing
- Previous hash linking between blocks
- Proof of Work mining (difficulty-based)
- Immutable blockchain structure

### 🖥️ GUI Features (PyQt5)
- Add transactions (From → To → Amount)
- Mine new blocks with a button click
- View blockchain in table format
- Validate blockchain integrity
- Real-time updates of blockchain data

### 💾 Storage Features
- Save blockchain data to JSON file
- Load blockchain from JSON file

### 🔍 Security Features
- Tamper detection system
- Chain validation system
- Hash integrity verification

---

## 📂 Project Structure
```
simple-private-ledger/
│
├── ledger.py        # Blockchain logic (core engine)
├── gui_app.py       # PyQt5 GUI application
└── blockchain.json  # Auto-generated saved blockchain data
```


---

## 🛠️ Technologies Used

- Python 3
- hashlib (SHA-256 encryption)
- datetime module
- JSON file handling
- PyQt5 (GUI framework)

---

## ▶️ How to Run the Project

### 1. Install dependencies
```bash
pip install pyqt5
```
2. Run the application
```
python gui_app.py
``` 
## 🧪 How to Use the Application
Open the application window  

Enter transaction details:  
- From  
- To  
- Amount  

Click:  
- ⛏️ **Mine Block** → Adds a new block  

Use other buttons:  
- 📂 **Load** → Load saved blockchain  
- 💾 **Save** → Save blockchain  
- 🔍 **Validate** → Check blockchain integrity  
## 🔗 How Blockchain Works
Each block contains:
- Index  
- Timestamp  
- Transaction Data  
- Previous Hash  
- Current Hash  
- Nonce (for mining)  

🔥 **Security Principle**:  
If any block is changed, the hash breaks and the blockchain becomes invalid.
## 🧠 Learning Outcomes
- Blockchain fundamentals  
- Cryptographic hashing (SHA-256)  
- Proof of Work concept  
- Data integrity and validation  
- GUI development using PyQt5  
- File handling in Python  
## 🚀 Future Improvements
- Add SQLite database integration  
- Add multi-node blockchain network  
- Add real-time synchronization  
- Improve UI with modern dashboards  
- Add transaction search feature  
- Add blockchain visualization graph  
## 👨‍💻 Author
Student Project – Python Blockchain Simulation System  
Built for learning and internship demonstration purposes.
## ⭐ Note
This is a simulated blockchain system, not a real cryptocurrency network.  
It is designed for educational purposes to understand how blockchain works internally.
## 📸 Project Screenshots

### Main Window
![Main Window](screenshots/home.png)

### Transaction Entry
![Transaction](screenshots/transaction.png)

### Mining a Block
![Mining](screenshots/mined_block.png)

### Blockchain Validation
![Validation](screenshots/validation.png)
