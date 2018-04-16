import praw
from bot_h import *

intro = 'This action was performed by a bot and posts definitions to commonly misconceived words.\n\n'
reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit('politics')

for submission in subreddit.stream.submissions():
	comments = submission.comments
	i = 0
	for top_level_comment in comments:
		if(i > 10):
			break
		try:
			reply = test(top_level_comment.body)
			if(reply != None):
				reply = intro + reply
				print(top_level_comment.fullName)
				#top_level_comment.reply(reply)
		except UnicodeEncodeError:
			continue
		except AttributeError: 
			continue
		i += 1

