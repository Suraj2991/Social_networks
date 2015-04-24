__author__ = 'suraj2991'
import numpy as np
import pandas as pd
import glob
import sys
import os
from operator import itemgetter
from gensim import corpora, models
import logging
import re
from nltk.corpus import stopwords
import nltk
import cython
#nltk.download()
def text_proc(Files):
    TextFiles = []
    for i in Files:
        f = open(i)
        TextFiles.append(f.readlines())
    Final_text = []
    for lines in TextFiles:
        Z = []
        for line in lines:
            Z = Z + list(set(re.findall(r"[\w']+", line.lower())))

        Final_text.append(list(set(Z)))

    print len(Final_text)

    
    return Final_text
    


def ExtractFile(pwd):
    i = 0
    for root, dirs, file in os.walk(pwd):
	i = i+1
        text_law = []
        fil = glob.glob(os.path.join(root, '*_*052013*.txt'))
    return fil


class Sentence(object):
	def __init__(self, dirname):
		self.dirname = dirname
	def __iter__(self):
		stpwrds = stopwords.words('english')
		stpwrds += ['reuters', 'span']
		for root,dirNames,fname in os.walk(self.dirname):
		    	files = glob.glob(os.path.join(root, '*.txt'))
			for f in files:	
                            for line in open(f, 'r'):
				y = re.sub("\(<span (.*)\</span>\)", "", line)
				z = re.sub("\(Reuters\) -", "", y)
				x = re.sub("[^a-zA-Z]", " ",z).lower().split()
				new_line = [w for w in x if not w in stpwrds]
				yield new_line		

def main(path):
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    sentences = Sentence(path)
    #import pdb; pdb.set_trace() 

    num_features = 300                          
    min_word_count = 15                         
    num_workers = 8       
    context = 10                                                                                              
    downsampling = 1e-3   # Downsample setting for frequent words
    model = models.Word2Vec(sentences, min_count=min_word_count, size=num_features,  window=context, sample=downsampling, workers = num_workers)
    
    model.save('initial_model')
    return model
    

import sys
paths = sys.argv[1]
mod = main(paths)
