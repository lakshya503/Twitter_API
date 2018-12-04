from config import *
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from textblob import TextBlob
from elasticsearch import Elasticsearch

import config
from twython import Twython, TwythonError

twitter = Twython(config.consumer_key, config.consumer_secret, config.access_token, config.access_token_secret)
# print(twitter)

# Sentiment live stream of a given topic
class TweetListener(StreamListener):

    def on_data(self,data):

        # load the data found
        new_data = json.loads(data)

        # using the TextBlob library, get the text of the tweet
        tweet = TextBlob(new_data["text"])

        # sentiment ranges from -1 to 1
        # -1 being strongly negative, +1 being strongly positive
        sentiment = tweet.sentiment.polarity

        # print the sentiment score
        print(sentiment)

        # print the sentiment tag
        if sentiment < 0:
            print("Negative tweet")
        elif sentiment == 0.0:
            print("Neutral tweet")
        else:
            print("Positive tweet")

        return True

    def on_error(self,status):
        print(status)


authorize = OAuthHandler(consumer_key,consumer_secret)
authorize.set_access_token(access_token,access_token_secret)

listener1 = TweetListener()
stream1 = Stream(authorize, listener1)
stream1.filter(track = ["python"])
