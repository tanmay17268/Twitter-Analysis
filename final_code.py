import nltk
import tweepy
import sys
import requests
import textblob
import matplotlib.pyplot as plt
import numpy as np

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

ConsumerKey="PUT_YOUR_CONSUMER_KEY_HERE"
ConsumerSecret="PUT_YOUR_CONSUMER_SECRET_HERE"
AccessToken="PUT_YOUR_ACCESS_TOKEN_HERE"
AcessSecret="PUT_YOUR_ACESS_SECRET_KEY_HERE"

oah=tweepy.OAuthHandler(ConsumerKey,ConsumerSecret)
oah.set_access_token(AccessToken,AcessSecret)
api=tweepy.API(oah)
c=0
arr2=[]

def news(n):
    url="https://newsapi.org/v2/everything?"
    api_key="f011dd3c46f641e9b8b4adaf5d0812ce"
    newsjson1=requests.get(url+"q="+str(n)+"&sources=bbc-news&language=en&apiKey="+api_key)
    newsjson2=requests.get(url+"q="+str(n)+"&sources=fox-news&language=en&apiKey="+api_key)
    newsjson3=requests.get(url+"q="+str(n)+"&language=en&apiKey="+api_key)
    return newsjson1.json()['articles'],newsjson2.json()['articles'],newsjson3.json()['articles']

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
        if (c==100):
            return False
    def on_error(self,st):
        print(st)
        if status_code == 420:
            return False
n=input("Enter a named Entity: ")
if (namedEntity(n)!=False):
    arr1,arr3,arr4=news(n)
    TwitStream=tweepy.Stream(oah,Stream_Listener())
    while (c!=100):
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
    pos.append(positive)
    neg.append(negative)
    neu.append(neutral)
    positive,negative,neutral=0,0,0
    print()
    print("Sentiment Analysis for "+n)
    print()
    print("POSITIVE")
    print(str(pos[0])+"% in BCC News")
    print(str(pos[1])+"% in FOX News")
    print(str(pos[2])+"% in Various News Sources")
    print(str(pos[3])+"% in Tweets")
    print("NEUTRAL")
    print(str(neu[0])+"% in BCC News")
    print(str(neu[1])+"% in FOX News")
    print(str(neu[2])+"% in Various News Sources")
    print(str(neu[3])+"% in Tweets")
    print("NEGATIVE")
    print(str(neg[0])+"% in BCC News")
    print(str(neg[1])+"% in FOX News")
    print(str(neg[2])+"% in Various News Sources")
    print(str(neg[3])+"% in Tweets")
    print()
    figure,axis=plt.subplots()
    ind=np.arange(3)
    rect1=plt.bar(ind,[pos[0],neu[0],neg[0]],0.15,alpha=0.6,color='r',label='BBC News')
    rect2=plt.bar(ind+0.15,[pos[1],neu[1],neg[1]],0.15,alpha=0.6,color='b',label='FOX News')
    rect3=plt.bar(ind+0.3,[pos[2],neu[2],neg[2]],0.15,alpha=0.6,color='g',label='Various News sources')
    rect4=plt.bar(ind+0.45,[pos[3],neu[3],neg[3]],0.15,alpha=0.6,color='y',label='Twitter')
    plt.xlabel('SENTIMENT',fontsize=15)
    plt.ylabel('No. of articles(%)',fontsize=15)
    plt.title("Sentiment Analysis for "+n)
    plt.xticks(ind+0.3,('Positive','Neutral','Negative'))
    plt.legend()
    plt.tight_layout()
    plt.show()
else:
    print("Sorry not a named entity")
