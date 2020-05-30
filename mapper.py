#!/usr/bin/env python

import sys
import json
import string

afinn = {}

#create a dictionary of sentiment words from AFINN.txt

afinn_file = open("cache")

for line in afinn_file:
    line = line.strip()
    word, sentiment_score = line.split("\t")
    afinn[word] = (int(sentiment_score))

for line in sys.stdin:
    line.strip()
    tweet = json.loads(line)

    #Extract tweet id and text from the input file

    tweet_id = tweet["id_str"]
    tweet_text = tweet["text"]
    tweet_text.strip()
    tweet_id.strip()

    tweet_text_words = tweet_text.split()

    #Calculate the sentiment score from words in tweet text

    sentiment_score=0

    for words in tweet_text_words:
        word = word.lower()
        word = word.encode('utf-8').translate(None, string.punctuation)
        if(words in afinn.keys()):
            sentiment_score=sentiment_score+afinn[words]
    sentiment_score=str(sentiment_score)

    #Pass tweet id and sentiment score to reducer
    
    print '%s\t%s' % (tweet_id,sentiment_score)
