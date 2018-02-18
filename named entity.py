import nltk
import pymongo
import sys
import collections

def addNamedEntities(data,named_entities_found):
    chunk=[]
    for i in data:
        if type(i)==nltk.tree.Tree:
            for tk,ps in i.leaves():
                s="".join(tk)
            chunk.append(s)
        elif len(chunk)>0:
            s=" ".join(chunk)
            if s[0:2]=="RT":
                s=s[3:]
            if s!="":
                try:
                    named_entities_found[s.lower()]+=1
                except:
                    named_entities_found[s.lower()]=1
            chunk=[]

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
mongo="mongodb://localhost/sampleTweet"
dbase=pymongo.MongoClient(mongo).sampleTweet

all_tweets=dbase['tweets'].find()
named_entities_found={}

for tweet in all_tweets:
    words=nltk.word_tokenize(tweet['text'].translate(non_bmp_map))
    pos=nltk.pos_tag(words)
    namedEntity=nltk.ne_chunk(pos,binary=True)
    addNamedEntities(namedEntity,named_entities_found)

print("The 15 most frequently occurring named-entities are: ")
tb=dict(collections.Counter(named_entities_found).most_common(15))
keys=tb.keys()
j=1
for i in keys:
    if j<10:
        print(str(j)+'.   '+i+(' '*(20-len(i)))+':  '+str(tb[i])+" times")
    else:
        print(str(j)+'.  '+i+(' '*(20-len(i)))+':  '+str(tb[i])+" times")
    j+=1
