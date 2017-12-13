import praw
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime



def initReddit():
    # init API
    print "starting up reddit api"
    reddit = praw.Reddit(client_id='jAdMtveNKrDi9g',
                         client_secret='6LFxnKmAM-M_fFb6aE83-FZLvQU',
                         user_agent='python:com.example.commentcounter:v1.0.0')
    print "reddit API initialized"
    return reddit

def getSubmissions(unix_date, reddit):
    # pull submissions
    submissions = reddit.subreddit('EthTrader').submissions(start = unix_date, 
                                                            end = unix_date + 86400) #make top instead of hot
    # set total comment/score counters
    print "retrieved"
    return submissions


# Super Score Calculator
def superScore(title, comment_ct, score, sentiment_dict):
    multiplier = (1.0 - (5 * sentiment_dict['neg']) + (5 * sentiment_dict['pos']))
    super_score = (comment_ct + score) * multiplier
    
    def printScore():
        print '*******    string: ', submission.title
        print '*******  comments: ', len(submission.comments)
        print '*******     score: ', submission.score
        print "*********** negative: ", sentiment_dict['neg']
        print "***********  neutral: ", sentiment_dict['neu']
        print "*********** positive: ", sentiment_dict['pos']
        print "multiplier: ", multiplier
        print "SUPERSCORE: ", super_score
        print '\n'
   
    return super_score

#Sentiment Analysis
def sentiment(string):
    sid = SIA()
    return sid.polarity_scores(string)





def score(submission_obj): 
    for submission in submissions:
        #totalComments = 0
        #totalScore = 0
        #totalComments += len(submission.comments)
        #totalScore += submission.score
        print submission.title
        superScore(submission, sentiment(submission.title))

print "start"

counter = 0
reddit = initReddit()
date = 1493596800
submissions = getSubmissions(date, reddit) # start may 1st



#score(submissions)     

#print submissions

titles = []
scores = []
comments = []
super_scores = []
dates = []


for i in range(0, 150):
    
    date = 1493596800 + (86400 * i)

    print 'date:', datetime.datetime.utcfromtimestamp(date)
    #retrieve data
    reddit = initReddit()
    submissions = getSubmissions(date, reddit)
    
    # create arrays to be added to pandas
    print 'scraping and scoring...'
    for submission in submissions:
        title = submission.title
        score = submission.score
        len_comments = len(submission.comments)
        titles.append(title)
        scores.append(score)
        comments.append(len_comments)
        super_scores.append(superScore(title, len_comments, score, sentiment(title)))
        dates.append(datetime.datetime.utcfromtimestamp(date))
    


df = pd.DataFrame({
                    #'date': pd.Timestamp('20130102'), 
                    'title': titles,
                    'score': scores,
                    'comments': comments,
                    'date': dates,
                    'super_scores' : super_scores
                  })


df
