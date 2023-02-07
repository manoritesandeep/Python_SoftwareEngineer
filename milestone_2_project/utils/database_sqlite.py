"""
Concerned with storing and retrieving pages from a database.
"""
from .database_connection import DatabaseConnection

def create_book_table():
    with DatabaseConnection() as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS pages(name text primary key, author text, read integer)')


def add_book(name, author):
    with DatabaseConnection() as connection:
        cursor = connection.cursor()
        # two ways to execute insert. Below not recommended. Leaves SQL injection attack
        # cursor.execute(f'INSERT INTO pages VALUES("{name}","{author}",0)')
        # use this instead, more popular and avoids attacks
        cursor.execute('INSERT INTO pages VALUES(?,?,0)', (name, author))


def get_all_books():
    with DatabaseConnection() as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM pages')
        books = [{"name": row[0],"author": row[1],"read": row[2]} for row in cursor.fetchall()]
        # cursor.fetchall() returns tuple [(name,author,read), (name,author,read)]
    return books


def mark_book_as_read(name):
    with DatabaseConnection() as connection:
        cursor = connection.cursor()

        cursor.execute('UPDATE pages SET read=1 WHERE name=?',(name,))


def delete_book(name):
    with DatabaseConnection() as connection:
        cursor = connection.cursor()

        cursor.execute('DELETE FROM pages WHERE name=?', (name,))