import csv
import mysql.connector

# 🔹 Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ap@ragh0820!",   # 👉 Put your MySQL password here if you have one
    database="student_db"
)

cursor = conn.cursor()

# 🔹 Open CSV file
filename = "student_behavior_updated.csv"

with open(filename, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        cursor.execute("""
            INSERT INTO student_behavior 
            (Date, Screen_Time, Study_Hours, Sleep, Gym, Mood, Instagram, YouTube, Productivity_Score)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """, tuple(row.values()))

# 🔹 Save changes
conn.commit()

# 🔹 Close connection
cursor.close()
conn.close()

print("✅ CSV data uploaded to MySQL successfully!")
