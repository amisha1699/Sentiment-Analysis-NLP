import csv
import tweepy
import nltk
import os
import re
from nltk.corpus import stopwords
from textblob import TextBlob

def preprocessTweets(original_tweet):
    # Load the English stopwords in NLTK
    stop_words = set(stopwords.words('english'))

    # Remove the stop words from the tweet
    tweet = " ".join([word for word in original_tweet.split() if word.lower() not in stop_words])

    # Remove URLs
    tweet = re.sub(r"http\S+", "", tweet)

    # Remove emojis and other unwanted characters
    tweet = re.sub(r'[^\w\s#@/:%.,_-]', '', tweet)
    return tweet

def findTweets(topic):
    # Set up your Twitter API credentials
    consumer_key = "<REPLACE_WITH_YOUR_CONSUMER_KEY>"
    consumer_secret = "<REPLACE_WITH_YOUR_CONSUMER_SECRET>"
    access_token = "<REPLACE_WITH_YOUR_ACCESS_TOKEN>"
    access_token_secret = "<REPLACE_WITH_YOUR_ACCESS_TOKEN_SECRET>"

    # Authenticate with the Twitter API using Tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Create the API object
    api = tweepy.API(auth)

    # Grab 100 tweets with the requested topic
    tweets = []
    for tweet in tweepy.Cursor(api.search_tweets, q=topic, tweet_mode='extended').items(100):
        if "retweeted_status" in dir(tweet):
            tweets.append(tweet.retweeted_status.full_text)
        else:
            tweets.append(tweet.full_text)
    print("Collected %d tweets about %s." % (len(tweets), topic))
    return tweets

if __name__ == "_main_":
    # Download the stopwords if necessary
    nltk.download('stopwords')

    # Search for tweets about the chosen topic
    tweets = findTweets("Computational Biology")

    # Define the sentiment analyzer
    sentimentAnalysis = lambda text: TextBlob(text).sentiment.polarity

    # Open a CSV file to store the retrieved tweets and sentiment scores
    with open('tweets_sentiment.csv', mode='w', newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(['Tweet', 'Sentiment Score'])

        print("Performing Sentiment Analysis on the tweets.")
        # Analyze the sentiment of each tweet and write it to the CSV file
        for tweet in tweets:
            clean_tweet = preprocessTweets(tweet)

            # Analyze the sentiment of the filtered tweet
            sentiment = sentimentAnalysis(clean_tweet)

            # Write the tweet and sentiment score to the CSV file
            writer.writerow([clean_tweet, sentiment])

    print("CSV file with tweets and sentiment scores saved.")