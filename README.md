# LandChain — Blockchain-Based Land Record Management System

A Python-based mini project that demonstrates how blockchain technology can help maintain a tamper-evident history of land registrations and ownership transfers.

## 📌 Project Overview

**LandChain** is a web-based land record management prototype developed using Python and Flask. It applies core blockchain concepts, including SHA-256 hashing, linked blocks, and persistent JSON storage, to record property registrations and ownership transfers.

The application provides a web dashboard where users can register land records, transfer ownership, view ownership history, and verify blockchain integrity.

This project is designed for learning and academic demonstration. It is not an official land registry or a production-ready blockchain network.

## ✨ Features

- **Land Registration:** Register properties with a unique land ID, location, area, and owner's name.
- **Ownership Transfer:** Record ownership changes in the blockchain ledger.
- **Ownership History:** View recorded registration and transfer events for a property.
- **SHA-256 Hashing:** Generate a cryptographic hash for each block.
- **Block Linking:** Link each block to the previous block using its hash.
- **Persistent Storage:** Save blockchain records in a JSON file.
- **Integrity Verification:** Check block hashes and links for unauthorized modifications.
- **Tampering Demonstration:** Test whether changes to stored block data are detected.
- **Web Dashboard:** Manage and inspect records through a Flask-based interface.

## 🛠️ Technologies Used

- Python 3
- Flask
- SHA-256
- JSON
- HTML and CSS
- Visual Studio Code

## 📂 Project Structure

```text
Land-Record-Blockchain/
├── app.py
├── blockchain.py
├── blockchain_data.json
├── requirements.txt
├── test_blockchain.py
├── test_tampering.py
└── templates/
    ├── index.html
    ├── history.html
    └── verify.html
```

## ⚙️ Installation and Setup

### Prerequisites

- Python 3 installed
- Visual Studio Code
- A web browser

### Step 1: Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Land-Record-Blockchain
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

Alternatively, download the repository ZIP file and open the extracted folder in VS Code.

### Step 2: Create a virtual environment

```bash
python -m venv .venv
```

### Step 3: Activate the virtual environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can use the appropriate activation command for your terminal or run the virtual environment's Python executable directly.

### Step 4: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Run the application

```bash
python app.py
```

Open the following address in your browser:

http://127.0.0.1:5000

Keep the terminal running while using the application.

## 🔗 How It Works

1. **Genesis Block:** The blockchain starts with an initial block.
2. **Land Registration:** Registering a property creates a new block containing its details.
3. **Hash Generation:** The system calculates a SHA-256 hash from each block's data.
4. **Block Linking:** Each new block stores the hash of the preceding block.
5. **Ownership Transfer:** A transfer is recorded as a new block rather than overwriting the earlier event.
6. **History Reconstruction:** The application uses ledger events to display a property's ownership history.
7. **Integrity Verification:** The system recalculates block hashes and checks previous-hash links to detect modifications.

## 🧪 Testing

The project includes Python scripts for demonstrating basic blockchain behavior and tampering detection.

Run the basic blockchain test:

```bash
python test_blockchain.py
```

Run the tampering demonstration:

```bash
python test_tampering.py
```

The tampering test modifies stored block data without updating its hash and checks whether the integrity verification detects the change.

**Note:** Check that the test scripts use separate test data files so they do not unintentionally modify your application's main `blockchain_data.json`.

## 🔐 Security and Limitations

LandChain is an educational prototype and has several limitations:

- It uses local JSON storage rather than a distributed blockchain network.
- Ownership transfers currently rely on matching an owner's name; this does not prove the person's identity.
- Hash linking can reveal changes to block data, but someone who can rewrite the entire chain and recalculate all hashes may evade these checks.
- The project does not implement distributed consensus, digital signatures, or production-grade access controls.
- Flask's development server and debug mode are not intended for production deployment.

The system should not be used to store real legal land records or establish legal ownership.

## 🚀 Future Enhancements

- User authentication and role-based access control
- Cryptographic digital signatures for ownership authorization
- Search and filtering for property records
- Document hash verification
- Database integration
- Automated unit tests
- Distributed blockchain architecture
- Improved logging and security controls

## 🎓 Learning Outcomes

Through this project, I explored:

- Blockchain fundamentals and block structure
- SHA-256 hashing and hash-linked records
- Tamper-evident data storage
- Python application development
- Flask web application development
- JSON-based persistence
- Basic integrity testing

## 👨‍💻 Author

**Student Mini Project — Blockchain Technology**

Developed for educational and academic purposes.
