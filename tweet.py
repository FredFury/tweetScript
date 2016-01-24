# tweet.py
import sys
import tweepy

CONSUMER_KEY = [insert your unique key]
CONSUMER_SECRET = [insert your unique secret key]
ACCESS_KEY = [insert your unique key]
ACCESS_SECRET = [insert your unique secret key]
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

print “33[34mTweet.py by Fred Fourie33[0m” # Print your title here

# Search a User by typing their handle as an argument
if sys.argv[1][0] == ‘@’:
user = sys.argv[1]
print “33[1;34m%s33[0m” % user
try:
timeline = api.user_timeline(screen_name=user, include_rts=True, count=5)
for tweet in reversed(timeline):
print tweet.text
print ‘\n’
except:
print “User %s not found” % user

# Display your own Tweets by sending “timeline” as an argument
if sys.argv[1] == “timeline”:
user_tweets = api.user_timeline()
for tweet in reversed(user_tweets):
print tweet.text
print ‘\n’

# Display Tweets by sending “read” as an argument
if sys.argv[1] == “read”:
tweets= api.home_timeline(count=10)
for tweet in reversed(tweets):
print “33[1;34m@%s33[0m” % tweet.user.screen_name
print tweet.text
print ‘\n’

# Tweet by sending “tweet” as an argument, follow by ‘ ‘ and the tweeted text. No char length handling yet.

#if sys.argv[1] == “tweet”:
#api.update_status(sys.argv[2])
#print “TWEET: ‘%s'” % sys.argv[2]
