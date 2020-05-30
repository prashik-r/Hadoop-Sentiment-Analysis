#!/usr/bin/env python

import sys

for line in sys.stdin:
	line.strip()
	tweet_id,sentiment_score,=line.split("\t",1)

	#Output the result given by mapper to the user

	print 'Tweet ID : %s' % (tweet_id)
	print 'Sentiment Score : %s' % (sentiment_score)

	sentiment_score=int(sentiment_score)

	if(sentiment_score<0):
		print 'Sentiment Analysis : Negative Tweet\n\n'
	elif(sentiment_score>0):
		print 'Sentiment Analysis : Positive Tweet\n\n'
	else:
		print 'Sentiment Analysis : Neutral Tweet\n\n'
