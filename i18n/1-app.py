#!/usr/bin/env python3
from logging import config
from flask import Flask, app ,render_template
from flask_babel import Babel 
class Config(object):
    app = Flask(__name__)
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"
   
   #APPLY configuration 
    app.config.from_object(config) 

    #Initialize Babel 
    babel = Babel(app)


    @app.route('/', strict_slashes=False)
    def hello_world():
    
        return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")




