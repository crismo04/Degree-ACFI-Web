from flask import Blueprint, render_template
import manageDB as db

# En este archivo se guardan todas las rutas tanto dinamicas como estáticas de la página web
# Cada función incorpora los datos correspondientes a cada una de las plantillas

routes = Blueprint('routes', __name__)

# Esta es la ruta base, o index. Es la landing page.
@routes.route('/')
def home():
   return render_template('index.html', header_fruit=db.get_random_fruits()[0][0])

# Aqui es donde está el catalogo y a donde te lleva la página una vez interactuas con la portada
@routes.route('/fruits')
def fruits():
   print(db.get_all_fruits())
   return render_template('fruits.html', fruits=db.get_all_fruits(), header_fruit=db.get_random_fruits()[0][0])

# Sección con información sobre la página y la tienda
@routes.route('/about')
def about():
   return render_template('about.html', header_fruit=db.get_random_fruits()[0][0])

# Página con la información sobre el método de pago
@routes.route('/payment')
def payment():
   return render_template('payment.html', header_fruit=db.get_random_fruits()[0][0])