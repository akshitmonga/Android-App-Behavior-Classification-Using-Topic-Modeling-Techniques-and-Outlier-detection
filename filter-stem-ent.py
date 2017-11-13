import nltk
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
cachedStopWords = stopwords.words("english");
def testFuncNew():
	txt=".txt"
        newfile="entertainment"
	newfile1="entertainmentfiltered"
	newfile2="entertainmentstemmed"
        for temp in range(0,60):
		target= open(newfile+`temp`+txt,"r")
		#with open(target) as f:
    		lines = target.readlines()
		for index in range(len(lines)):
			text = ' '.join([words for words in lines[index].split() if words not in cachedStopWords])
			target1 = open(newfile1+`temp`+txt,"a")
			#fp=open("filt.txt","a")
			target1.write(text)
			#target1.write("\n")
	        
                
	        	port = SnowballStemmer("english")
	        	text1 =  " ".join([port.stem(i) for i in text.split()])
			target2= open(newfile2+`temp`+txt,"a")                
			#fs=open("stem.txt","a")	        
	        	target2.write(text1)
	        	#fs.write("\n")
		target2.close()
		target1.close()
		target.close()

			
	
testFuncNew()

