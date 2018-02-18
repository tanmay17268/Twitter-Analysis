import requests
import pymongo

mongo="mongodb://localhost/sampleTweet"
url="https://newsapi.org/v2/everything?"
api_key="f011dd3c46f641e9b8b4adaf5d0812ce"
named_entities=["Army","Trump","Florida","America","Asian"]

dbase=pymongo.MongoClient(mongo).sampleTweet

for i in range(5):
    newsjson=requests.get(url+"q="+named_entities[i]+"&sources=bbc-news&language=en&apiKey="+api_key)
    for j in newsjson.json()['articles']:
        if i==0:
            dbase.Army_BBCnews.insert(j)
        elif i==1:
            dbase.Trump_BBCnews.insert(j)
        elif i==2:
            dbase.Florida_BBCnews.insert(j)
        elif i==3:
            dbase.America_BBCnews.insert(j)
        elif i==4:
            dbase.Asian_BBCnews.insert(j)
        else:
            dbase.error_in_code.insert(j)
print("News articles from BBC news, successfully collected")

for i in range(5):
    newsjson=requests.get(url+"q="+named_entities[i]+"&sources=fox-news&language=en&apiKey="+api_key)
    for j in newsjson.json()['articles']:
        if i==0:
            dbase.Army_FOXnews.insert(j)
        elif i==1:
            dbase.Trump_FOXnews.insert(j)
        elif i==2:
            dbase.Florida_FOXnews.insert(j)
        elif i==3:
            dbase.America_FOXnews.insert(j)
        elif i==4:
            dbase.Asian_FOXnews.insert(j)
        else:
            dbase.error_in_code.insert(j)
print("News articles from FOX news, successfully collected")

for i in range(5):
    newsjson=requests.get(url+"q="+named_entities[i]+"&language=en&apiKey="+api_key)
    for j in newsjson.json()['articles']:
        if i==0:
            dbase.Army_news.insert(j)
        elif i==1:
            dbase.Trump_news.insert(j)
        elif i==2:
            dbase.Florida_news.insert(j)
        elif i==3:
            dbase.America_news.insert(j)
        elif i==4:
            dbase.Asian_news.insert(j)
        else:
            dbase.error_in_code.insert(j)
print("News articles from various news sources, successfully collected")
