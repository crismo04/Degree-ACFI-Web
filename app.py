from flask import Flask, render_template
from routes import routes
import manageDB as mdb

def create_app():
   mdb.init()
   app = Flask(__name__)
   app.register_blueprint(routes)
   return app

if __name__ == '__main__':
   app = create_app()
   app.run(debug=True)
