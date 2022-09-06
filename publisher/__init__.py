from flask import Flask
from .C_redirecting import overview, get_file

####################################################
## How to easily get a secret key from your terminal
## $ python -c 'import secrets; print(secrets.token_hex())'
####################################################

def create_app(test_config=None):
    app = Flask(__name__)
    app.secret_key = 'bbe5ab933da0be71ffe196d77527a6a30b7eb73347ca029c6a7447ae3c3ca4e6'
    app.add_url_rule('/', view_func=overview)
    app.add_url_rule('/<filename>', view_func=get_file)
    # view or bg
    return app