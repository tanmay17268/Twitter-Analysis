import tweepy
import pymongo
import json

mongo="mongodb://localhost/sampleTweet"
ConsumerKey="PUT_YOUR_CONSUMER_KEY_BEFORE_EXECUTING_THE_CODE"
ConsumerSecret="PUT_YOUR_CONSUMER_SECRET_BEFORE_EXECUTING_THE_CODE"
AccessToken="PUT_YOUR_ACCESS_TOKEN_BEFORE_EXECUTING_THE_CODE"
AcessSecret="PUT_YOUR_ACESS_SECRET_BEFORE_EXECUTING_THE_CODE"
named_entities=[["Army","ARMY"],["Trump","trump"],["Florida","florida"],["America","america"],["Asian","asian"]]

oah=tweepy.OAuthHandler(ConsumerKey,ConsumerSecret)
oah.set_access_token(AccessToken,AcessSecret)
api=tweepy.API(oah)
c=0

class Stream_Listener(tweepy.StreamListener):
    def on_data(self,dt):
        global c
        c+=1
        data=json.loads(dt)
        dbase=pymongo.MongoClient(mongo).sampleTweet
        if i==0:
            dbase.Army_twitter.insert(data)
        elif i==1:
            dbase.Trump_twitter.insert(data)
        elif i==2:
            dbase.Florida_twitter.insert(data)
        elif i==3:
            dbase.America_twitter.insert(data)
        elif i==4:
            dbase.Asian_twitter.insert(data)
        else:
            dbase.error_in_code.insert(data)        
        if (c==1000):
            c=0
            return False
    
    def on_error(self,st):
        print(st)
        if status_code == 420:
            return False

for i in range(5):
    TwitStream=tweepy.Stream(oah,Stream_Listener())
    TwitStream.filter(track=named_entities[i],languages=["en"])

print("Tweets successfully stored in MongoDB")
