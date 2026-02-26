from flask import Flask, render_template, request
import sqlite3
import json
import os
from ciphers.caesar import caesar_cipher
from ciphers.substitution import substitution_cipher
from ciphers.vigenere import vigenere_encrypt, vigenere_decrypt
from ciphers.xor import xor_encrypt, xor_decrypt
from ciphers.rail_fence import rail_fence_encrypt, rail_fence_decrypt
from ciphers.playfair import playfair_encrypt, playfair_decrypt

app = Flask(__name__)
DATABASE = 'cipher.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    if not os.path.exists(DATABASE):
        conn = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            conn.executescript(f.read())
        conn.close()

# Initialize database on app start
with app.app_context():
    init_db()

def analyze_password(password):
    import re
    feedback = []
    score = 0

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("At least 8 characters")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Uppercase letter")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Lowercase letter")

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Number")

    if re.search(r'[@$!%*?&#]', password):
        score += 1
    else:
        feedback.append("Special character")

    return "Strong password" if score >= 4 else f"Weak: {', '.join(feedback)}"

@app.route("/")
def home():
    return render_template("index.html", output="", text="")

@app.route("/view-data")
def view_data():
    try:
        conn = get_db()
        logs = conn.execute('SELECT * FROM cipher_logs ORDER BY timestamp DESC').fetchall()
        conn.close()
        return render_template("view_data.html", logs=logs)
    except Exception as e:
        return f"Database Error: {str(e)}"

@app.route("/process", methods=["POST"])
def process():
    text = request.form.get("plaintext", "")
    action = request.form.get("action")
    method = request.form.get("encryption-method")
    output = text
    params = {}

    try:
        if action == "encrypt":
            if method == "caesar":
                output = caesar_cipher(text)
                params = {"shift": 3}
            elif method == "substitution":
                output = substitution_cipher(text)
            elif method == "vigenere":
                keyword = request.form.get("keyword", "")
                output = vigenere_encrypt(text, keyword)
                params = {"keyword": keyword}
            elif method == "xor":
                key = int(request.form.get("key", 0))
                output = xor_encrypt(text, key)
                params = {"key": key}
            elif method == "rail_fence":
                rails = int(request.form.get("rails", 3))
                output = rail_fence_encrypt(text, rails)
                params = {"rails": rails}
            elif method == "playfair":
                keyword = request.form.get("keyword", "")
                output = playfair_encrypt(text, keyword)
                params = {"keyword": keyword}

        elif action == "decrypt":
            if method == "caesar":
                output = caesar_cipher(text, decrypt=True)
                params = {"shift": 3}
            elif method == "substitution":
                output = substitution_cipher(text, decrypt=True)
            elif method == "vigenere":
                keyword = request.form.get("keyword", "")
                output = vigenere_decrypt(text, keyword)
                params = {"keyword": keyword}
            elif method == "xor":
                key = int(request.form.get("key", 0))
                output = xor_decrypt(text, key)
                params = {"key": key}
            elif method == "rail_fence":
                rails = int(request.form.get("rails", 3))
                output = rail_fence_decrypt(text, rails)
                params = {"rails": rails}
            elif method == "playfair":
                keyword = request.form.get("keyword", "")
                output = playfair_decrypt(text, keyword)
                params = {"keyword": keyword}

        elif action == "analyze":
            output = analyze_password(text)
            method = None
            params = None

        # Log to database
        conn = get_db()
        conn.execute(
            'INSERT INTO cipher_logs (input_text, action, method, parameters, output_text) '
            'VALUES (?, ?, ?, ?, ?)',
            (text, action, method, json.dumps(params) if params else None, output)
        )
        conn.commit()
        conn.close()

    except Exception as e:
        output = f"Error: {str(e)}"

    return render_template("index.html", output=output, text=text)

if __name__ == "__main__":
    app.run(debug=True)
