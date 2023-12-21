from flask import Flask, render_template
from routes import routes
import manageDB as mdb


# Lanzar back end
def create_app():
   mdb.init()
   app = Flask(__name__)
   app.register_blueprint(routes)
   return app

if __name__ == '__main__':
   app = create_app()
   
   #TODO: cambiar al desplegar!
   app.run(debug=True)
