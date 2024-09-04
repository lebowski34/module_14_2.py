import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
''')

users = [
    ('User1', 'example1@gmail.com', 10, 1000),
    ('User2', 'example2@gmail.com', 20, 1000),
    ('User3', 'example3@gmail.com', 30, 1000),
    ('User4', 'example4@gmail.com', 40, 1000),
    ('User5', 'example5@gmail.com', 50, 1000),
    ('User6', 'example6@gmail.com', 60, 1000),
    ('User7', 'example7@gmail.com', 70, 1000),
    ('User8', 'example8@gmail.com', 80, 1000),
    ('User9', 'example9@gmail.com', 90, 1000),
    ('User10', 'example10@gmail.com', 100, 1000)
]

cursor.execute("DELETE FROM Users")

cursor.executemany("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", users)

cursor.execute("UPDATE Users SET balance = 500 WHERE id % 2 = 1")

cursor.execute("DELETE FROM Users WHERE id % 3 = 0")

cursor.execute("DELETE FROM Users WHERE id = 6")

cursor.execute("SELECT COUNT(*) FROM Users")
result = cursor.fetchone()

if result is not None:
    total_users = result[0]
else:
    total_users = 0

print(f"Total users: {total_users}")

cursor.execute("SELECT SUM(balance) FROM Users")
result = cursor.fetchone()

if result is not None:
    all_balances = result[0]
else:
    all_balances = 0

print(f"Sum of all balances: {all_balances}")

if total_users > 0:
    average_balance = all_balances / total_users
    print(f"Average balance: {average_balance}")
else:
    print("Нет пользователей в базе данных")

connection.commit()
connection.close()
