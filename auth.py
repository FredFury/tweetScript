# Auth.py
import tweepy

CONSUMER_KEY = ‘[Your key]’
CONSUMER_SECRET = ‘[Your secret key]’

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth_url = auth.get_authorization_url()
print ‘Please authorize: ‘ + auth_url
verifier = raw_input(‘PIN: ‘).strip()
auth.get_access_token(verifier)
print “ACCESS_KEY = ‘%s'” % auth.access_token.key
print “ACCESS_SECRET = ‘%s'” % auth.access_token.secret
Status API Training Shop Blog About Pricing
© 2016 GitHub, Inc. Terms Privacy Security Contact Help
