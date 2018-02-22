from django.shortcuts import render
from decouple import config
import nltk
import tweepy
import sys
import requests
import textblob

c=0
arr2=[]
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

def namedEntity(n):
    words=nltk.word_tokenize(n)
    pos=nltk.pos_tag(words)
    name_entity=nltk.ne_chunk(pos,binary=True)
    chunk=[]
    flag=0
    for i in name_entity:
        if type(i)==nltk.tree.Tree:
            flag=1
            for tk,ps in i.leaves():
                s="".join(tk)
            chunk.append(s)
        elif flag==1:
            break
    if flag==0:
        return False
    s=" ".join(chunk)
    return s

class Stream_Listener(tweepy.StreamListener):
    def on_status(self,st):
        global c
        c+=1
        arr2.append(st.text.translate(non_bmp_map))
        if (c==20):
            return False
    def on_error(self,st):
        print(st)
        if status_code == 420:
            return False

def ans(n):
	ConsumerKey=config('ConsumerKey')
	ConsumerSecret=config('ConsumerSecret')
	AccessToken=config('AccessToken')
	AcessSecret=config('AcessSecret')

	oah=tweepy.OAuthHandler(ConsumerKey,ConsumerSecret)
	oah.set_access_token(AccessToken,AcessSecret)
	api=tweepy.API(oah)
	if (namedEntity(n)!=False):
	    url="https://newsapi.org/v2/everything?"
	    api_key="e583ae134b164c0186191bde2b75e7b8"
	    newsjson1=requests.get(url+"q="+str(n)+"&sources=bbc-news&language=en&apiKey="+api_key)
	    newsjson2=requests.get(url+"q="+str(n)+"&sources=fox-news&language=en&apiKey="+api_key)
	    newsjson3=requests.get(url+"q="+str(n)+"&language=en&apiKey="+api_key)
	    arr1,arr3,arr4=newsjson1.json()['articles'],newsjson2.json()['articles'],newsjson3.json()['articles']

	    TwitStream=tweepy.Stream(oah,Stream_Listener())
	    global c
	    while (c!=20):
	    	try:
	    		TwitStream.filter(track=n,languages=["en"])
	    	except:
	    		c=0
	    pos,neg,neu,positive,negative,neutral=[],[],[],0,0,0
	    for news in arr1:
	    	senti=textblob.TextBlob(news['title'].translate(non_bmp_map))
	    	if senti.sentiment.polarity>0:
	    		positive+=1
	    	elif senti.sentiment.polarity<0:
	    		negative+=1
	    	else:
	    		neutral+=1
	    total=positive+negative+neutral
	    if total==0:
	    	total=1
	    pos.append((positive*100)/total)
	    neg.append((negative*100)/total)
	    neu.append((neutral*100)/total)
	    positive,negative,neutral=0,0,0
	    for news in arr3:
	        senti=textblob.TextBlob(news['title'].translate(non_bmp_map))
	        if senti.sentiment.polarity>0:
	            positive+=1
	        elif senti.sentiment.polarity<0:
	            negative+=1
	        else:
	            neutral+=1
	    total=positive+negative+neutral
	    if total==0:
	    	total=1
	    pos.append((positive*100)/total)
	    neg.append((negative*100)/total)
	    neu.append((neutral*100)/total)
	    positive,negative,neutral=0,0,0
	    for news in arr4:
	        senti=textblob.TextBlob(news['title'].translate(non_bmp_map))
	        if senti.sentiment.polarity>0:
	            positive+=1
	        elif senti.sentiment.polarity<0:
	            negative+=1
	        else:
	            neutral+=1
	    total=positive+negative+neutral
	    if total==0:
	    	total=1
	    pos.append((positive*100)/total)
	    neg.append((negative*100)/total)
	    neu.append((neutral*100)/total)
	    positive,negative,neutral=0,0,0
	    for tweet in arr2:
	        senti=textblob.TextBlob(tweet.translate(non_bmp_map))
	        if senti.sentiment.polarity>0:
	            positive+=1
	        elif senti.sentiment.polarity<0:
	            negative+=1
	        else:
	            neutral+=1
	    total=positive+negative+neutral
	    if total==0:
	    	total=1
	    pos.append((positive*100)/total)
	    neg.append((negative*100)/total)
	    neu.append((neutral*100)/total)
	    positive,negative,neutral=0,0,0
	    tb=['',"Sentiment Analysis for "+n,'',"POSITIVE", str(pos[0])+r"% in BBC News", str(pos[1])+r"% in FOX News",str(pos[2])+r"% in Various News Sources",str(pos[3])+r"% in Tweets", "NEUTRAL",str(neu[0])+r"% in BBC News",str(neu[1])+r"% in FOX News",str(neu[2])+r"% in Various News Sources", str(neu[3])+r"% in Tweets","NEGATIVE",str(neg[0])+r"% in BBC News",str(neg[1])+r"% in FOX News", str(neg[2])+r"% in Various News Sources",str(neg[3])+r"% in Tweets"]
	    return tb
	else:
	    return(["Sorry not a named entity"])

def index(request):
	return render(request,'personal/home.html')

def search(request):
    if 'q' in request.GET:
    	message = ans(request.GET['q'])
    else:
        message = ['You submitted an empty form.']
    return render(request,'personal/basic.html',{'content':message})