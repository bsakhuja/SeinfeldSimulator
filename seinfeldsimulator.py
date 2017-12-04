import config # contains the API keys and access tokens
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
tweetbot.twitter_login(config.cons_key, config.cons_secret, config.access_token, config.access_token_secret)

# Start periodically tweeting
while True:
	minutesToWait = 30
	secondsToWait = 60 * minutesToWait
	tweetbot.twitter_tweeting_start(days=0, hours=0, minutes=minutesToWait, keywords=None, prefix=None, suffix=None)
	time.sleep(secondsToWait) # tweet every half hour
