# import config # contains the API keys and access tokens
import twitter
import os
import time

from markovbot import MarkovBot

# Initialise the MarkovBot instance
tweetbot = MarkovBot()

# Get the seinfeld transcripts and read
dirname = os.path.dirname(os.path.abspath(__file__))
textFile = os.path.join(dirname, 'seinfelf.txt')
tweetbot.read(textFile)

# Text Generations

# Log in to Twitter
consumer_key = os.environ.get('cons_key')
consumer_key_secret = os.environ.get('cons_secret')
access_token = os.environ.get('access_token')
access_token_secret = os.environ.get('access_token_secret')
tweetbot.twitter_login(consumer_key, consumer_key_secret, access_token, access_token_secret)

# Start periodically tweeting
while True:
	minutesToWait = 30
	secondsToWait = 60 * minutesToWait
	tweetbot.twitter_tweeting_start(days=0, hours=0, minutes=minutesToWait, keywords=None, prefix=None, suffix=None)
	time.sleep(secondsToWait) # tweet every half hour
