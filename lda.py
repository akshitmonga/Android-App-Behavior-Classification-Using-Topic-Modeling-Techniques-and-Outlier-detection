import topics as tp
import gensim
import csv
import os
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
documents=[]
string=[]
arr=[]
cluster = [[] for i in range(11)]
kmeans = [[] for j in range(11)]
txt=".txt"
newfile="../crawling/APPLY-TOPIC-NAME/t_entertainment"
newfile1="../crawling/APPLY-TOPIC/entertainmentstemmed"

for temp in range(0,60):
#	print temp
	target= open(newfile1+`temp`+txt,"r")
	target1=target.read()
#	print target.readlines()
#	target1= open("tryldas/APPLY-TOPIC/entertainmentstemmed1.txt","r").read()
	documents.append(target1)
	def tokenize(text):
	    z =[token for token in gensim.utils.simple_preprocess(text) if token not in gensim.parsing.preprocessing.STOPWORDS]
	    return z

	#print "After the tokenizer, the previous document becomes:\n",tokenize(documents[0])
	processed_docs = [tokenize(doc) for doc in documents]
#	print processed_docs
	word_count_dict = gensim.corpora.Dictionary(processed_docs)
	#print "In the corpus there are", len(word_count_dict), "unique tokens"
	bag_of_words_corpus = [word_count_dict.doc2bow(pdoc) for pdoc in processed_docs]
	bow_doc1 = bag_of_words_corpus[0]
	
	#print "Bag of words representation of the first document (tuples are composed by token_id and multiplicity):\n", bow_doc1
	#print
	#for i in range(20):
	 #   print "In the document, topic_id {} (word \"{}\") appears {} time[s]".format(bow_doc1[i][0], word_count_dict[bow_doc1[i][0]], bow_doc1[i][1])
	#print "..."
	lda_model = gensim.models.LdaModel(bag_of_words_corpus, num_topics=2, id2word=word_count_dict, passes=200)
	_ = lda_model.print_topics(-1)
	
	for index, score in sorted(lda_model[bag_of_words_corpus[0]], key=lambda tup: -1*tup[1]):
	    #print "Topic: {}".format(score, lda_model.print_topic(index, 4))
	    vari=lda_model.print_topic(index, 2)
	    #print vari
	    t=open("abc.txt","w")
	    t.write(vari)
	    t.close()
	    import re
	    y=[]
	    t = open("abc.txt","r")
	    f=t.read()
	    x = re.findall("\d+.\d+",f)
            print x
	    y = re.findall("[a-z]*",f)
	    z = [z for z in y if z]
	    print z
	    for i in range(0,12):
	    	for j in range(0,2):
	   		try:
	    			print("array index {} {}".format(i,tp.topic_words[i].index(z[j])))
				#print z[j]
				kmeans[i].append(x[j])
				t1= open(newfile+`temp`+txt,"r")
				t2=t1.readlines()
				tempsave=t2
#				q = open("a.txt","a")
				#print t2
				if tempsave not in cluster[i]:
					cluster[i].append(t2)				
				t1.close()
			except Exception as e:
			        continue
	    
# 	    print x
#	    print z
	    #print vari
	del documents[:]
	target.close()

#print cluster

newfile="../crawling/APPLY-TOPIC-NAME/t_sports"
newfile1="../crawling/APPLY-TOPIC/sportsstemmed"

for temp in range(0,60):
#	print temp
	target= open(newfile1+`temp`+txt,"r")
	target1=target.read()
#	print target.readlines()
#	target1= open("tryldas/APPLY-TOPIC/entertainmentstemmed1.txt","r").read()
	documents.append(target1)
	def tokenize(text):
	    z =[token for token in gensim.utils.simple_preprocess(text) if token not in gensim.parsing.preprocessing.STOPWORDS]
	    return z

	#print "After the tokenizer, the previous document becomes:\n",tokenize(documents[0])
	processed_docs = [tokenize(doc) for doc in documents]
