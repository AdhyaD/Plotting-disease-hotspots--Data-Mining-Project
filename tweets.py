import tweepy 
  
# Fill the X's with the credentials obtained by  
# following the above mentioned procedure. 
consumer_key = "kEE3DM1v28wb5eNkxOR8oyA38" 
consumer_secret = "ZDuorWdbbl9HzTw0wnQpvXI3NyJcZbxsncRiCnjJL9RJsOepFn"
access_key = "877193643341135872-IZ4ZQ29dZr3USnAyUgCCSwg88P0Ng3K"
access_secret = "gIO13HApWBf24ey50MvTG7G5whUGIFoyLa3PP76PxmkdM"
  
# Function to extract tweets 
def get_tweets(username): 
          
        # Authorization to consumer key and consumer secret 
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
        # Access to user's access key and access secret 
        auth.set_access_token(access_key, access_secret) 
  
        # Calling api 
        api = tweepy.API(auth) 
  
        # 200 tweets to be extracted 
        number_of_tweets=50
        tweets = api.user_timeline(screen_name=username) 
  
        # Empty Array 
        tmp=[]  
  
        # create array of tweet information: username,  
        # tweet id, date/time, text 
        tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created  
        for tweet in tweets:
            print(tweet.entities.get('hashtags'))
            print(tweet.text)
            print("\\\\\\\\\\\\\\\\")
        for j in tweets_for_csv: 
  
            # Appending tweets to the empty array tmp 
            # print(j)
            # print("\n\n")
            # #print("Name:", tweet.author.name.encode('utf8'))
            # #print("Screen-name:", tweet.author.screen_name.encode('utf8'))
            # print("Tweet created:", tweet.created_at)
            # print("Tweet:", tweet.text.encode('utf8'))
            # print("Retweeted:", tweet.retweeted)
            # print("Favourited:", tweet.favorited)
            # #print("Location:", tweet.user.location.encode('utf8'))
            # print("Time-zone:", tweet.user.time_zone)
            # print("Geo:", tweet.geo)
            # print("//////////////////")
            tmp.append(j)  
  
        # Printing the tweets 
        #print(tmp) 
  
  
# Driver code 
if __name__ == '__main__': 
  
    # Here goes the twitter handle for the user 
    # whose tweets are to be extracted. 
    get_tweets("@UNICEFIndia") 