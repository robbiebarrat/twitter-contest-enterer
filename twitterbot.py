author__ = 'Robbie Barrat'

# I know the code was a bit messy, but this was a quick project. Inspired by a story I heard on the news where
# a guy did something almost exactly the same and won a bunch of stuff. I couldn't find the code that that guy
# used so I wrote this. Have fun.

import tweepy, time

#enter the corresponding information from your Twitter application:

CONSUMER_KEY = '' #keep the quotes, enter your consumer key
CONSUMER_SECRET = ''#keep the quotes, enter your consumer secret key
ACCESS_KEY = ''#keep the quotes, enter your access token
ACCESS_SECRET =  ''#keep the quotes, enter your access token secret

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


keywords = ["RT to win", "retweet to win",
            "RT and win", "retweet and win",
            "RT for", "RT 4",
            "RETWEET to", "RETWEET TO"]


def search(twts):
    for i in twts:
        # Keywords
        relevant = False
        for x in keywords:
            if x in i.text:
                relevant = True
        if relevant == True:
            # Retweets
            api.retweet(i.id)
            print "JUST RETWEETED " + (i.text)
                # Follows
            if "follow" in (i.text) or "Follow" in (i.text) or "FOLLOW" in (i.text):
                username = i.user.screen_name
                api.create_friendship(username)
                print "JUST FOLLOWED " + str(username)
            if "fav" in (i.text) or "FAV" in (i.text) or "Fav" in (i.text):
                API.create_favorite(i.id)
                print "JUST FAVORITED " + (i.text)
            print "\n************************\n"
            # If you make the sleep time shorter twitter will think you're a robot (rightfully so)
            time.sleep(45)

    restart()

def restart():
    twts = api.search(q="RT to win")
    time.sleep(20)
    print "************************"
    print "\n...Refreshing searched tweets...\n"
    print "************************"
    search(twts)

print "Thank you for using my twitter contest-entering bot.\nConsider leaving a star if you like it."
print "https://github.com/robbiebarrat/twitter-contest-enterer\n"
restart()