#	print processed_docs
	word_count_dict = gensim.corpora.Dictionary(processed_docs)
	#print "In the corpus there are", len(word_count_dict), "unique tokens"
	bag_of_words_corpus = [word_count_dict.doc2bow(pdoc) for pdoc in processed_docs]
	bow_doc1 = bag_of_words_corpus[0]
	
	#print "Bag of words representation of the first document (tuples are composed by token_id and multiplicity):\n", bow_doc1
	#print
	#for i in range(20):
	 #   print "In the document, topic_id {} (word \"{}\") appears {} time[s]".format(bow_doc1[i][0], word_count_dict[bow_doc1[i][0]], bow_doc1[i][1])
	#print "..."
	lda_model = gensim.models.LdaModel(bag_of_words_corpus, num_topics=2, id2word=word_count_dict, passes=200)
	_ = lda_model.print_topics(-1)
	
	for index, score in sorted(lda_model[bag_of_words_corpus[0]], key=lambda tup: -1*tup[1]):
#	    print "Topic: {}".format(score, lda_model.print_topic(index, 4))
	    vari=lda_model.print_topic(index, 2)
	    t=open("abc.txt","w")
	    t.write(vari)
	    t.close()
	    import re
	    y=[]
	    t = open("abc.txt","r")
	    f=t.read()
	    x = re.findall("\d+.\d+",f)
	    y = re.findall("[a-z]*",f)
	    z = [z for z in y if z]
	    for i in range(0,12):
	    	for j in range(0,2):
	   		try:
	    			print("array index {} {}".format(i,tp.topic_words[i].index(z[j])))
				kmeans[i].append(x[j])			
				t1= open(newfile+`temp`+txt,"r")
				t2=t1.readlines()
				tempsave=t2
			#	print t2
				if tempsave not in cluster[i]:
					cluster[i].append(t2)
				t1.close()
			except Exception as e:
			        continue
# 	    print x
#	    print z
	    #print vari
	del documents[:]
	target.close()

#print cluster

newfile="../crawling/APPLY-TOPIC-NAME/t_medical"
newfile1="../crawling/APPLY-TOPIC/medicalstemmed"

for temp in range(0,60):
#	print temp
	target= open(newfile1+`temp`+txt,"r")
	target1=target.read()
#	print target.readlines()
#	target1= open("tryldas/APPLY-TOPIC/entertainmentstemmed1.txt","r").read()
	documents.append(target1)
	def tokenize(text):
	    z =[token for token in gensim.utils.simple_preprocess(text) if token not in gensim.parsing.preprocessing.STOPWORDS]
	    return z

	#print "After the tokenizer, the previous document becomes:\n",tokenize(documents[0])
	processed_docs = [tokenize(doc) for doc in documents]
#	print processed_docs
	word_count_dict = gensim.corpora.Dictionary(processed_docs)
	#print "In the corpus there are", len(word_count_dict), "unique tokens"
	bag_of_words_corpus = [word_count_dict.doc2bow(pdoc) for pdoc in processed_docs]
	bow_doc1 = bag_of_words_corpus[0]
	
	#print "Bag of words representation of the first document (tuples are composed by token_id and multiplicity):\n", bow_doc1
	#print
	#for i in range(20):
	 #   print "In the document, topic_id {} (word \"{}\") appears {} time[s]".format(bow_doc1[i][0], word_count_dict[bow_doc1[i][0]], bow_doc1[i][1])
	#print "..."
	lda_model = gensim.models.LdaModel(bag_of_words_corpus, num_topics=2, id2word=word_count_dict, passes=200)
	_ = lda_model.print_topics(-1)
	
	for index, score in sorted(lda_model[bag_of_words_corpus[0]], key=lambda tup: -1*tup[1]):
#	    print "Topic: {}".format(score, lda_model.print_topic(index, 4))
	    vari=lda_model.print_topic(index, 2)
	    t=open("abc.txt","w")
	    t.write(vari)
	    t.close()
	    import re
	    y=[]
	    t = open("abc.txt","r")
	    f=t.read()
	    x = re.findall("\d+.\d+",f)
	    y = re.findall("[a-z]*",f)
	    z = [z for z in y if z]
	    for i in range(0,12):
	    	for j in range(0,2):
	   		try:
	    			print("array index {} {}".format(i,tp.topic_words[i].index(z[j])))
				kmeans[i].append(x[j])
				t1= open(newfile+`temp`+txt,"r")
				t2=t1.readlines()
				tempsave=t2
			#	print t2
				if tempsave not in cluster[i]:
					cluster[i].append(t2)
				t1.close()
			except Exception as e:
			        continue
