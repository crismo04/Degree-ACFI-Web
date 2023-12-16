import sqlite3
import os
import download_image as image

def create_database():
  # Get the current directory
  current_directory = os.getcwd()

  # Concatenate the current directory with your database name
  db_path = os.path.join(current_directory, 'frutería_app.db')

  conn = sqlite3.connect(db_path)
  c = conn.cursor()

  # Drop the table if it exists
  c.execute('''DROP TABLE IF EXISTS fruits''')
  c.execute('''DROP TABLE IF EXISTS header''')

  c.execute('''
      CREATE  TABLE fruits (
          id INTEGER PRIMARY KEY,
          name TEXT,
          color TEXT,
          price INTEGER,
          url TEXT,
          temporada DATE
      )
  ''')
  c.execute('''
    CREATE  TABLE header (
        id INTEGER PRIMARY KEY,
        name TEXT
    )
''')

  conn.commit()
  conn.close()

def insert_fruit(name, color, price, db, url):
  # Get the current directory
  current_directory = os.getcwd()

  # Concatenate the current directory with your database name
  db_path = os.path.join(current_directory, 'frutería_app.db')

  conn = sqlite3.connect(db_path)
  c = conn.cursor()
  if db == 'fruits':
    c.execute("INSERT INTO fruits (name, color, price, url) VALUES (?, ?, ?, ?)", (name, color, price, url))
  else:
    c.execute(f"INSERT INTO {db} (name) VALUES ('{name}')")

  conn.commit()
  conn.close()

def populate_test_database():

  fruits_data = [
    {"name": "Ajo", "color": "grey", "price": 1.50},
    {"name": "Aguacate", "color": "Green", "price": 2.00},
    {"name": "Banano", "color": "Olive", "price": 1.20},
    {"name": "Cebollín", "color": "Green", "price": 1.80},
    {"name": "Chayote", "color": "Green", "price": 1.50},
    {"name": "Higo", "color": "Purple", "price": 2.20},
    {"name": "Jengibre", "color": "Brown", "price": 2.50},
    {"name": "Kiwi", "color": "Brown", "price": 1.50},
    {"name": "Limón", "color": "Olive", "price": 1.20},
    {"name": "Mango", "color": "Orange", "price": 2.00},
    {"name": "Nabo", "color": "grey", "price": 1.80},
    {"name": "Pepino", "color": "Green", "price": 1.50},
    {"name": "Pimiento", "color": "Red", "price": 2.50},
    {"name": "Plátano", "color": "Olive", "price": 1.20},
    {"name": "Rábano", "color": "Red", "price": 1.80},
    {"name": "Tomate", "color": "Red", "price": 2.00},
    {"name": "Coco", "color": "Brown", "price": 2.50},
    {"name": "Caqui", "color": "Orange", "price": 2.00},
    {"name": "Maní", "color": "Brown", "price": 1.50},
    {"name": "Melocotón", "color": "Orange", "price": 2.00},
    {"name": "Melón", "color": "Green", "price": 1.50},
    {"name": "Pomelo", "color": "Olive", "price": 2.20},
    {"name": "Tamarindo", "color": "Brown", "price": 1.80},
    {"name": "Uva", "color": "Purple", "price": 2.50},
    {"name": "Calabacín", "color": "Green", "price": 1.20},
    {"name": "Cantalupo", "color": "Orange", "price": 2.00},
    {"name": "Champiñón", "color": "grey", "price": 1.80},
    {"name": "Espárrago", "color": "Green", "price": 2.00},
    {"name": "Puerro", "color": "Green", "price": 1.50},
    {"name": "Papayo", "color": "Orange", "price": 2.20},
    {"name": "Pera", "color": "Green", "price": 1.50},
    {"name": "Clementina", "color": "Orange", "price": 1.80},
    {"name": "Níspero", "color": "Orange", "price": 2.50},
    {"name": "Cacao", "color": "Brown", "price": 1.50},
    {"name": "Haba", "color": "Green", "price": 2.00},
    {"name": "Acelga", "color": "Green", "price": 1.80},
    {"name": "Azafrán", "color": "Olive", "price": 2.00},
    {"name": "Caña de azúcar", "color": "Green", "price": 1.50},
    {"name": "Cactus", "color": "Green", "price": 2.20},
    {"name": "Frambuesa", "color": "Red", "price": 1.80},
    {"name": "Membrillo", "color": "Olive", "price": 1.50}
  ]

  # Insert each fruit into the database using the existing function
  for fruit in fruits_data:
      im = image.get_google_img(fruit["name"])
      insert_fruit(fruit["name"], fruit["color"], fruit["price"], 'fruits', im)

  h_data = [
  {"name": "RIESCO"},
  {"name": "Producto"},
  {"name": "FRUTERO"},
  {"name": "FRUTERO"},
  {"name": "Robo descarado de imagenes de google"},
  {"name": "Proyecto de AUDITORÍA, CALIDAD Y FIABILIDAD INFORMÁTICAS"},
  {"name": "Ajo"},
  {"name": "Aguacate"},
  {"name": "Cebollín"},
  {"name": "Chayote"},
  {"name": "Higo"},
  {"name": "Jengibre"},
  {"name": "Kiwi"},
  {"name": "Limón"},
  {"name": "Mango"},
  {"name": "Nabo"},
  {"name": "Pepino"},
  {"name": "Pimiento"},
  {"name": "Plátano"},
  {"name": "Rábano"},
  {"name": "Tomate"},
  {"name": "Coco"},
  {"name": "Caqui"},
  {"name": "Maní"},
  {"name": "Melocotón"},
  {"name": "Melón"},
  {"name": "Pomelo"},
  {"name": "Tamarindo"},
  {"name": "Calabacín"},
  {"name": "Cantalupo"},
  {"name": "Champiñón"},
  {"name": "Espárrago"},
  {"name": "Puerro"},
  {"name": "Papayon"},
  {"name": "Ciruelo"},
  {"name": "Níspero"},
  {"name": "Cacao"},
  {"name": "Azafrán"},
  {"name": "Cactus"},
  {"name": "Cacao"},
  {"name": "Membrillo"},
  ]

  # Insert each fruit into the database using the existing function
  for h in h_data:
      insert_fruit(h["name"], None, None, 'header', None)


def get_all_fruits(db='fruits'):
  # Get the current directory
  current_directory = os.getcwd()
  # Concatenate the current directory with your database name
  db_path = os.path.join(current_directory, 'frutería_app.db')
  conn = sqlite3.connect(db_path)
  c = conn.cursor()
  c.execute(f"SELECT * FROM {db}")
  rows = c.fetchall()
  conn.close()
  return rows

def get_random_fruits(db='header'):
  # Get the current directory
  current_directory = os.getcwd()
  # Concatenate the current directory with your database name
  db_path = os.path.join(current_directory, 'frutería_app.db')
  conn = sqlite3.connect(db_path)
  c = conn.cursor()
  c.execute(f"SELECT name FROM {db} ORDER BY RANDOM() LIMIT 1")
  rows = c.fetchall()
  conn.close()
  return rows

def init():
  create_database()
  populate_test_database()

