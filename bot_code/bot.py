import tweepy
import secrets
import time
import PortmanteauCreator

# Twitter requires all requests to use OAth for authentication
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
# Construct the API instance
api = tweepy.API(auth)

# Function to create a valid portmanteau
def handlePortmanteau(tweet_text):
	word1 = tweet.split()[1]
	word2 = tweet.split()[2]
	portmanteau = PortmanteauCreator.portmanteau(word1, word2)
	if portmanteau == "n/a":  # Somehow the input word(s) were invalid; don't tweet
		return
	tweetPortmanteau(word1, word2, portmanteau)

# Function to handle tweeting the completed portmanteau
def tweetPortmanteau(word1, word2, portmanteau):
	

# A class inheriting from tweepy.StreamListener
class BotStreamer(tweepy.StreamListener):
	def on_status(self, status):
		username = status.user.screen_name
		status_id = status.id

		# Get tweet text, check formatting
		tweet_text = status.text
		if check_formatting(tweet_text):
			handlePortmanteau(tweet_text)

	def check_formatting(self, tweet):
		if len(tweet.split()) == 3:  # Tweet length should be 3: @mention word1 word2
			word1 = tweet.split()[1]
			word2 = tweet.split()[2]
			if word1.isalpha() && word2.isalpha():  # Words should only contain letters
				return true
		return false

myStreamListener = BotStreamer()
# Construct Stream instance
stream = tweepy.Stream(auth, myStreamListener)
stream.filter(track=['@makeportmanteau'])
