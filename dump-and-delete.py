
import tweepy
from tweepy import OAuthHandler


# auth stuff
consumer_key = 'xx'
consumer_secret = 'xx'
access_token = 'xx'
access_token_secret = 'xx'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user_tweets = api.user_timeline() # returns authenticated user's tweets

tweet_count = 0

for tweet in user_tweets :
    print(tweet.text)
    username = tweet.user.screen_name
    the_id = tweet.id # retrieves ID of individial tweets
    tweet_count += 1
    print(the_id)
print("Found tweets", tweet_count, "for user", username)


# Time to delete those tweets

dialog = input("Delete tweets? Y/N")

if dialog == "Y" :

    # loop tweets again
    for tweet in user_tweets:
        the_id = tweet.id
        api.destroy_status(the_id)

        # check if Deleted
        try :
            api.get_status(the_id)
        except :
            print("Deleted tweet", the_id)

    print("Deleted tweets")


else:
    print("Will not delete tweets")
