import praw

reddit = praw.Reddit(client_id='jAdMtveNKrDi9g',
                     client_secret='6LFxnKmAM-M_fFb6aE83-FZLvQU',
                     user_agent='python:com.example.commentcounter:v1.0.0')

submissions = reddit.subreddit('EthTrader').hot(limit=10) #make top instead of hot

totalComments = 0
totalScore = 0
print(submissions.next())
for submission in submissions:
    print(submission.title + ': ' + str(len(submission.comments)) + ': ' + str(submission.score)) #add sentiment of each article title too

    totalComments += len(submission.comments)
    totalScore += submission.score

print('Total Comments: ', totalComments)
print('Total Score: ', totalScore)

#calculate daily score (sum of daily_sentiment*daily_total_comments*daily_score for each article within the past 24 hours)


#other things to do: program should skip posts that have below x amount of comments (since they're most likely irrelevant)
#posts by ethereum staff should be weighted higher












#extra information
#print('Number of top level comments: ', len(submission.comments))
#for top_level_comment in submission.comments:
#	print('Comment: ', top_level_comment.body)


#edit below if data is to be exported to an excel file
#with open('comments.csv', 'a') as outf:
# 2 dimension array needs two for loops
#for ele in final:
#   for ele2 in ele:
#       # write to file in the proper comma delimited format, one per line
#       outf.write(u"{0},{1}\n".format(ele2['id'], ele2['comment']).encode('utf-8'))

#Sentiment Analysis
# import nltk
#import numpy
#from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

#text_file = open("wordsList.txt", "r")
#lines = text_file.read()

#sid = SIA()
#print(sid.polarity_scores(lines))




#Abdur's Twitter Project
#import Twython
# keys when registering app with twitter
#APP_KEY = 'KqIkw34tQJHOtZS3bbYyc2EYr'
#APP_SECRET = 'l3t3mydsl7QLWoNfm3ZdIBfjmPb1tMWbxlfe6FS1xGSSTFhfR7'


# new twython instance for authorization
#twitter = Twython(APP_KEY, APP_SECRET)
#    auth = twitter.get_authentication_tokens(callback_url = 'http://ide50-abdurrehman1.cs50.io/verify')

# get request tokens from auth
#OAUTH_TOKEN = auth['oauth_token']
#    OAUTH_TOKEN_SECRET = auth['oauth_token_secret']
