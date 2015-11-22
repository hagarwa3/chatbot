import tweepy
import json
#import csv
from tweepy import OAuthHandler
data={}
#with open('lalala.txt', 'w') as outfile:
#	json.dump(data, outfile)
outfile = open('donald.json', 'w')
outfile2 = open('palintweets.txt', 'w')
handle = ['realDonaldTrump']
# with open('C:\Users\Harshit Agarwal\Downloads\SFTwitterSentimentAnalysis.csv', 'r') as f:
#     reader = csv.reader(f)
#     for row in reader:
#     	handle.append(row[0])
consumer_key = 'eSq6W5aevBNKbMP0QyQdusftC'
consumer_secret = 'kvyky5rTDx3H4cfzqde4owRxbadTEaotXQHvlSB0W0Lp2xtK51'
access_token = '1872442789-ycPITsb7DfRnmhHicZ6gWIuDF30N5RDNLVjblVi'
access_secret = 'i9lqvyZagTeRBsjYdWjru9q16CumwGbPSttNsc0oPRxeZ'

    #apikey = "eSq6W5aevBNKbMP0QyQdusftC"
listit = []
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
for lala in handle:
   
    obj = []
    api = tweepy.API(auth)
    timeline = api.user_timeline(screen_name=lala, include_rts=False, count=1000)
    for tweet in timeline:
        #print tweet
        obj.append(tweet.text)
        outfile2.write(tweet.text.encode('ascii', errors='ignore')+"\n")
    print len(obj)
    #print obj	#creates json object and writes to file
    data = {u"handle": lala, u"tweets": obj}
    listit.append(data)

    #json.dump(data, outfile)
    #for status in tweepy.Cursor(api.home_timeline).items(10):
        # Process a single status
        #print(status.text) 
json.dump(listit, outfile)    
outfile.close()
print "hi"