# Twitter-Analysis

A short description on every file:-

1. sample_tweets.py<br />
   It collects a random sample of 10K tweets using the Twitter API and prints them on the command line.
2. random_tweets.py
   It collects a random sample of 10k tweets using the Twitter API and stores them in a MongoDB collection named tweets.
3. print_all_tweets.py
   It prints all the tweets present in the MongoDB collection named tweets on the command line.
4. named entity.py
   It prints the 15 most frequently occurring named-entities from the tweets stored in MongoDB along with the number of their occurrences.
5. news_involving_namedEntites.py
   It collects 20 latest news each from BBC News, Fox News and newsAPI featuring the named-entites and stores them in different MongoDB
   collections.
6. tweets_involving_namedEntities.py
   It collects 1000 tweets of each named entity using the Twitter API and stores them in a MongoDB collection.
7. sentiment_analysis_and_comparison.py
   It performs a Sentiment Analysis on the news articles and tweets collected from news sources and twitter, and compare the twitter and
   news sentiments for the common named-entities. It also prints how the TextBlob analyses for a positive, negative or neutral sentiment.
8. sentiment_analysis_and_comparison_with_illustrations.py
   It prints the comparison of twitter and news sentiments along with the graphical interpretation.


