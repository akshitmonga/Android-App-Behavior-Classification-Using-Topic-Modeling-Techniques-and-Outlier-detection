import os
import numpy as np
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import sklearn.feature_extraction.text as text
from sklearn import decomposition

#CORPUS_PATH =os.path.join('tryldas','APPLY-TOPIC')
CORPUS_PATH =os.path.join('../crawling','APPLY-TOPIC')

filenames = sorted([os.path.join(CORPUS_PATH, fn) for fn in os.listdir(CORPUS_PATH)])

#print len(filenames)
#print filenames[:5]


vectorizer = text.CountVectorizer(input='filename', stop_words='english', min_df=20)

dtm = vectorizer.fit_transform(filenames).toarray()

vocab = np.array(vectorizer.get_feature_names())

print dtm.shape
print len(vocab)
print vocab

num_topics = 11

num_top_words = 10

clf = decomposition.NMF(n_components=num_topics, random_state=1)

doctopic = clf.fit_transform(dtm)

topic_words = []
print clf.components_
for topic in clf.components_:
     word_idx = np.argsort(topic)[::-1][0:num_top_words]
     topic_words.append([vocab[i] for i in word_idx])

print topic_words
"""newfile = "info"
txt = ".txt"
for temp in range(0,11):
	file1=open(newfile+`temp`+txt,"w")
	for item in topic_words[temp]:
  		#print>>file1, item
		file1.write(item);
		file1.write(" ");  		
		#print>>file1	
	file1.close()"""
file1=open("info.txt","w")
for temp in range(0,11):
	for item in topic_words[temp]:
  		file1.write(item)
  		file1.write(" ")
	file1.write("\n")
	file1.write("\n")
	file1.write("\n")	
file1.close()
