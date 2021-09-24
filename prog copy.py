import tweepy
import json

access_token = "1441127096302981120-UmpUO9DLyFPxb5qkMEE77hsy7LPkEv"
access_token_secret = "u5lqcjcPvVL6j0QLdsG5XveYMvcGkfUWr5naD8lEy3HSY"

consumer_token = "271u0ZQyI5cSyuFNdt89Wl303"
consumer_token_secret = "OKM9xYXK7BhjmrYFvDxtU7lj4VeYBZwcOjNSnFEP5zuq07GQZC"
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

criteria = ["what's the song name", 
            "what's the name of the song", 
            "what is the name of the song", 
            "what is the song name", 
            "anyone know the name of this song", 
            "anyone know the name of the song",
            "does anyone know the name of the song",
            "does anyone know the name of this song",
            "what song is used in this video", 
            "what song is used here",
            "can someone tell me the name of this song",
            "what’s the name of the song playing",
            "what is the name of the song playing"]

message = "Darude - Sandstorm \n https://www.youtube.com/watch?v=y6120QOlsfU&ab_channel=Darude"

auth = tweepy.OAuthHandler(consumer_token,consumer_token_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

class MyStreamListener(tweepy.StreamListener):
    message = "Darude - Sandstorm \n https://www.youtube.com/watch?v=y6120QOlsfU&ab_channel=Darude"
    
    #def __init__(self, api):
    #    self.api = api
    #    self.me = api.me()

    def on_status(self, tweet):
        print(tweet.user.name)
        print(f"@{tweet.user.screen_name} {message}")

    #def on_status(self, tweet):
    #    print("found",tweet.user.name)
    #    api.update_status(status=message)

    def on_error(self, status):
        print("Error detected")

tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(track=alpha, languages=["en"])
print("stream started")

