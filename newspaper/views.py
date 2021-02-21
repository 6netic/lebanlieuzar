import os
import requests
import lxml
from bs4 import BeautifulSoup
from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename


app = Flask(__name__)


@app.route("/", methods=['GET'])
def category():
	""" Homepage that displays all articles from category 'Politique' """

	# Retrieve urlCat
	#if (get['cat']) == ''
	# search_sentence = request.form.get('mySearch')
	# if request.method == "GET":




	return render_template("cat.html")