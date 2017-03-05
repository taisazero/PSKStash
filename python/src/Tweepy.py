import tweepy
import os

consumerKey = os.environ.get('TWITTER_CONSUMER_KEY')
consumerSecret = os.environ.get('TWITTER_CONSUMER_SECRET')
accessToken = os.environ.get('TWITTER_ACCESS_TOKEN')
accessSecret = os.environ.get('TWITTER_ACESS_TOKEN_SECRET')

#oAuth
auth = tweepy.OAuthHandler(consumerKey,consumerSecret)

auth.set_access_token(accessToken, accessSecret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)


