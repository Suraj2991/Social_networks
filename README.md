# Social_networks

############################################################################################
wordV.py should be given a path containing News Articles.

News Articles can have sub directories.

The program builds a word2vec model using gensim and stores the model which can then be loaded and used for different purposes.

python wordV.py /home/dir1/news_articlesDir

############################################################################################
reu.py extracts news articles from reuters and stores them in a directory.

Need to manually change the directory and the dates or months

############################################################################################
Make sure to enter the paths for models correctly

run_server.py 

Basically starts the server and loads models.

Go to  http://127.0.0.1:5000/<word_name>

<word-name> has to be one word, that you want to see the trend for

eg.  http://127.0.0.1:5000/facebook

returns the following (in the shell not the browser) in descending order of variance (most var to least var)


WORD      Similarities                                  Variance


whatsapp [0, 0.68031680470201683, 0.65515409261211066] 0.0991878891007


koum [0, 0.50260311272791813, 0.51839855751038155] 0.0579551610476


messenger [0.11240806847373981, 0.61597852082880744, 0.59514625711821534] 0.0541170380525


roadshow [0.59143326394392515, 0.14669283780219497, 0.15138273893393561] 0.0434956118199


ipo [0.72459798009968768, 0.34316219411605603, 0.37451608967086991] 0.0298926284002


debut [0.59953685406553181, 0.28558358970423769, 0.26094980114026006] 0.0237571853501


zynga [0.68003027275442829, 0.41712405995273116, 0.38700121198077864] 0.0173214547953


page [0.30186777518547958, 0.55550533958782067, 0.54154011399952107] 0.0135522079549


twitter [0.42348236633653874, 0.68079996797786757, 0.64812583947067048] 0.0130827374233


advertising [0.58768494947112637, 0.41320528815771496, 0.36837260794011489] 0.00895011384171


messaging [0.36583175192781292, 0.5300345509490314, 0.53092774966386225] 0.00602444949765


networking [0.67233084161014967, 0.52360643159850639, 0.51637181377507579] 0.00516605646574


fb [0.40806316339016407, 0.55250850905267856, 0.53262295593180187] 0.00408611500272


yelp [0.58251301309610892, 0.44693984759444327, 0.44885870089894447] 0.00402747115234


zuckerberg [0.63624908564540561, 0.52094064778041238, 0.50918847916682064] 0.00328650522541


linkedin [0.58937549696981129, 0.52218088908630322, 0.49307000618398539] 0.00162636737639


user [0.50253064131121783, 0.54510989934554244, 0.55535178537151098] 0.000523106967107


google [0.49381869598341666, 0.5361672151532948, 0.50138673486133334] 0.000340039344187


users [0.57208762434336224, 0.55081086439577787, 0.52734963435864701] 0.000333846397399


instagram [0.5791267100369607, 0.61387133606276645, 0.58725380590615572] 0.000220192404064


############################################################################################

Use this for word2vec model
https://drive.google.com/folderview?id=0B2D0gE0DfdUHfmcyaEo3UTJ3U1FWTTM5dC1WeF9xYXNWRmZ5MTlHQW9VdVI4U0h3aHltaWc&usp=sharing


