import pymongo
import sys

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
mongo="mongodb://localhost/sampleTweet"
dbase=pymongo.MongoClient(mongo).sampleTweet

all_tweets=dbase['tweets'].find()

for tweet in all_tweets:
    print(tweet['text'].translate(non_bmp_map))
    print()
