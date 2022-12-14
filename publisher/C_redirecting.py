##############################################################################################
## Course   : Linked Data and Python: Introduction                                          ##
## Section  : Redirecting                                                                   ##
## Authors  : Christian Fleiner, Andreas Harth                                              ##
## See more : https://github.com/wintechis/-SMART-vhb-Linked-Data-and-Python-Publishing     ##
##                                                                                          ##
## Learning Goals:                                                                          ##
## - Redirecting client                                                                     ##
## - Create Flash messages and retrieve them in HTML template                               ##
##############################################################################################

##################################################
## Import libraries
import os
from flask import Flask, make_response, request, send_from_directory, render_template, redirect, url_for, flash


from .B_serializing import get_mime, get_true_ext, parse, serialize

##################################################
## Create Flask Webserver (only testing)
## Run in console: flask --app C_redirecting --debug run
app = Flask(__name__)

##################################################
## Set secret key (for testing)
app.secret_key = '12345'

##################################################
## Store directory to file path folder as global var
FILES = os.path.join(os.path.dirname(__file__), 'files')

############################################################
## Dict with file extensions as keys and MIMEtypes as values
MIMES = {
    '.rdf': 'application/rdf+xml',
    '.ttl': 'text/turtle',
    '.nt' : 'text/plain',
    '.jsonld': 'application/ld+json'
}

############################################################
## Serve FOAF data in available notations (with redirect and flash)
@app.get('/<filename>')
def get_file(filename:str):
    name, ext = os.path.splitext(filename)
    mime = get_mime(ext)

    if not mime: 
        flash(f'File extension "{ext}" is not supported!')
        return redirect(url_for('overview'), 404)

    resp = make_response(get_notation(name, ext))
    if resp.status_code == 200: resp.mimetype = mime
    return resp



############################################################
## Show overview of available files and formats (with flash)
@app.get('/')
def overview():
    root, dirs, files = next(os.walk(FILES))
    names = sorted([os.path.splitext(f)[0] for f in files])
    return render_template('overview_with_flash.html', names=names, exts=sorted(MIMES.keys()))


# ############################################################
## Return Response data''
def get_notation(name, ext: str):
    # get file extension of existing file
    f_ext = get_true_ext(name, ext)

    if not f_ext:
        flash(f'Filename "{name}" does not exist!')
        return redirect(url_for('overview'), 404)
    elif f_ext.startswith('.'):
        f = f'{request.url[:-len(ext)]}{f_ext}'
        return (serialize(parse(f), ext), 200) # request for serialized data
    return send_from_directory(FILES, f_ext) # request for original file