# 	    print x
#	    print z
	    #print vari
	del documents[:]
	target.close()

#print cluster

newfile="../crawling/APPLY-TOPIC-NAME/t_news"
newfile1="../crawling/APPLY-TOPIC/newsstemmed"

for temp in range(0,60):
#	print temp
	target= open(newfile1+`temp`+txt,"r")
	target1=target.read()
#	print target.readlines()
#	target1= open("tryldas/APPLY-TOPIC/entertainmentstemmed1.txt","r").read()
	documents.append(target1)
	def tokenize(text):
	    z =[token for token in gensim.utils.simple_preprocess(text) if token not in gensim.parsing.preprocessing.STOPWORDS]
	    return z

	#print "After the tokenizer, the previous document becomes:\n",tokenize(documents[0])
	processed_docs = [tokenize(doc) for doc in documents]
#	print processed_docs
	word_count_dict = gensim.corpora.Dictionary(processed_docs)
	#print "In the corpus there are", len(word_count_dict), "unique tokens"
	bag_of_words_corpus = [word_count_dict.doc2bow(pdoc) for pdoc in processed_docs]
	bow_doc1 = bag_of_words_corpus[0]
	
	#print "Bag of words representation of the first document (tuples are composed by token_id and multiplicity):\n", bow_doc1
	#print
	#for i in range(20):
	 #   print "In the document, topic_id {} (word \"{}\") appears {} time[s]".format(bow_doc1[i][0], word_count_dict[bow_doc1[i][0]], bow_doc1[i][1])
	#print "..."
	lda_model = gensim.models.LdaModel(bag_of_words_corpus, num_topics=2, id2word=word_count_dict, passes=200)
	_ = lda_model.print_topics(-1)
	
	for index, score in sorted(lda_model[bag_of_words_corpus[0]], key=lambda tup: -1*tup[1]):
#	    print "Topic: {}".format(score, lda_model.print_topic(index, 4))
	    vari=lda_model.print_topic(index, 2)
	    t=open("abc.txt","w")
	    t.write(vari)
	    t.close()
	    import re
	    y=[]
	    t = open("abc.txt","r")
	    f=t.read()
	    x = re.findall("\d+.\d+",f)
	    y = re.findall("[a-z]*",f)
	    z = [z for z in y if z]
	    for i in range(0,12):
	    	for j in range(0,2):
	   		try:
	    			print("array index {} {}".format(i,tp.topic_words[i].index(z[j])))
				kmeans[i].append(x[j])				
				t1= open(newfile+`temp`+txt,"r")
				t2=t1.readlines()
				tempsave=t2
			#	print t2
				if tempsave not in cluster[i]:
					cluster[i].append(t2)
				t1.close()
			except Exception as e:
			        continue
# 	    print x
#	    print z
	    #print vari
	del documents[:]
	target.close()

#print cluster

newfile="../crawling/APPLY-TOPIC-NAME/t_weather"
newfile1="../crawling/APPLY-TOPIC/weatherstemmed"

for temp in range(0,60):
#	print temp
	target= open(newfile1+`temp`+txt,"r")
	target1=target.read()
#	print target.readlines()
#	target1= open("tryldas/APPLY-TOPIC/entertainmentstemmed1.txt","r").read()
	documents.append(target1)
	def tokenize(text):
	    z =[token for token in gensim.utils.simple_preprocess(text) if token not in gensim.parsing.preprocessing.STOPWORDS]
	    return z

	#print "After the tokenizer, the previous document becomes:\n",tokenize(documents[0])
	processed_docs = [tokenize(doc) for doc in documents]
