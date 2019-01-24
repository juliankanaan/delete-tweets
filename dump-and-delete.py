
import tweepy
from tweepy import OAuthHandler


# auth stuff
consumer_key = 'xx'
consumer_secret = 'xx'
access_token = 'xx-xx'
access_token_secret = 'xx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user_tweets = api.user_timeline() # returns authenticated user's tweets


tweet_count = 0

# does the account have any tweets?
def haveTweets():
    global tweet_count
    for tweet in user_tweets :
        tweet_count += 1
        # the_id = tweet.id
    # return last tweet ID so we know where we left off in case we need it 
    if tweet_count > 0 :
        return True
    else:
        return False


def deleteTweets() :

    for tweet in user_tweets:
        the_id = tweet.id
        api.destroy_status(the_id)

        # check if Deleted
        try :
            api.get_status(the_id)
        except :
            print("Deleted tweet", the_id)

    print("Deleted tweets")



def main() :

    dialog = input("Delete tweets? Y/N")

    if dialog == "Y" :

        # if tweets still exist, delete them 20 at a time (limited by API)
        while print(haveTweets()) :
            try :
                deleteTweets()
            except:
                print("Whoops, something went wrong")
        print("Tweets all gone")

    else:
        print("Will not delete tweets")

main()


