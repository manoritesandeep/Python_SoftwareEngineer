"""
Concerned with storing and retrieving pages from a database.
"""

import sqlite3

def create_book_table():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS pages(name text primary key, author text, read integer)')

    connection.commit()
    connection.close()

def add_book(name, author):
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    # two ways to execute insert. Below not recommended. Leaves SQL injection attack
    # cursor.execute(f'INSERT INTO pages VALUES("{name}","{author}",0)')

    # use this instead, more popular and avoids attacks
    cursor.execute('INSERT INTO pages VALUES(?,?,0)', (name, author))

    connection.commit()
    connection.close()

def get_all_books():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM pages')
    books = [{"name": row[0],"author": row[1],"read": row[2]} for row in cursor.fetchall()]
    # cursor.fetchall() returns tuple [(name,author,read), (name,author,read)]

    # we don't need to commit since we are not writing anything, only reading!
    #connection.commit()
    connection.close()

    return books

def mark_book_as_read(name):
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    cursor.execute('UPDATE pages SET read=1 WHERE name=?',(name,))

    connection.commit()
    connection.close()

def delete_book(name):
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    cursor.execute('DELETE FROM pages WHERE name=?', (name,))

    connection.commit()
    connection.close()