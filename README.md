# Linked Data and Python: Publish Content with Flask, Gunicorn and NGINX
![Supported Python Versions](https://img.shields.io/badge/python-3.9-blue.svg)
![Used RDFLib version](https://img.shields.io/badge/rdflib-v6.2-blue.svg)
![Supported Platforms](https://img.shields.io/badge/platforms-Linux%2C%20Windows-blue.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
## Content
This repository offers code snippets and exercises about the application of the Web framwork [Flask](https://flask.palletsprojects.com/en/2.2.x/) and the Python Package [RDFLib](https://rdflib.readthedocs.io/en/stable/) to serve RDF documents on the Web. It is part of the Smart vhb course **Linked Data and Python: Publishing** that also includes descriptive videos. If you are currently enrolled at a Bavarian university, you can access all content via the [smart.vhb.org](https://smart.vhb.org/). This repositoy provides code snippets, examples and exercises for the following elements:

* Serve data and files 
* Serialize and serve RDF data in available formats/notations
* Create Flash messages and retrieve them in HTML template

If you want to learn more about the capabilities of the [RDFLib](https://rdflib.readthedocs.io/en/stable/), please have a look at this [repository](https://github.com/wintechis/SMART-vhb-Linked-Data-and-Python-Introduction).

If you want to learn more about the capabilities of [Flask](https://flask.palletsprojects.com/en/2.2.x/), please check out its official [tutorial](https://flask.palletsprojects.com/en/2.2.x/tutorial/).

## Virtuelle Hochschule Bayern: SMART vhb
[Virtuelle Hochschule Bayern (vhb)](https://www.vhb.org/en/) was founded in 2000 and is a network of 32 universities in Bavaria that provides a platform for sharing and linking digital teaching for its members.
*SMART vhb* courses are blended learning units. The online learning units can be flexibly integrated into classroom teaching and are designed for use across member universities.  If you are currently enrolled at a Bavarian university, you can access all content via the [smart.vhb.org](https://smart.vhb.org/)


## Target Audience
This repository is especially designed for Bavarian students who are also permitted to access the additional content on the Smart vhb repository. Nonetheless, this repository might also help Python developers who are new to the Semantic Web. It is important to distress that this repository does neither teach Flask nor RDFLib. It only provides code snippets how Flask and RDFLib can be instrumentalized to serve RDF documents on the Web.   


## Installation
Open your favoured terminal and clone the repository. Due to the long name, we recommend you give it a new name like "ldpy_intro".
```console
git clone https://github.com/wintechis/-SMART-vhb-Linked-Data-and-Python-Publishing.git ldpy_publish
```
Change directory to the repo folder.
```console
cd ldpy_publish
```
Create a new virtual environment within this folder.
```console
python -m venv env
```
Activate the virtual environment (Windows example).
```console
env/scripts/activate
```

Install Flask (2.2.2), RDFLib (6.2.0), requests (2.28.1), and wheel (0.37.1). You can use also more recent versions, but the code snippets were only tested with the mentioned versions.
```console
pip install flask==2.2.2 rdflib==6.2.0 requests==2.28.1 wheel==0.37.1
```
Congratulations! You have successfully installed all required packages.


## Questions, Remarks and Issues
* If you did not understand a code snippet, let us know by creating a GitHub Issue where the title starts with "Q:"  
* If you are missing any code snippets for understanding specific classes or functions or have a good idea about a new exercise, create a GitHub Issue where the title starts with "R:"
* If you have found an error in the code, then create an GitHub Issue where the title starts with "I:"


## Not enough of RDF and SPARQL?
If you are looking for a simple framework to practice RDF and SPARQL, but do not want to deepdive into one of the open knowledge graphs (DBpedia, WikiData, ...), the [RDF Training and Demonstration Framework (RDeF)](https://github.com/wintechis/RDeF) might be a project, you want to check out. RDeF is a Python framework for creating interactive stories based on RDF triples. In stories, players build their own knowledge base from RDF triples hidden in scenes and uncover new findings by querying this knowledge base with SPARQL queries. RDeF is mainly built upon [Kivy](https://kivy.org/#home) and [RDFLib](https://rdflib.readthedocs.io/en/stable/#getting-started).

## Maintenance
This repository is maintained by the [Chair of Technical Information Systems](https://www.ti.rw.fau.de/), Friedrich-Alexander-Universität Erlangen-Nürnberg.

## License
See [LICENSE](LICENSE) for details.

