# Secure Ciphertext Analyzer 

A Flask-based web application for encrypting, decrypting, and analyzing text using classical cryptographic algorithms. Supports multiple ciphers with customizable parameters, password strength analysis, and operation logging.

## Features ✨

- **6 Cryptographic Algorithms**:
  - Caesar Cipher
  - Substitution Cipher
  - Vigenère Cipher
  - XOR Cipher
  - Rail Fence Cipher
  - Playfair Cipher
- **Password Strength Analyzer** with detailed feedback
- **Operation Logging** to SQLite database
- **Database Viewer** for audit and analysis
- **Responsive UI** with dynamic parameter fields
- **Error Handling** with clear user feedback

## Installation 🛠️

### Prerequisites
- Python 3.8+
- SQLite

### Setup
1. Clone the repository:

   cd SecureCipherProject
Install dependencies:

bash
pip install -r requirements.txt
Initialize the database:

bash
sqlite3 cipher.db < schema.sql
Run the application:

bash
python app.py
Access the app at: http://localhost:5000

Usage 🖥️
Encrypt/Decrypt Text:

Enter text in the input area

Select a cipher from the dropdown

Provide required parameters

Click "Encrypt" or "Decrypt"

Analyze Password Strength:

Enter a password in the input area

Click "Analyze Password"

View Database Logs:

Click the "DB" link at bottom right

Supported Ciphers 🧩
Cipher	Key Type	Special Features
Caesar	Shift (default: 3)	Case-sensitive
Substitution	Predefined key	Static character mapping
Vigenère	Custom keyword	Case-preserving
XOR	Integer (0-255)	Supports all characters
Rail Fence	Number of rails	Zig-zag pattern
Playfair	Custom keyword	Replaces 'J' with 'I', adds filler 'X'
Database Schema 📊
The application logs all operations to cipher.db with the following structure:

sql
CREATE TABLE cipher_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    input_text TEXT NOT NULL,
    action TEXT NOT NULL CHECK(action IN ('encrypt', 'decrypt', 'analyze')),
    method TEXT CHECK(method IN ('caesar', 'substitution', 'vigenere', 'xor', 'rail_fence', 'playfair')),
    parameters TEXT,
    output_text TEXT NOT NULL
);
Code Structure 📂
text
SecureCipherProject/
├── ciphers/               # Cryptographic algorithm implementations
│   ├── caesar.py          # Caesar cipher implementation
│   ├── substitution.py    # Substitution cipher
│   ├── vigenere.py        # Vigenère cipher
│   ├── xor.py             # XOR cipher
│   ├── rail_fence.py      # Rail Fence cipher
│   └── playfair.py        # Playfair cipher
├── static/                # Static assets
│   └── styles.css         # Main stylesheet
├── templates/             # HTML templates
│   ├── index.html         # Main application interface
│   └── view_data.html     # Database log viewer
├── app.py                 # Flask application core
├── requirements.txt       # Python dependencies
└── schema.sql             # Database schema definition
Known Limitations ⚠️
Playfair Cipher:

Decryption removes all 'X' characters which might remove legitimate 'X's from original plaintext

Non-alphabetic characters are not supported

Database:

Passwords are stored in plaintext (consider hashing for production)

No user authentication implemented

Substitution Cipher:

Uses a static key (not suitable for secure communication)

### Notes on Implementation:
1. The Playfair cipher limitation is noted in the README (removes all 'X's during decryption)
2. Database stores operations but passwords are in plaintext - consider adding bcrypt hashing for production
3. The app includes a database viewer accessible via the "DB" link
4. All cipher operations are logged with parameters and timestamps
5. The UI dynamically shows/hides parameters based on selected cipher
