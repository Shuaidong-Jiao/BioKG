import nltk
import json
import re
import numpy as np
from nltk import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords # Import the stop word list

from flask import Flask,request
from flask import render_template
from flask_bootstrap import Bootstrap
import KBQA
from KBQA import answer_question

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/query/',methods = ['GET'])
def query():
	if request.method == 'GET':
		results = []
		q = request.args.get('q')
		results = answer_question(q)## use answer_question function to analyze question and return answers
		return render_template('index.html',q = q,results = results)
	return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'),404

if __name__ == '__main__':
	app.run(debug = True)