#	print processed_docs
	word_count_dict = gensim.corpora.Dictionary(processed_docs)
	#print "In the corpus there are", len(word_count_dict), "unique tokens"
	bag_of_words_corpus = [word_count_dict.doc2bow(pdoc) for pdoc in processed_docs]
	bow_doc1 = bag_of_words_corpus[0]
	
	#print "Bag of words representation of the first document (tuples are composed by token_id and multiplicity):\n", bow_doc1
	#print
	#for i in range(20):
	 #   print "In the document, topic_id {} (word \"{}\") appears {} time[s]".format(bow_doc1[i][0], word_count_dict[bow_doc1[i][0]], bow_doc1[i][1])
	#print "..."
	lda_model = gensim.models.LdaModel(bag_of_words_corpus, num_topics=2, id2word=word_count_dict, passes=200)
	_ = lda_model.print_topics(-1)
	
	for index, score in sorted(lda_model[bag_of_words_corpus[0]], key=lambda tup: -1*tup[1]):
#	    print "Topic: {}".format(score, lda_model.print_topic(index, 4))
	    vari=lda_model.print_topic(index, 2)
	    t=open("abc.txt","w")
	    t.write(vari)
	    t.close()
	    import re
	    y=[]
	    t = open("abc.txt","r")
	    f=t.read()
	    x = re.findall("\d+.\d+",f)
	    y = re.findall("[a-z]*",f)
	    z = [z for z in y if z]
	    for i in range(0,12):
	    	for j in range(0,2):
	   		try:
	    			print("array index {} {}".format(i,tp.topic_words[i].index(z[j])))
				kmeans[i].append(x[j])				
				t1= open(newfile+`temp`+txt,"r")
				t2=t1.readlines()
				tempsave=t2
			#	print t2
				if tempsave not in cluster[i]:
					cluster[i].append(t2)
				t1.close()
			except Exception as e:
			        continue
# 	    print x
#	    print z
	    #print vari
	del documents[:]
	target.close()

#print cluster
newfile="../crawling/APPLY-TOPIC-NAME/t_music"
newfile1="../crawling/APPLY-TOPIC/musicstemmed"

for temp in range(0,60):
#	print temp
	target= open(newfile1+`temp`+txt,"r")
	target1=target.read()
#	print target.readlines()
#	target1= open("tryldas/APPLY-TOPIC/entertainmentstemmed1.txt","r").read()
	documents.append(target1)
	def tokenize(text):
	    z =[token for token in gensim.utils.simple_preprocess(text) if token not in gensim.parsing.preprocessing.STOPWORDS]
	    return z

	#print "After the tokenizer, the previous document becomes:\n",tokenize(documents[0])
	processed_docs = [tokenize(doc) for doc in documents]
#	print processed_docs
	word_count_dict = gensim.corpora.Dictionary(processed_docs)
	#print "In the corpus there are", len(word_count_dict), "unique tokens"
	bag_of_words_corpus = [word_count_dict.doc2bow(pdoc) for pdoc in processed_docs]
	bow_doc1 = bag_of_words_corpus[0]
	
	#print "Bag of words representation of the first document (tuples are composed by token_id and multiplicity):\n", bow_doc1
	#print
	#for i in range(20):
	 #   print "In the document, topic_id {} (word \"{}\") appears {} time[s]".format(bow_doc1[i][0], word_count_dict[bow_doc1[i][0]], bow_doc1[i][1])
	#print "..."
	lda_model = gensim.models.LdaModel(bag_of_words_corpus, num_topics=2, id2word=word_count_dict, passes=200)
	_ = lda_model.print_topics(-1)
	
	for index, score in sorted(lda_model[bag_of_words_corpus[0]], key=lambda tup: -1*tup[1]):
