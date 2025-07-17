CREATE TABLE IF NOT EXISTS cipher_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    input_text TEXT NOT NULL,
    action TEXT NOT NULL CHECK(action IN ('encrypt', 'decrypt', 'analyze')),
    method TEXT CHECK(method IN ('caesar', 'substitution', 'vigenere', 'xor', 'rail_fence', 'playfair')),
    parameters TEXT,
    output_text TEXT NOT NULL
);