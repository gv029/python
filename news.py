import praw


user_agent = "Karma breakdown 1.0 by /u/_Daimon_"
r = praw.Reddit(user_agent='cool_reddit_app21')
submissions = r.get_subreddit('MLS').get_hot(limit=10)
[str(x) for x in submissions]
