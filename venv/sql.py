import sqlite3

with sqlite3.connect("sample.db") as connection:
    c = connection.cursor()
    c.execute("DROP TABLE posts")
    c.execute("CREATE TABLE posts(title TEXT, description TEXT)")
    c.execute('INSERT INTO posts VALUES("good","i am good")')
    c.execute('INSERT INTO posts VALUES("bad", "i am bad")')