#	    print "Topic: {}".format(score, lda_model.print_topic(index, 4))
	    vari=lda_model.print_topic(index, 2)
	    t=open("abc.txt","w")
	    t.write(vari)
	    t.close()
	    import re
	    y=[]
	    t = open("abc.txt","r")
	    f=t.read()
	    x = re.findall("\d+.\d+",f)
	    y = re.findall("[a-z]*",f)
	    z = [z for z in y if z]
	    for i in range(0,12):
	    	for j in range(0,2):
	   		try:
	    			print("array index {} {}".format(i,tp.topic_words[i].index(z[j])))
				kmeans[i].append(x[j])
				t1= open(newfile+`temp`+txt,"r")
				t2=t1.readlines()
				tempsave=t2
			#	print t2
				if tempsave not in cluster[i]:
					cluster[i].append(t2)
				t1.close()
			except Exception as e:
			        continue
# 	    print x
#	    print z
	    #print vari
	del documents[:]
	target.close()

#print cluster
newfile="../crawling/APPLY-TOPIC-NAME/t_shopping"
newfile1="../crawling/APPLY-TOPIC/shoppingstemmed"

for temp in range(0,60):
#	print temp
	target= open(newfile1+`temp`+txt,"r")
	target1=target.read()
#	print target.readlines()
#	target1= open("tryldas/APPLY-TOPIC/entertainmentstemmed1.txt","r").read()
	documents.append(target1)
	def tokenize(text):
	    z =[token for token in gensim.utils.simple_preprocess(text) if token not in gensim.parsing.preprocessing.STOPWORDS]
	    return z

	#print "After the tokenizer, the previous document becomes:\n",tokenize(documents[0])
	processed_docs = [tokenize(doc) for doc in documents]
#	print processed_docs
	word_count_dict = gensim.corpora.Dictionary(processed_docs)
	#print "In the corpus there are", len(word_count_dict), "unique tokens"
	bag_of_words_corpus = [word_count_dict.doc2bow(pdoc) for pdoc in processed_docs]
	bow_doc1 = bag_of_words_corpus[0]
	
	#print "Bag of words representation of the first document (tuples are composed by token_id and multiplicity):\n", bow_doc1
	#print
	#for i in range(20):
	 #   print "In the document, topic_id {} (word \"{}\") appears {} time[s]".format(bow_doc1[i][0], word_count_dict[bow_doc1[i][0]], bow_doc1[i][1])
	#print "..."
	lda_model = gensim.models.LdaModel(bag_of_words_corpus, num_topics=2, id2word=word_count_dict, passes=200)
	_ = lda_model.print_topics(-1)
	
	for index, score in sorted(lda_model[bag_of_words_corpus[0]], key=lambda tup: -1*tup[1]):
#	    print "Topic: {}".format(score, lda_model.print_topic(index, 4))
	    vari=lda_model.print_topic(index, 2)
	    t=open("abc.txt","w")
	    t.write(vari)
	    t.close()
	    import re
	    y=[]
	    t = open("abc.txt","r")
	    f=t.read()
	    x = re.findall("\d+.\d+",f)
	    y = re.findall("[a-z]*",f)
	    z = [z for z in y if z]
	    for i in range(0,12):
	    	for j in range(0,2):
	   		try:
	    			print("array index {} {}".format(i,tp.topic_words[i].index(z[j])))
				kmeans[i].append(x[j])
				t1= open(newfile+`temp`+txt,"r")
				t2=t1.readlines()
				tempsave=t2
			#	print t2
				if tempsave not in cluster[i]:
					cluster[i].append(t2)
				t1.close()
			except Exception as e:
			        continue
# 	    print x
#	    print z
	    #print vari
	del documents[:]
	target.close()

#print cluster

newfile="../crawling/APPLY-TOPIC-NAME/t_social"
newfile1="../crawling/APPLY-TOPIC/socialstemmed"

for temp in range(0,60):
#	print temp
	target= open(newfile1+`temp`+txt,"r")
	target1=target.read()
#	print target.readlines()
#	target1= open("tryldas/APPLY-TOPIC/entertainmentstemmed1.txt","r").read()
	documents.append(target1)
	def tokenize(text):
	    z =[token for token in gensim.utils.simple_preprocess(text) if token not in gensim.parsing.preprocessing.STOPWORDS]
	    return z

	#print "After the tokenizer, the previous document becomes:\n",tokenize(documents[0])
	processed_docs = [tokenize(doc) for doc in documents]
