import sentiment_analysis

x = input("What is the name of the tweet file:  ")
y = input("What is the name of the keyword file:  ")

result = (sentiment_analysis.compute_tweets(x, y))
if result == []:
    pass
else:
    print("Eastern Average: {:.4f} | Eastern Keyword Tweets: {} | Eastern Total Tweets: {}".format(result[0][0], int(result[0][1]), int(result[0][2])))
    print("Central Average: {:.4f} | Central Keyword Tweets: {} | Central Total Tweets: {}".format(result[1][0], int(result[1][1]), int(result[1][2])))
    print("Mountain Average: {:.4f} | Mountain Keyword Tweets: {} | Mountain Total Tweets: {}".format(result[2][0], int(result[2][1]), int(result[2][2])))
    print("Pacific Average: {:.4f} | Pacific Keyword Tweets: {} | Pacific Total Tweets: {}".format(result[3][0], int(result[3][1]), int(result[3][2])))


