import tweepy
import json

file = open('keys.json')
data = json.load(file)

access_token = data["access_token"]
access_token_secret = data["access_token_secret"]

consumer_token = data["consumer_token"]
consumer_token_secret = data["consumer_token_secret"]
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

for i in range(len(criteria)):
    sup = str(criteria[i])
    sup2 = sup+"?"
    sup3 = sup.capitalize()
    sup4 = sup3+"?"

    criteria.append(sup2)
    criteria.append(sup3)
    criteria.append(sup4)


message = "Darude - Sandstorm \n https://www.youtube.com/watch?v=y6120QOlsfU&ab_channel=Darude"

auth = tweepy.OAuthHandler(consumer_token,consumer_token_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

print("Bot started")

class MyStreamListener(tweepy.StreamListener):
    message = "Darude - Sandstorm \n https://www.youtube.com/watch?v=y6120QOlsfU&ab_channel=Darude"
    
    #def __init__(self, api):
    #    self.api = api
    #    self.me = api.me()

    def on_status(self, tweet):
        print("found", tweet.user.screen_name)
        messagenew = f"@{tweet.user.screen_name} {message}"
        api.update_status(status=messagenew,
                            in_reply_to_status_id=tweet.id)
        
        print("Replied to",tweet.user.screen_name)

    #def on_status(self, tweet):
    #    print("found",tweet.user.name)
    #    api.update_status(status=message)

    def on_error(self, status):
        print("Error detected")

tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(track=criteria, languages=["en"])
print("stream started")