#	print processed_docs
	word_count_dict = gensim.corpora.Dictionary(processed_docs)
	#print "In the corpus there are", len(word_count_dict), "unique tokens"
	bag_of_words_corpus = [word_count_dict.doc2bow(pdoc) for pdoc in processed_docs]
	bow_doc1 = bag_of_words_corpus[0]
	
	#print "Bag of words representation of the first document (tuples are composed by token_id and multiplicity):\n", bow_doc1
	#print
	#for i in range(20):
	 #   print "In the document, topic_id {} (word \"{}\") appears {} time[s]".format(bow_doc1[i][0], word_count_dict[bow_doc1[i][0]], bow_doc1[i][1])
	#print "..."
	lda_model = gensim.models.LdaModel(bag_of_words_corpus, num_topics=2, id2word=word_count_dict, passes=200)
	_ = lda_model.print_topics(-1)
	
	for index, score in sorted(lda_model[bag_of_words_corpus[0]], key=lambda tup: -1*tup[1]):
#	    print "Topic: {}".format(score, lda_model.print_topic(index, 4))
	    vari=lda_model.print_topic(index, 2)
	    t=open("abc.txt","w")
	    t.write(vari)
	    t.close()
	    import re
	    y=[]
	    t = open("abc.txt","r")
	    f=t.read()
	    x = re.findall("\d+.\d+",f)
	    y = re.findall("[a-z]*",f)
	    z = [z for z in y if z]
	    for i in range(0,12):
	    	for j in range(0,2):
	   		try:
	    			print("array index {} {}".format(i,tp.topic_words[i].index(z[j])))
				kmeans[i].append(x[j])
				t1= open(newfile+`temp`+txt,"r")
				t2=t1.readlines()
				tempsave=t2
			#	print t2
				if tempsave not in cluster[i]:
					cluster[i].append(t2)
				t1.close()
			except Exception as e:
			        continue
# 	    print x
#	    print z
	    #print vari
	del documents[:]
	target.close()


newfile="../crawling/APPLY-TOPIC-NAME/t_health"
newfile1="../crawling/APPLY-TOPIC/healthstemmed"

for temp in range(0,60):
#	print temp
	target= open(newfile1+`temp`+txt,"r")
	target1=target.read()
#	print target.readlines()
#	target1= open("tryldas/APPLY-TOPIC/entertainmentstemmed1.txt","r").read()
	documents.append(target1)
	def tokenize(text):
	    z =[token for token in gensim.utils.simple_preprocess(text) if token not in gensim.parsing.preprocessing.STOPWORDS]
	    return z

	#print "After the tokenizer, the previous document becomes:\n",tokenize(documents[0])
	processed_docs = [tokenize(doc) for doc in documents]
#	print processed_docs
	word_count_dict = gensim.corpora.Dictionary(processed_docs)
	#print "In the corpus there are", len(word_count_dict), "unique tokens"
	bag_of_words_corpus = [word_count_dict.doc2bow(pdoc) for pdoc in processed_docs]
	bow_doc1 = bag_of_words_corpus[0]
	
	#print "Bag of words representation of the first document (tuples are composed by token_id and multiplicity):\n", bow_doc1
	#print
	#for i in range(20):
	 #   print "In the document, topic_id {} (word \"{}\") appears {} time[s]".format(bow_doc1[i][0], word_count_dict[bow_doc1[i][0]], bow_doc1[i][1])
	#print "..."
	lda_model = gensim.models.LdaModel(bag_of_words_corpus, num_topics=2, id2word=word_count_dict, passes=200)
	_ = lda_model.print_topics(-1)
	
	for index, score in sorted(lda_model[bag_of_words_corpus[0]], key=lambda tup: -1*tup[1]):
