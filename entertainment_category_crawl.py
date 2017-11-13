import urllib2
from urllib2 import Request
import re

def trade_spider():
	temp=0
	#url = 'https://play.google.com/store/apps/details?id=com.sm.SlingGuide.Dish&hl=en'
	#url = 'https://play.google.com/store/apps/details?id=in.startv.hotstar&hl=en'
	url = 'https://play.google.com/store/apps/category/ENTERTAINMENT/collection/topselling_free?hl=en'
	req = Request(url)
	resp = urllib2.urlopen(req)
	newfile="entertainment"
	newfile1="t_entertainment"
	txt=".txt"
	respData = resp.read()
	#print(respData)
	link1 =  re.findall(r'<a class="title".*?>',str(respData))
	#print(link1)
        for link in link1:
		#target= open(newfile+`temp`+txt,"a")
		#target1= open(newfile1+`temp`+txt,"a")
		target= open(newfile+`temp`+txt,"a")
		target1= open(newfile1+`temp`+txt,"a")
		r = re.compile('(?<=href=").*?(?=")')
		li = r.findall(link)
		href ="https://play.google.com" + ',' .join(li) 
		req1 = Request(href)
		resp1 = urllib2.urlopen(req1)
		respData1 = resp1.read()
		#print(respData1)
		titles = re.findall(r'<a class="title".*?>(.*?)',str(respData))
		#print(titles)
		for eac in titles:
			count=0
			r = re.compile('(?<=title=").*?(?=")')
			li = r.findall(link)
		#	print(eac)
			target1.write('titles[0] '.join(li))
			count+=1;
			if(count==1):
				break;
		paragraph = re.findall(r'<div jsname="C4s9Ed">(.*?)</div>',str(respData1))
		for eachP in paragraph:
			line=re.sub('<[^>]*>', '', eachP)
			#print(line)			
			target.write(line)
		temp+=1
		target.close()
		target1.close()
trade_spider()
