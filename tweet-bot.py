import tweepy
import time 
import os
import random
from dotenv import load_dotenv
load_dotenv()



consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token_key = os.getenv("ACCESS_TOKEN_KEY")
access_token = os.getenv("ACCESS_TOKEN")

FILE_NAME = 'seen_tweets.txt'


# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_key)

api = tweepy.API(auth,  wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)


def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

last_seen_id = str(read_last_seen(FILE_NAME))



def tweet_replies():
    tweets =api.mentions_timeline(since_id=last_seen_id, count=4)
    # print(tweets)
    #remove duplicates
    tweetsIds = []
    if tweets:
        for tweet in reversed(tweets):
            tweet1 = "@" +tweet.user.screen_name + " #EndSarsNow #ReformPoliceNG #SARSMUSTEND #ReformPoliceNG #SARSMUSTEND #ReformPoliceNG  #SARSMUSTEND  #SARSMUSTEND  #SARSMUSTEND #SARSMUSTEND #SARSMUSTEND #SARSMUSTEND #SARSMUSTEND #SARSMUSTEND #SARSMUSTEND #SARSMUSTEND #SARSMUSTEND #EndSars"
            tweet2 = "@" +tweet.user.screen_name + " #ReformPoliceNG #SARSMUSTEND #ReformPoliceNG #SARSMUSTEND #ReformPoliceNG #ReformPoliceNG #SARSMUSTEND #ReformPoliceNG #ReformPoliceNG #EndSarsNow #EndSarsNow #EndSarsNow"
            tweet3 = "@" +tweet.user.screen_name + " #SARSMUSTEND #ReformPoliceNG #SARSMUSTEND #SARSMUSTEND #ReformPoliceNG #SARSMUSTEND #SARSMUSTEND #EndSarNow #SARSMUSTEND #SARSMUSTEND #SARSMUSTEND #SARSMUSTEND #ReformPoliceNG #SARSMUSTEND #SARSMUSTEND #SARSMUSTEND #SARSMUSTEND #SARSMUSTEND #SARSMUSTEND #SARSMUSTEND "
            all_tweets = [tweet1, tweet2, tweet3]
            final_tweet = random.choice(all_tweets)
            # print(final_tweet)
            print(str(tweet.id) + ' - ' + tweet.text)
            try:
                api.update_status(final_tweet, tweet.id)
                api.create_favorite(tweet.id)
            


                store_last_seen(FILE_NAME, tweet.id)

            except Exception as e:
                if e.api_code == 187:
                    time.sleep(20)
                elif e.api_code == 186:
                    time.sleep(20)
                time.sleep(20)
                print("an error occured", e)
    else:
        print('No New Tweets')

tweet_replies()
time.sleep(20)