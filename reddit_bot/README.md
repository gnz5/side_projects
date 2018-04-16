# Reddit Bot

This is a simple reddit bot which scans posts and comments in various subreddits for
terms that are often misunderstood and used improperly, such as "Fascism" and "Socialism,"
and posts their definitions from a credible source and the link to the definition. The bot
makes use of the Python Reddit API wrapper "PRAW." 

The program first begins by calling the praw class and getting an instance of "Reddit."
Using that, submissions and comments can be examined, and posts can be made. The main loop
of the program first fetches the string containing all text in a post or comment. Then the
string is stripped of all non-alphabetical characters and articles such as "the" and "a." 
Afterwards, the string is split up into individual words and compared to a database of keywords.
If a match is found, the definition of the keyword is posted and the comment id is saved so
the bot doesn't reply multiple times to the same comment.

For more information on PRAW see

https://praw.readthedocs.io/en/latest/