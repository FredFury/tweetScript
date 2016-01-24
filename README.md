# Tweet.py
 A Python twitter script
 Fred Fourie 

Twitter is a great platform, for news, for gossip, and loads of information. According to Twitter, there are 271 million people using twitter per month and the daily total of Tweets reach up to 500 million. 500 million a day!! This is likely only to increase.
So after my birth into the twitterverse I got interested in harnessing all that data.

My attention was triggered by twitterbots out there like @earthshook, which tweets earthquakes as the happen, automatically.
Being native Linux (Ubuntu) user, with Python as home language I decided to put together a twitter script which can be used from terminal.
This project uses the very handy Tweepy Python library.

To link the script to the twitter account you want, you'll need to authorize it. This can be a bit tricky to figure out, since there is a lot of outdated information out there on how to do it.

I’ll try to add that process later, for now find some info on the matter at http://tweepy.readthedocs.org/en/v2.3.0/auth_tutorial.html#auth-tutorial.

Once you have an access key, edit the auth.sh script with your access keys

******

To use the tweet.py type:
./tweet.py [arg]

Arguments:

At this stage the code make provision for 3 kinds of arguments:

read – Displays the last 10 tweets in the registered users home feed
timeline – Displays the tweets by the user
tweet "string" – Tweets “string” from the user account. No error catching yet
@x – Display the last few tweets of the user x

******
