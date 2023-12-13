import sqlite3

def create_database():
  conn = sqlite3.connect('frutería_app.db')
  c = conn.cursor()

  c.execute('''
      CREATE TABLE fruits (
          id INTEGER PRIMARY KEY,
          name TEXT,
          color TEXT,
          price INTEGER
      )
  ''')

  conn.commit()
  conn.close()

def insert_fruit(name, color, price):
  conn = sqlite3.connect('frutería_app.db')
  c = conn.cursor()

  c.execute("INSERT INTO fruits (name, color, price) VALUES (?, ?, ?)", (name, color, price))

  conn.commit()
  conn.close()

def populate_test_database():

  fruits_data = [
      {"name": "Apple", "color": "Red", "price": 1.00},
      {"name": "Banana", "color": "Yellow", "price": 0.75},
      {"name": "Orange", "color": "Orange", "price": 1.25},
      {"name": "Grapes", "color": "Purple", "price": 2.50},
      {"name": "Strawberry", "color": "Red", "price": 1.50},
      {"name": "Mango", "color": "Yellow", "price": 2.00},
      {"name": "Blueberry", "color": "Blue", "price": 3.00},
      {"name": "Watermelon", "color": "Green", "price": 1.75},
      {"name": "Pineapple", "color": "Yellow", "price": 2.50},
      {"name": "Cherry", "color": "Red", "price": 1.80},
      {"name": "Kiwi", "color": "Brown", "price": 2.20},
      {"name": "Peach", "color": "Orange", "price": 1.90},
      {"name": "Pear", "color": "Green", "price": 1.60},
      {"name": "Plum", "color": "Purple", "price": 2.10},
      {"name": "Raspberry", "color": "Red", "price": 3.50},
  ]

  # Insert each fruit into the database using the existing function
  for fruit in fruits_data:
      insert_fruit(fruit["name"], fruit["color"], fruit["price"])
      
      

def get_all_fruits():
  conn = sqlite3.connect('frutería_app.db')
  c = conn.cursor()

  c.execute("SELECT * FROM fruits")

  rows = c.fetchall()

  conn.close()

  return rows