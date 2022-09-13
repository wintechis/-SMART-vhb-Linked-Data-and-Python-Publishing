##############################################################################################
## Course   : Linked Data and Python: Introduction                                          ##
## Section  : Serializing (with RDFLib)                                                     ##
## Authors  : Christian Fleiner, Andreas Harth                                              ##
## See more : https://github.com/wintechis/-SMART-vhb-Linked-Data-and-Python-Publishing     ##
##                                                                                          ##
## Learning Goals:                                                                          ##
## - Serialize and serve RDF data in available formats/notations                            ##
## - Provide an overview of available files and formats                                     ##
##############################################################################################

##################################################
## Import libraries
import os
from flask import Flask, make_response, request, send_from_directory, abort, render_template
from rdflib import Graph

##################################################
## Create Flask Webserver (only testing)
## Run in console: Flask --app B_serializing --debug run
app = Flask(__name__)

##################################################
## Store directory to file path folder as global var
FILES = os.path.join(os.path.dirname(__file__), 'files')


############################################################
## Create FOAF data with 
## FOAF-a-matic: http://ldodds.com/foaf/foaf-a-matic.html
## and save data as RDF document in file data directory (here: max.rdf)


###########################################################
# Serve FOAF file (fixed URL)
@app.get('/')
def get_file():
    resp = make_response(send_from_directory(FILES, 'max.rdf'))
    resp.mimetype = 'application/rdf+xml'
    return resp


############################################################
## Serve FOAF file (by variable in URL path) 
# @app.get('/<filename>')
# def get_file(filename:str):
#     resp = make_response(send_from_directory(directory=FILES, path=filename))
#     resp.mimetype = 'application/rdf+xml'
#     return resp


############################################################
## Dict with file extensions as keys and MIMEtypes as values
MIMES = {
    '.rdf': 'application/rdf+xml',
    '.ttl': 'text/turtle',
    '.nt' : 'text/plain',
    '.jsonld': 'application/ld+json'
}

############################################################
## Serve FOAF data in available notations  
# @app.get('/<filename>')
# def get_file(filename:str):
#     name, ext = os.path.splitext(filename) # [0]: filename [1]: .{file extension}
#     mime = get_mime(ext)

#     # Return BAD REQUEST (bc file extension is not supported); 404 would be also fine
#     if not mime: return (f'File extension "{ext}" is not supported!', 400)

#     # Create Response
#     resp = make_response(get_notation(name, ext))

#     # Assign MIMEtype (default: text/html)
#     if resp.status_code == 200: resp.mimetype = mime
#     return resp


# ############################################################
# ## Return available MIMEtype or ''
# def get_mime(ext: str) -> str:
#     if ext in MIMES.keys(): return MIMES[ext] 
#     return ''


# ############################################################
# ## Return Response data''
# def get_notation(name, ext: str):
#     # get file extension of existing file
#     f_ext = get_true_ext(name, ext)

#     if not f_ext:
#         return abort(404) # file does not exist
#     elif f_ext.startswith('.'):
#         f = f'{request.url[:-len(ext)]}{f_ext}'
#         return (serialize(parse(f), ext), 200) # request for serialized data
#     return send_from_directory(FILES, f_ext) # request for original file
    
  
# ############################################################
# ## Return file extension of existing file in files folder (or '')
# def get_true_ext(name: str, ext: str) -> str:
#     root, dirs, files = next(os.walk(FILES))
#     for file in files:
#         if file == f'{name}{ext}':
#             return file
#         elif os.path.splitext(file)[0] == name: 
#             return os.path.splitext(file)[1]
#     return ''


# ############################################################
# ## load RDF data from file in rdflib.Graph
# def parse(file) -> Graph:
#     return Graph().parse(file)

# ############################################################
# ## Serialize graph triples into requested notation/format
# def serialize(g: Graph, ext: str) -> str:
#     if ext.startswith('.'): ext = ext[1:]

#     # File extension does not match identifier of serializer
#     if ext == 'rdf': ext = 'xml' 
#     if ext == 'jsonld': ext = 'json-ld'
#     return g.serialize(format=ext)


# ############################################################
# ## Show overview of available files and formats
# @app.get('/')
# def overview():
#     root, dirs, files = next(os.walk(FILES))

#     # Sort available file names
#     names = sorted([os.path.splitext(f)[0] for f in files])

#     # Note: render_template defines template folder as standard directory
#     return render_template('overview.html', names=names, exts=sorted(MIMES.keys()))