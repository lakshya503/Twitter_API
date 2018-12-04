from textblob import TextBlob
import sys, tweepy
import matplotlib.pyplot as plt

def calc_percent(a,b):
    return 100*(float(a)/b)

import config
from twython import Twython, TwythonError

twitter = Twython(config.consumer_key, config.consumer_secret, config.access_token, config.access_token_secret)

#establish connection with API
authenticate = tweepy.OAuthHandler( consumer_key , consumer_secret)
authenticate.set_access_token(access_token, access_token_secret)

#create object for API
my_api = tweepy.API(authenticate)

#Inputs for the project :
search_name = input("What would you like to know about? ")
number_of_search = int(input("How many tweets do you want to analyze? "))

#find the tweets
tweet = tweepy.Cursor(my_api.search , q = search_name).items(number_of_search)

# TextBlob generates the polarity of the tweets. -1 means strongly negative
# 0 means neutral and +1 means strongly positive
pos = []
neg =[]
neut=[]
final = 0

#Iterate through the tweets :
for i in tweet:
    analysis = TextBlob(i.text)
    polar = analysis.sentiment.polarity
    final += polar
    # print(polar)
    if(polar == 0):
        neut.append(0)
    if(polar > 0):
        pos.append(0)
    if(polar < 0):
        neg.append(0)


pos_tweets = calc_percent(len(pos), number_of_search)
neg_tweets = calc_percent(len(neg) , number_of_search)
neut_tweets = calc_percent(len(neut) , number_of_search)

average_pol = (-1.0*(len(neg)) + 0.0*len(neut) + 1.0*(len(pos)))/(number_of_search)
print(average_pol)
