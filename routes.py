from flask import Blueprint, render_template
import manageDB as db

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
   return render_template('index.html')

@routes.route('/fruits')
def fruits():
   print(db.get_all_fruits())
   return render_template('fruits.html', fruits=db.get_all_fruits())

@routes.route('/about')
def about():
   return render_template('about.html')

@routes.route('/payment')
def payment():
   return render_template('payment.html')