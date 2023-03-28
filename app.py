# Entry point for Python website

from flask import Flask

from views import views # Importing from "views.py"

app = Flask(__name__) # Initializing the application

app.register_blueprint(views, url_prefix="/views") 

if __name__ == '__main__':
    app.run(debug=True,port=8000) # Debug is true so that when files are changed, app is auto-refreshed
    
