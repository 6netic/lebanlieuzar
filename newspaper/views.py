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
	if request.method == "GET":
		
		if request.args.get('categ') == 'politique':
			param = 'politique'
			url = "https://www.leparisien.fr/politique/"	
		elif request.args.get('categ') == 'economie':
			param = 'economie'
			url = "https://www.leparisien.fr/economie/"
		elif request.args.get('categ') == 'societe':
			param = 'societe'
			url = "https://www.leparisien.fr/societe/"
		elif request.args.get('categ') == 'faits_divers':
			param = 'faits_divers'
			url = "https://www.leparisien.fr/faits-divers/"
		else:
			param = 'politique'
			url = "https://www.leparisien.fr/politique/"
		
		response = requests.get(url)
		html = response.content
		scraped = BeautifulSoup(html, "lxml")

		artTitle, artUrl = [], []

		firstFiveLink = scraped.find_all("a", attrs={"class" : "no-decorate no-active title_sm"})
		for one in firstFiveLink:
			articleUrl = "https:" + one['href']
			articleTitle = one.find('span', attrs={"class" : "story-headline"})
			
			if articleTitle is None:
				articleTitle = one.find('h2', attrs={"class" : "story-headline"}).text.strip()
			else:
				articleTitle = one.find('span', attrs={"class" : "story-headline"}).text.strip()
			
			artUrl.append(articleUrl)
			artTitle.append(articleTitle)
		
		lineNb = len(artTitle)

		return render_template("cat.html", param=param, lineNb=lineNb, artUrl=artUrl, artTitle=artTitle)



@app.route("/article/", methods=['GET'])
def article():
	""" Page that displays a specific article """
	
	# Retrieve urlCat
	if request.method == "GET":
		blocks = []
		url = request.args.get('article')

		response = requests.get(url)
		html = response.content
		scraped = BeautifulSoup(html, "lxml")

		title = scraped.find('h1', attrs={"class" : "title_xl col margin_bottom_headline"}).text.strip()
		paragraphs = scraped.find_all('p', attrs={'class':'paragraph text_align_left'})
		for parag in paragraphs:
			parag = parag.text.strip()
			blocks.append(parag)
		image = scraped.find("img", attrs={"class" : "image"})['src']
		image = "https://www.leparisien.fr" + image

	return render_template("art.html", title=title, blocks=blocks, image=image)





































	