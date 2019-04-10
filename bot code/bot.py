import tweepy
from secrets import *
from PortmanteauCreator import *

# Create an OAuthHandler instance
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

# Construct the API instance
api = tweepy.API(auth)  # Creates an API object to provide access to all
                        # twitter RESTful API methods

class BotStreamer(tweepy.StreamListener):  # Class inheriting from tweepy StreamListener
    def on_status(self, status):
        username = status.user.screen_name
        status_id = status.id

        tweet = status.text
        # Make portmanteau if tweet is formatted correctly
        postMsg = "@" + status.author.screen_name + " "
        if len(tweet.split()) == 2:
            word1 = tweet.split[0]
            word2 = tweet.split[1]
            postMsg += portmanteau(word1, word2)
        postMsg += "."
        api.update_status(postMsg)

myStreamListener = BotStreamer()
# Construct the Stream instance
stream = tweepy.Stream(auth, myStreamListener)
stream.filter(track=['@BotPortmanteau'])
