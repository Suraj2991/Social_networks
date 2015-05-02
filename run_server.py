from flask import Flask
from flask import render_template
from gensim import models
import numpy as np
from operator import itemgetter
from flask import request, Response, jsonify
#from flask.ext.cors import CORS
app = Flask(__name__)
#cors = CORS(app)

#CORS(app, resources=r'/example_array', allow_headers='Content-Type')

def get_words(tups, w_list):
	
	for keys, vals in tups:
		if keys not in w_list:
			w_list.append(keys)
	return w_list

def get_similarities(m1, m2, m3, m4, m5, m6, word, w_n):
	mods = [m1, m2, m3, m4, m5, m6]
	simis = []
	for w in word:
		simis_w = []
		for mos in mods:
			try:
			    val = mos.similarity(w_n, w)
			    simis_w.append(val+1)
			except:
			    simis_w.append(1)
		simis.append(simis_w)
	return simis
		    


@app.route('/')
def index():
    return render_template('index.html')

def get_array(word, vals):
	year_lists = ['2008', '2009', '2010', '2011', '2012', '2013', '2014']
	final_list = []
	for v in range(len(vals)):
		dict2 = {}
		dict2['date'] = year_lists[v]
		dict2['price'] = vals[v]
		dict2['symbol'] = word
		final_list.append(dict2)
	return final_list
		

def create_dict(tuples):
	lists = []
	for i,j,k in tuples:
		word_dict = {}
		word_dict['key'] = i
		word_dict['values'] = get_array(i,j)
		lists.append(word_dict)
	return lists
"""
@app.route('/', methods=['POST'])
def load_models():
    word_name = request.form['interestingtextfield']
    x = tuple(mod12.most_similar(word_name))
    y = tuple(mod13.most_similar(word_name))
    z = tuple(mod14.most_similar(word_name))
    words = []
    words = get_words(x, words) 
    words = get_words(y, words)
    words = get_words(z, words)
    similars = get_similarities(mod09, mod10, mod11, mod12, mod13, mod14, words, word_name)
    varians = map(np.var, similars)
    pairs = zip(words, similars, varians)	
    final_file = {}
    pairs.sort(key=itemgetter(2), reverse=True)
    if request.form['my-form'] == 'Higher Variance':
	    final_file['Results'] = create_dict(pairs[:6])
    else:
	    final_file['Results'] = create_dict(pairs[-6:])
    return jsonify(final_file)
"""

@app.route("/example_array/<word_name>", methods=['GET'])
def load_models2(word_name):
    print "We are in the function"
    print word_name
    #word_name = request.form['interestingtextfield']
    #import pdb; pdb.set_trace();
    
    x = tuple(mod12.most_similar(word_name))
    y = tuple(mod13.most_similar(word_name))
    z = tuple(mod14.most_similar(word_name))
    words = []
    words = get_words(x, words) 
    words = get_words(y, words)
    words = get_words(z, words)
    similars = get_similarities(mod09, mod10, mod11, mod12, mod13, mod14, words, word_name)
    varians = map(np.var, similars)
    pairs = zip(words, similars, varians)	
    final_file = {}
    pairs.sort(key=itemgetter(2), reverse=True)
    """
    if request.form['my-form'] == 'Higher Variance':
	    final_file['Results'] = create_dict(pairs[:6])
    else:
	    final_file['Results'] = create_dict(pairs[-6:])
    """
    final_file['Results'] = create_dict(pairs[:4])
    return jsonify(final_file)
    #return render_template('index.html', result=final_file)

print "Loading Models 2008 - 2011"
mod08 = models.Word2Vec.load('model2008')
mod09 = models.Word2Vec.load('model2009')
mod10 = models.Word2Vec.load('model2010')
mod11 = models.Word2Vec.load('model2011')
print "2012 - 2014"
mod12 = models.Word2Vec.load('model2012')
mod13 = models.Word2Vec.load('model2013')
mod14 = models.Word2Vec.load('model2014')
app.run(debug=True)
