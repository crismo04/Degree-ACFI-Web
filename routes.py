from flask import Blueprint, render_template
import manageDB as db

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
   return render_template('index.html', header_fruit=db.get_random_fruits()[0][0])

@routes.route('/fruits')
def fruits():
   print(db.get_all_fruits())
   return render_template('fruits.html', fruits=db.get_all_fruits(), header_fruit=db.get_random_fruits()[0][0])

@routes.route('/about')
def about():
   return render_template('about.html', header_fruit=db.get_random_fruits()[0][0])

@routes.route('/payment')
def payment():
   return render_template('payment.html', header_fruit=db.get_random_fruits()[0][0])