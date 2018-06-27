# twitter-contest-enterer
Have you ever seen a tweet that looks like this?
![alt tag](http://i.imgur.com/LDkU6hC.png)

Chances are you have. This program (written entirely in python) finds and retweets these types of tweets. It also automatically favorites the tweet if the word "favorite"/"fav" is in it, and/or it will follow the user if the word "follow" is in the tweet.

# Screenshots
Here it is running. As you can see it found the word "follow" in a few tweets so it followed the user too.
Maybe it's just me but I think that's pretty cool.

![alt tag](http://i.imgur.com/Ss5EZ5M.png)


Here is a picture of something it retweeted. It also followed this account (you don't see that though).
![alt tag](http://i.imgur.com/F2DodMy.png)

# Modules and code
It's compatible with all versions, and the only modules it requires are 'time' (built-in) and tweepy
You can install Tweepy with

    pip install tweepy

and the github repo for it is here:

    https://github.com/tweepy/tweepy

Also -- you can get all the keys/tokens if you follow this guide.
 
     https://www.digitalocean.com/community/tutorials/how-to-authenticate-a-python-application-with-twitter-using-tweepy-on-ubuntu-14-04

# Progress
I just looked at the last 20 things it has retweeted, and it retweeted 18 'good' tweets, and only 2 'bad' ones. A 'good' tweet is one that is a "Retweet for a chance to win"-type tweet, while a 'bad' tweet is a tweet that isn't a contest. I'd say that 90% valid retweets is pretty great.

You can check this for yourself; check out [@beefbot9000](https://twitter.com/beefbot9000)

# Terms of use
Feel free to do whatever with it, but if you get in trouble with Twitter you'd better not get me in trouble too.

