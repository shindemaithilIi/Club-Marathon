import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS registrations(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    gender TEXT,
    email TEXT,
    mobile TEXT,
    address TEXT,
    blood_group TEXT,
    emergency_contact TEXT,
    race_distance TEXT,
    tshirt_size TEXT,
    medical_certificate TEXT,
    previous_participant TEXT,
    previous_certificate TEXT,
    fee_status TEXT
)
""")
 
conn.commit()
conn.close()

print("Database created successfully!") 