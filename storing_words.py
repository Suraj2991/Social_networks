from gensim import models
import numpy as np
from sklearn.cluster import SpectralClustering, KMeans, MiniBatchKMeans


def get_array(word, mods): 
	feat_arrays = np.zeros(np.shape(mods.syn0))
	i = 0
	for w in word:
		feat_arrays[i] = mods[w]
		i = i+1
	return feat_arrays
		
		
word_mod = models.Word2Vec.load('initial_model')

words = word_mod.index2word

features_word = get_array(words, word_mod)

unsuper_mod = MiniBatchKMeans(n_clusters = 40, max_iter = 400, batch_size = 100, verbose = 20)
clusts = unsuper_mod.fit_predict(features_word)



