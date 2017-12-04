import config # contains the API keys and access tokens
import twitter
import os
import time

from markovbot import MarkovBot

# Initialise a MarkovBot instance
tweetbot = MarkovBot()

# Get the current directory's path
dirname = os.path.dirname(os.path.abspath(__file__))
# Construct the path to the book
textFile = os.path.join(dirname, 'seinfelf.txt')
# Make your bot read the book!
tweetbot.read(textFile)

## Text Generations
generatedTweet = tweetbot.generate_text(25, seedword=['dream', 'psychoanalysis'])
print(generatedTweet)

# Log in to Twitter
tweetbot.twitter_login(config.cons_key, config.cons_secret, config.access_token, config.access_token_secret)

# Start periodically tweeting
while True:
    tweetbot.twitter_tweeting_start(days=0, hours=0, minutes=1, keywords=None, prefix=None, suffix=None)
    minutesToWait = 30
    secondsToWait = 60 * minutesToWait
    time.sleep(secondsToWait) # tweet every half hour
