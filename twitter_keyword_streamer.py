import tweepy
from tweepy.streaming import StreamListener
from tweepy import Stream
from tweepy import OAuthHandler
from config import consumer_key
from config import consumer_secret
from config import access_token
from config import access_token_secret
import json
import thread
#from main_analyzer import main_classifier
import time
import csv
import sys

c = csv.writer(open("keyword.csv", "wb"))
c.writerow(["Tweet"])


tweets_data = []


def tweet_data_sender( threadName, delay):
	count = 0
	flag = 'changed'
	previous_val = 0
	check = 'notdone'
	min_stress = 'null'
	max_stress = 'null'
	avg_stress = 0
    
	while (check == 'notdone'):
		time.sleep(delay)
		length = len(tweets_data)
		if previous_val != (length-1): 
			flag = 'changed'
        
		if ((length > 0) and (flag == 'changed')):
			tweets_data[length-1]
			#result = main_classifier(tweets_data[length-1])
			print tweets_data[length-1]
			c.writerow([tweets_data[length-1].encode("utf-8")])
			#result_array.append(result)
			
			previous_val = length-1
			flag = 'notchanged'
			#stress = stress_finder(result_array)
			#if ((min_stress == 'null') and (max_stress == 'null')):
			#	min_stress = stress
			#	max_stress = stress
			#if (stress < min_stress):
			#	min_stress = stress
			#if (stress > max_stress):
			#	max_stress = stress

			#stress_array.append(stress)

			#print 'Stress Percentage  '+str(stress)+'%'
			#c.writerow([tweets_data[length-1].encode("utf-8"), result.encode("utf-8"), stress])

		if (length > 10):
			check = 'done'

	

class StdOutListener(StreamListener):

    def on_data(self, data):
        tweet = json.loads(data)
        append_text = tweet['text'].replace(";", "")  # to avoid semi colon breaking csv, replaces semicolon with null
        tweets_data.append(append_text)
        return True

    def on_error(self, status):
        print status

def thread_starter():
	try:
		thread.start_new_thread( tweet_data_sender, ("Thread-1", 0.25, ) )
	except:
		print "Error: unable to start thread"


def twitter_keyword_streamer():

	thread_starter()
    #This handles Twitter authetification and the connection to Twitter Streaming API
	l = StdOutListener()
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	stream = Stream(auth, l)
	print "here in"
    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
	# stream.filter(track=['python', 'javascript', 'ruby'])
	stream.filter(follow=['18839785'])
	print "here"


twitter_keyword_streamer()
