##############################################################################################
## Course   : Linked Data and Python: Introduction                                          ##
## Section  : Basic                                                                         ##
## Authors  : Christian Fleiner, Andreas Harth                                              ##
## See more : https://github.com/wintechis/-SMART-vhb-Linked-Data-and-Python-Publishing     ##
##                                                                                          ##
## Learning Goals:                                                                          ##
## - Create a minimal Flask application (for testing)                                       ##
## - Serve data and files                                                                   ##
##############################################################################################


##################################################
## Import libraries
import os
from flask import Flask, make_response, request, send_from_directory

##################################################
## Create Flask Webserver (only testing)
## Run in console: Flask --app A_basic --debug run
app = Flask(__name__)


##################################################
## Serve simple RDF data (as HTML document)
@app.route("/")
def get_turtle():
    return """
    PREFIX : <#>
    :s  :p  :o .
    """

##################################################
## Serve RDF data with correct MIMEtype
# @app.route("/")
# def get_turtle():
#     ttl =  """
#     PREFIX : <#>
#     :s  :p  :o .
#     """
#     resp = make_response(ttl)
#     resp.mimetype = 'text/turtle'
#     return resp

##################################################
## Allow and check HTTP method of request (single function)
# @app.route("/", methods=('GET', 'POST')) # HEAD automatically allowed with GET
# def get_turtle():
#     if request.method == 'POST': return 'This was a POST Request'
#     ttl =  """
#     PREFIX : <#>
#     :s  :p  :o .
#     """
#     resp = make_response(ttl)
#     resp.mimetype = 'text/turtle'
#     return resp

##################################################
## Allow and check HTTP method of request (one function per method)
# @app.get('/')
# def get_turtle():
#     ttl =  """
#     PREFIX : <#>
#     :s  :p  :o .
#     """
#     resp = make_response(ttl)
#     resp.mimetype = 'text/turtle'
#     return resp

# @app.post('/')
# def post_turtle():
#     return 'This was a POST Request'


##################################################
## Serving files
# @app.get('/')
# def get_turtle():
#     path = os.path.dirname(__file__)
#     resp = make_response(send_from_directory(directory=path, path='dummy.ttl'))
#     resp.mimetype = 'text/turtle'
#     return resp