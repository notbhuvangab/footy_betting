## Add Twitter Sentiment Analysis
import tweepy
from textblob import TextBlob

# Authenticate with Twitter API
consumer_key = 'eq9QvcZRupgT1iBdqEbnu9Wea'
consumer_secret = 'cvbu9YAI5TcGXkuVk6mNB54cNjlAo3Pbr3NcXGb109XFI2PcHX'
access_token = '2479063608-4cx5s5H6wIRXZJBcM19MbGSBBLPUCuY8K54UYNv'
access_token_secret = 'vpGBGHEzBrxNp1JKIeWSE9c1n5WMACamAeDVTcNFj8j8k'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Search for tweets about the Warriors
def get_club_stats(teamName):
    club_tweets = tweepy.Cursor(api.search, q=teamName).items(100)


# Perform sentiment analysis on tweets
positive_tweets = 0
negative_tweets = 0
neutral_tweets = 0

for tweet in warriors_tweets:
    analysis = TextBlob(tweet.text)
    if analysis.sentiment.polarity > 0:
        positive_tweets += 1
    elif analysis.sentiment.polarity < 0:
        negative_tweets += 1
    else:
        neutral_tweets += 1

# Print results
print("Positive tweets: ", positive_tweets)
print("Negative tweets: ", negative_tweets)
print("Neutral tweets: ", neutral_tweets)
