author__ = 'Robbie Barrat'

# I'd like to give github user 'timster' credit for optimizing a lot of rough bits in the code, he's helped a lot.

# This was a quick project. Inspired by a story I heard of on the news where a guy did something almost exactly the same
#  and won a bunch of stuff. I couldn't find the code that that guy used (I don't think he wanted to release it), so I
# wrote this. Have fun.

import tweepy, time

#enter the corresponding information from your Twitter application:

CONSUMER_KEY = '' #keep the quotes, enter your consumer key
CONSUMER_SECRET = ''#keep the quotes, enter your consumer secret key
ACCESS_KEY = ''#keep the quotes, enter your access token
ACCESS_SECRET =  ''#keep the quotes, enter your access token secret

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

keywords = [
    "rt to", "rt and win", "retweet and win",
    "rt for", "rt 4", "retweet to"
]

bannedwords = [
    "vote"
]

def search(twts):
    for i in twts:
        if not any(k in i.text.lower() for k in keywords) or any(k in i.text.lower() for k in bannedwords):
            continue
        # Retweets
        try:
            api.retweet(i.id)
            print "JUST RETWEETED " + (i.text)
        except:
            print "Hm... Something went wrong.\nYou've probably already retweeted this."
        # Follows
        if "follow" in i.text or "Follow" in i.text or "FOLLOW" in i.text:
            # This part follows the actual contest-holder, instead of some random person who retweeted their contest
            tweet = i.text
            if tweet[0:3] == "RT ":
                tweet = tweet[3:]
            if tweet[0] == "@":
                splittext = (tweet).split(":")
                username = str(splittext[0]).replace("@", "")
                api.create_friendship(username)
                print "JUST FOLLOWED " + (username)
            else:
                username = i.user.screen_name
                api.create_friendship(username)
                print "JUST FOLLOWED " + str(username)

        # This next part favorites tweets if it has to
        if "fav" in i.text or "Fav" in i.text or "FAV" in i.text:
            api.create_favorite(i.id)
            print "JUST FAVORITED " + (i.text)
        # This part waits a minute before moving onto the next one.
        time.sleep(60)


def run():
    for key in ["RT to win", "retweet to win"]:
        print "************************"
        print "\n...Refreshing searched tweets...\n"
        print "************************"
        search(api.search(q=key))


if __name__ == '__main__':
    print "Thank you for using my twitter contest-entering bot.\nConsider leaving a star if you like it."
    print "https://github.com/robbiebarrat/twitter-contest-enterer\n"
    print "Also -- if you run this for too long it will get your account suspended. I'd suggest using it on a 'test account'" \
          "\nand only letting it run for a short time every day."
    while True:
        run()
