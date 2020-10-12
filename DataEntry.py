import sqlite3

FILE = sqlite3.connect("CREDENTIALS.db")

CURSOR = FILE.cursor()

CURSOR.execute('CREATE TABLE IF NOT EXISTS Orders(name TEXT, address TEXT, email TEXT, product_name TEXT, amount INTEGER, order_number INTEGER)')

CURSOR.execute('CREATE TABLE IF NOT EXISTS Credentials(username TEXT, password TEXT)')

CURSOR.execute('DELETE FROM Credentials')

CURSOR.execute('DELETE FROM Orders')

CURSOR.execute('INSERT INTO Credentials VALUES(\'ADMIN\', \'one\')')

CURSOR.execute('INSERT INTO orders VALUES(\'BASE\', \'BASE\', \'BASE\', \'BASE\', \'0\', \'0\')')

FILE.commit()

FILE.close()