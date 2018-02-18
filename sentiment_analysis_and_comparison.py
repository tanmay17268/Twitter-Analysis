import textblob
import pymongo
import sys

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
mongo="mongodb://localhost/sampleTweet"
dbase=pymongo.MongoClient(mongo).sampleTweet
collections=['America_BBCnews','America_FOXnews','America_news','America_twitter','Army_BBCnews','Army_FOXnews','Army_news','Army_twitter','Asian_BBCnews','Asian_FOXnews','Asian_news','Asian_twitter','Florida_BBCnews','Florida_FOXnews','Florida_news','Florida_twitter','Trump_BBCnews','Trump_FOXnews','Trump_news','Trump_twitter']
namedEntity=['America','Army','Asian','Florida','Trump']
pos=[]
neg=[]
neu=[]

for i in range(20):
    all_tweets=dbase[collections[i]].find()
    positive=0
    negative=0
    neutral=0
    for tweet in all_tweets:
        if i==3 or i==7 or i==11 or i==15 or i==19:
            senti=textblob.TextBlob(tweet['text'].translate(non_bmp_map))
        else:
            senti=textblob.TextBlob(tweet['title'].translate(non_bmp_map))
        if senti.sentiment.polarity>0:
            positive+=1
        elif senti.sentiment.polarity<0:
            negative+=1
        else:
            neutral+=1

    if i==3 or i==7 or i==11 or i==15 or i==19:
        pos.append(positive/10)
        neg.append(negative/10)
        neu.append(neutral/10)
    else:
        pos.append(positive*5)
        neg.append(negative*5)
        neu.append(neutral*5)
        
    if ((i+1)%4==0):
        print()
        print("Sentiment Analysis for "+namedEntity[((i+1)//4)-1])
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
        pos=[]
        neg=[]
        neu=[]

print()
print("Looking at how does TextBlob perform sentiment analysis")
print("_______________________________________________________")
print()
print("TextBlob creates a probability distribution table, on the basis of every adjective it parses and thus uses it to conclude whether the sentence is positive, neutral or negative.\nTwo ID's are created for every word present in a setence, which are identified from the Dutch database and the English language lexical database ID. Then those are used to retreive the polarity, subjectivity and intensity of every adjective. \nThus These keywords form the basis of the probability distribution table.")
