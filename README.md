# Hadoop-Sentiment-Analysis

Hadoop is a framework that can be used to store and process large collection of data in a parallel and distributed manner.
The framework is thus used here to solve the problem of sentiment analysis on twitter data. Sentiment analysis is extremely useful in social media monitoring as it allows us to gain an overview of the wider public opinion behind certain topics.

## Project Description 

The project consists of mapper and reducer code along with a sample input file to test the working.
The project aims at collecting live stream data from the twitter account of the user and analyse the sentiments of the tweets in the users wall. 

## Working 

The project uses the well known AFINN dictionary to analyse the sentiment of the tweets. AFINN dictionary is basically a dictionary containing words and its sentiment score ranging from -5 to +5 . Thus, first the tweets are collected by using the oauth2 library in python and then for each tweet words are extracted from the tweets and a final sentiment score is calculated for all the words which occur in the AFINN dictionary , using the sentiment score the analysis is performed and displayed to the user. 

### input.txt

The input file consists of JSON objects collected by using the twitterstream file which uses the oauth2 library in python to collect the live stream twitter data. 


### mapper.py

The mapper takes input from the input file as JSON objects , then some cleaning is performed and the tweet_id and tweet_text is extracted from the JSON object.The mapper takes each word from the tweet_text and calculates the final sentiment score of the tweet using the AFINN dictionary. Mapper returns the tweet_id and sentiment score as a key->value pair to the reducer. 

### reducer.py

The reducer takes the tweet_id and sentiment score from the mapper and according to the sentiment score , analyses the sentiment of the tweet and gives the result to the user.

## Getting the dataset

The dataset is acquired using the twitter stream file. The steps to acquire live stream data from twitter is given below.

1) Install the oauth2 library.
```bash
pip install oauth2
``` 
2) Create twitter account .
3) Go to the [twitter dev apps](http://dev.twitter.com/apps) and login with twitter credentials.
4) Create app and fill the simple form.
5) Go to "Keys and Access Tokens" section and create your access token.
6) Copy API key, API secret, Access token, Access token secret and paste in the twitterstream file.
7) Run following command to get the data in file.
```bash
py twitterstream.py > "filename".txt
``` 
8) To get top "num" number of lines from the file use:
```bash
head -n "num" "filename1".txt > "filename2".txt
```

## Running the code

1) Make project directory in the HDFS.
```bash
hadoop fs -mkdir "directory path"
```
2) Include the input file and AFINN dictionary in project directory.
```bash
hadoop fs -put "file path" "target directory path"
```
3) Run the given command to execute the codes.

```bash
hadoop jar "jar path" -input "input file path" -output "output path" -mapper "mapper path" -reducer "reducer path" -cacheFile "cache file path"#"cache"
```  
4) Output can be seen by executing following command.
```bash
hadoop fs -cat "output directory path"
```  
