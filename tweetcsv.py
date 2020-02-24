import tweepy
import csv
import pandas as pd
####input your credentials here

consumer_key = "kEE3DM1v28wb5eNkxOR8oyA38" 
consumer_secret = "ZDuorWdbbl9HzTw0wnQpvXI3NyJcZbxsncRiCnjJL9RJsOepFn"
access_token = "877193643341135872-IZ4ZQ29dZr3USnAyUgCCSwg88P0Ng3K"
access_token_secret = "gIO13HApWBf24ey50MvTG7G5whUGIFoyLa3PP76PxmkdM"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('ua3.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#flu",count=1000, lang="en", since="2019-01-01").items():
    print (tweet.created_at, tweet.text)
    print(tweet.user.location)
    print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
    csvWriter.writerow([tweet.user.location.encode('utf-8'), tweet.text.encode('utf-8')])