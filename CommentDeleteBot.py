import praw
from prawcore.exceptions import Forbidden
from RedditCredentials import *

import sys

USER_AGENT = "useragent goes here"

USERNAME = REDDIT_USERNAME
PASSWORD = REDDIT_PASSWORD
CLIENT_ID = REDDIT_CLIENT_ID
CLIENT_SECRET = REDDIT_CLIENT_SECRET

def remove_all_comments(reddit):

	subredditList = str(sys.argv[1]).split(',')

	try:
		count = 0
		for comment in reddit.user.me().comments.new(limit=None):
		    if comment.subreddit.display_name.lower() in subredditList:
		        count += 1
		        print("Deleting: " + comment.body)
		        comment.delete()
		print("Deleted " + str(count) + " comments")
	except Exception as exception:
		print(exception)

if __name__ == "__main__":
    reddit = praw.Reddit(
        username=USERNAME,
        password=PASSWORD,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        user_agent=USER_AGENT
    )
    remove_all_comments(reddit)
