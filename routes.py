from flask import Blueprint, render_template

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
   return render_template('index.html')

@routes.route('/fruits')
def fruits():
   return render_template('fruits.html')

@routes.route('/about')
def about():
   return render_template('about.html')