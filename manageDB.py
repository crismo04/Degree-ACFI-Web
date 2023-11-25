import sqlite3

def create_database():
  conn = sqlite3.connect('frutería_app.db')
  c = conn.cursor()

  c.execute('''
      CREATE TABLE fruits (
          id INTEGER PRIMARY KEY,
          name TEXT,
          color TEXT
      )
  ''')

  conn.commit()
  conn.close()

def insert_fruit(name, color):
  conn = sqlite3.connect('frutería_app.db')
  c = conn.cursor()

  c.execute("INSERT INTO fruits (name, color) VALUES (?, ?)", (name, color))

  conn.commit()
  conn.close()

def get_all_fruits():
  conn = sqlite3.connect('frutería_app.db')
  c = conn.cursor()

  c.execute("SELECT * FROM fruits")

  rows = c.fetchall()

  conn.close()

  return rows