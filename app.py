from flask import Flask, request, render_template, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = "secret_key"

db = sqlite3.connect('shop.db')

@app.route("/signup", methods=['GET', 'POST'])
def signup():
  if request.method == 'POST':
      name = request.form['name']
      username = request.form['username']
      email = request.form['email']
      password = request.form['password']
      cursor = db.cursor()

      cursor.execute("SELECT username FROM users")
      numrow = cursor.fetchone()
      if numrow is not None:
          return render_template("signup.html", message="Username is already in use.")

      cursor.execute("INSERT INTO users(name, username, email, password) VALUES(?, ?, ?, ?)",
                   (name, username, email, password))
      db.commit()
      cursor.close()
      return redirect(url_for('login'))
  else:
      return render_template("signup.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
      username = request.form['username']
      password = request.form['password']
      cursor = db.cursor()

      cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?",
                   (username, password))
      user = cursor.fetchone()
      if user is None:
          return render_template("login.html", message="Invalid username or password.")

      session['logged_in'] = True
      session['username'] = username
      cursor.close()
      return redirect(url_for('dashboard'))
  else:
      return render_template("login.html")

@app.route("/dashboard")
def dashboard():
  if 'logged_in' in session:
      return render_template("dashboard.html", username=session['username'])
  else:
      return redirect(url_for('login'))

@app.route("/logout")
def logout():
  session.clear()
  return redirect(url_for('login'))

@app.route("/")
def home():
   return render_template("home.html")

if __name__ == '__main__':
  app.run(debug=True)