import random
import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
)
''')

cursor.execute(" CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

# cursor.execute(" INSERT INTO Users (username, email, age) VALUES (?, ?, ?)", ("newuser","ex@gmail.com","20"))
# for i in range(30):
#     cursor.execute(" INSERT INTO Users (username, email, age) VALUES (?, ?, ?)", (f"newuser{i}", f"{i}ex@gmail.com", str (random.randint(20, 60))))

# cursor.execute("UPDATE Users SET age = ? WHERE username = ?", (29, "newuser"))

# cursor.execute("DELETE FROM Users WHERE username = ?", ("newuser",))

# cursor.execute("SELECT * FROM Users")
# SELECT, FROM, WHERE, GROUP BY, HAVING, ORDER BY #

# cursor.execute("SELECT username, age FROM Users WHERE age > ?", (29,))

cursor.execute("SELECT username, age FROM Users GROUP BY AGE")

users = cursor.fetchall()
for user in users:
    print(user)

connection.commit()
connection.close()