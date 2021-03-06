import tweepy
import sys

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

ConsumerKey="PUT_YOUR_CONSUMER_KEY_BEFORE_EXECUTING_THE_CODE"
ConsumerSecret="PUT_YOUR_CONSUMER_SECRET_BEFORE_EXECUTING_THE_CODE"
AccessToken="PUT_YOUR_ACCESS_TOKEN_BEFORE_EXECUTING_THE_CODE"
AcessSecret="PUT_YOUR_ACESS_SECRET_BEFORE_EXECUTING_THE_CODE"

oah=tweepy.OAuthHandler(ConsumerKey,ConsumerSecret)
oah.set_access_token(AccessToken,AcessSecret)
api=tweepy.API(oah)
c=0

class Stream_Listener(tweepy.StreamListener):
    def on_status(self,st):
        global c
        c+=1
        print(st.text.translate(non_bmp_map))
        print()
        if (c==10000):
            print("10k tweets successfully printed")
            return False
    def on_error(self,st):
        print(st)
        if status_code == 420:
            return False

TwitStream=tweepy.Stream(oah,Stream_Listener())
TwitStream.sample(languages=["en"])