#	    print "Topic: {}".format(score, lda_model.print_topic(index, 4))
	    vari=lda_model.print_topic(index,2)
	    t=open("abc.txt","w")
	    t.write(vari)
	    t.close()
	    import re
	    y=[]
	    t = open("abc.txt","r")
	    f=t.read()
	    x = re.findall("\d+.\d+",f)
	    y = re.findall("[a-z]*",f)
	    z = [z for z in y if z]
	    for i in range(0,12):
	    	for j in range(0,2):
	   		try:
	    			print("array index {} {}".format(i,tp.topic_words[i].index(z[j])))	
				kmeans[i].append(x[j])
				t1= open(newfile+`temp`+txt,"r")
				t2=t1.readlines()
				tempsave=t2
			#	print t2
				if tempsave not in cluster[i]:
					cluster[i].append(t2)
				t1.close()
			except Exception as e:
			        continue
# 	    print x
#	    print z
	    #print vari
	del documents[:]
	target.close()


newfile="../crawling/APPLY-TOPIC-NAME/t_lifestyle"
newfile1="../crawling/APPLY-TOPIC/lifestylestemmed"

for temp in range(0,60):
#	print temp
	target= open(newfile1+`temp`+txt,"r")
	target1=target.read()
#	print target.readlines()
#	target1= open("tryldas/APPLY-TOPIC/entertainmentstemmed1.txt","r").read()
	documents.append(target1)
	def tokenize(text):
	    z =[token for token in gensim.utils.simple_preprocess(text) if token not in gensim.parsing.preprocessing.STOPWORDS]
	    return z

	#print "After the tokenizer, the previous document becomes:\n",tokenize(documents[0])
	processed_docs = [tokenize(doc) for doc in documents]
#	print processed_docs
	word_count_dict = gensim.corpora.Dictionary(processed_docs)
	#print "In the corpus there are", len(word_count_dict), "unique tokens"
	bag_of_words_corpus = [word_count_dict.doc2bow(pdoc) for pdoc in processed_docs]
	bow_doc1 = bag_of_words_corpus[0]
	
	#print "Bag of words representation of the first document (tuples are composed by token_id and multiplicity):\n", bow_doc1
	#print
	#for i in range(20):
	 #   print "In the document, topic_id {} (word \"{}\") appears {} time[s]".format(bow_doc1[i][0], word_count_dict[bow_doc1[i][0]], bow_doc1[i][1])
	#print "..."
	lda_model = gensim.models.LdaModel(bag_of_words_corpus, num_topics=2, id2word=word_count_dict, passes=200)
	_ = lda_model.print_topics(-1)
	
	for index, score in sorted(lda_model[bag_of_words_corpus[0]], key=lambda tup: -1*tup[1]):
#	    print "Topic: {}".format(score, lda_model.print_topic(index, 4))
	    vari=lda_model.print_topic(index, 2)
	    t=open("abc.txt","w")
	    t.write(vari)
	    t.close()
	    import re
	    y=[]
	    t = open("abc.txt","r")
	    f=t.read()
	    x = re.findall("\d+.\d+",f)
	    y = re.findall("[a-z]*",f)
	    z = [z for z in y if z]
	    for i in range(0,12):
	    	for j in range(0,2):
	   		try:
	    			print("array index {} {}".format(i,tp.topic_words[i].index(z[j])))
				kmeans[i].append(x[j])
				t1= open(newfile+`temp`+txt,"r")
				t2=t1.readlines()
				tempsave=t2
			#	print t2
				if tempsave not in cluster[i]:
					cluster[i].append(t2)
				t1.close()
			except Exception as e:
			        continue
# 	    print x
#	    print z
	    #print vari
	del documents[:]
	target.close()






#print cluster
print cluster
print "\n"

print kmeans
with open("output.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(kmeans)
target5= open("info1.txt","a")

for list in cluster:
	for sap in list:
		for s in sap:
			s=s.rstrip()	
			target5.write(s + "\t")
			"""target5.write("(")
			target5.write(c)
			target5.write(")")"""
	target5.write("\n")
	target5.write("\n")
	"""target5.write("-------------------------------------------------------------------------------------------")
	target5.write("\n")"""


target5.close()

target6= open("info.txt","w")
for list in tp.topic_words:
	for sap in list:	
		target6.write(sap + "\t")
	target6.write("\n")
	target6.write("\n")
	


target6.close()
