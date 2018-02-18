# Twitter-Analysis

A short description on every file:-

1. sample_tweets.py<br />
   It collects a random sample of 10K tweets using the Twitter API and prints them on the command line.
2. random_tweets.py<br />
   It collects a random sample of 10k tweets using the Twitter API and stores them in a MongoDB collection named tweets.
3. print_all_tweets.py<br />
   It prints all the tweets present in the MongoDB collection named tweets on the command line.
4. named entity.py<br />
   It prints the 15 most frequently occurring named-entities from the tweets stored in MongoDB along with the number of their occurrences.
5. news_involving_namedEntites.py<br />
   It collects 20 latest news each from BBC News, Fox News and newsAPI featuring the named-entites and stores them in different MongoDB
   collections.
6. tweets_involving_namedEntities.py<br />
   It collects 1000 tweets of each named entity using the Twitter API and stores them in a MongoDB collection.
7. sentiment_analysis_and_comparison.py<br />
   It performs a Sentiment Analysis on the news articles and tweets collected from news sources and twitter, and compare the twitter and
   news sentiments for the common named-entities. It also prints how the TextBlob analyses for a positive, negative or neutral sentiment.
8. sentiment_analysis_and_comparison_with_illustrations.py<br />
   It prints the comparison of twitter and news sentiments along with the graphical interpretation.
<br />
<br />
Get your own twitter API from https://apps.twitter.com/ and replace the "PUT_YOURUT_YOUR_CONSUMER_KEY_BEFORE_EXECUTING_THE_CODE" text from the code with your Keys.
<br />
<br />
Understanding the code...
<br />
While collecting the tweets there were 2 main challenges:<br />
1. we need to convert the non-bmp charachters like emoticons, so that the are printable on the command line. For this we mapped the every    charachter outside the BMP range to a replacement charachter.
   <br />
   Other way could have been to clean the tweet by removing links and special characters using simple regex statements.
2. While collecting random tweets, tweets of any language like russian, arabic, japanese etc. were collected. So I applied a language        filter so that tweets in only English language could be collected.
<br />
Also keep in mind that we need to overload the on_data() method of the StreamListener class so as to send the tweets to a MongoDB collection.
<br />
While finding the top 5 named entities, the most frequently occurred named entity was BTS ARMY, which is a fandom. But while finding news for the same, very few news articles were available. Therefore, I printed top 15 named entities and chose those on which news articles were also available. I also converted all the keywords to lower case before adding them to a dictionary.
<br />
<br />
I collected a sample of 1000 tweets and 20 news articles corresponding to every named entity. And then analysed the data by comparing the sentiment of each news using TextBlob. Finally to represent the data graphically I plotted a graph using the matplotlib library of Python.


<br /><br /><br />
I learnt MongoDB from Tutorials Point. The link for the same is https://www.tutorialspoint.com/mongodb/index.htm.<br />
I learnt to use tweepy from the documentation of tweepy present on GitHub. https://github.com/tweepy/tweepy <br />
For finding the named enitites, I learnt natural language processing using the NLTK module from the YouTube tutorials https://www.youtube.com/watch?v=FLZvOKSCkxY&list=PLQVvvaa0QuDf2JswnfiGkliBInZnIC4HL.<br />
To extract news from a news source, I used the following link https://newsapi.org/docs/get-started.<br />
For performing a Sentiment analysis, I used the textblob library of python. http://textblob.readthedocs.io/en/dev/ <br />
Later I learnt matplotlib to plot graphs in python.<br />
For making a webApp I am learning Django from https://www.youtube.com/watch?v=FNQxxpM1yOs&list=PLQVvvaa0QuDeA05ZouE4OzDYLHY-XH-Nd&index=1.
I hope I will complete my last task in a day.
