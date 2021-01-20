# compute happiness score
def compute_tweets(tweet_file, keyword_file):
    # initializing variables
    x = []
    keyword_values = {}
    punctuations = '''!()[]{};:'"\,<>./?@#$%^&*_~'''
    separated_tweet = []
    sentiment_sum = 0
    tweet_sentiment_sum = 0
    tweet_keywords = 0
    p1 = [49.189787, -67.444574]
    p2 = [24.660845, -67.444574]
    p3 = [49.189787, -87.518395]
    p4 = [24.660845, -87.518395]
    p5 = [49.189787, -101.998892]
    p6 = [24.660845, -101.998892]
    p7 = [49.189787, -115.236428]
    p8 = [24.660845, -115.236428]
    p9 = [49.189787, -125.242264]
    p10 = [24.660845, -125.242264]
    eastern_sentiment_sum = 0
    eastern_keyword_tweets = 0
    eastern_total_tweets = 0
    eastern_average = 0
    central_sentiment_sum = 0
    central_keyword_tweets = 0
    central_total_tweets = 0
    central_average = 0
    mountain_sentiment_sum = 0
    mountain_keyword_tweets = 0
    mountain_total_tweets = 0
    mountain_average = 0
    pacific_sentiment_sum = 0
    pacific_keyword_tweets = 0
    pacific_total_tweets = 0
    pacific_average = 0
    # check that both files exist
    try:
        with open(keyword_file, "r", encoding="utf-8") as keyword_file, open(tweet_file, "r",
                                                                             encoding="utf-8") as tweet_file:

            # stores keyword & corresponding happiness value in dictionary
            for line in keyword_file:
                line = line.rstrip()
                num_list = line.split(',')
                keyword_values[num_list[0]] = int(num_list[1])

            # process tweet file
            for line in tweet_file:
                line = line.split()
                for i in line:
                    separated_tweet.append((i.strip(punctuations)).lower())

                # check that tweet originates in USA
                if (p2[0] <= float(separated_tweet[0]) <= p1[0]) and (p10[1] <= float(separated_tweet[1]) <= p1[1]):
                    for i in separated_tweet:
                        if i in keyword_values:
                            sentiment_sum += keyword_values[i]
                            tweet_keywords += 1

                    # adds tweet sentiment score to timezone running total
                    if sentiment_sum > 0:
                        tweet_sentiment_sum = sentiment_sum / tweet_keywords

                        if p3[1] <= float(separated_tweet[1]) <= p1[1]:
                            eastern_sentiment_sum += tweet_sentiment_sum
                            eastern_keyword_tweets += 1

                        elif p5[1] <= float(separated_tweet[1]) < p3[1]:
                            central_sentiment_sum += tweet_sentiment_sum
                            central_keyword_tweets += 1

                        elif p7[1] <= float(separated_tweet[1]) < p5[1]:
                            mountain_sentiment_sum += tweet_sentiment_sum
                            mountain_keyword_tweets += 1

                        else:
                            pacific_sentiment_sum += tweet_sentiment_sum
                            pacific_keyword_tweets += 1

                        sentiment_sum = 0
                        tweet_keywords = 0
                        tweet_sentiment_sum = 0

                        separated_tweet.clear()

                    # handles tweets with 0 keywords
                    else:
                        if p3[1] <= float(separated_tweet[1]) <= p1[1]:
                            eastern_total_tweets += 1

                        elif p5[1] <= float(separated_tweet[1]) < p3[1]:
                            central_total_tweets += 1

                        elif p7[1] <= float(separated_tweet[1]) < p5[1]:
                            mountain_total_tweets += 1

                        else:
                            pacific_total_tweets += 1

                        separated_tweet.clear()

                # handles non-USA tweets
                else:
                    separated_tweet.clear()
                    continue

            # compute average and total tweets
            if eastern_keyword_tweets != 0:
                eastern_average = eastern_sentiment_sum / eastern_keyword_tweets
            else:
                eastern_average = 0
            eastern_total_tweets = eastern_total_tweets + eastern_keyword_tweets

            if central_keyword_tweets != 0:
                central_average = central_sentiment_sum / central_keyword_tweets
            else:
                central_average = 0
            central_total_tweets = central_total_tweets + central_keyword_tweets

            if mountain_keyword_tweets != 0:
                mountain_average = mountain_sentiment_sum / mountain_keyword_tweets
            else:
                mountain_average = 0
            mountain_total_tweets = mountain_total_tweets + mountain_keyword_tweets

            if pacific_keyword_tweets != 0:
                pacific_average = pacific_sentiment_sum / pacific_keyword_tweets
            else:
                pacific_average = 0
            pacific_total_tweets = pacific_total_tweets + pacific_keyword_tweets
            # return list of tuples
            return [(eastern_average, eastern_keyword_tweets, eastern_total_tweets),
                    (central_average, central_keyword_tweets, central_total_tweets),
                    (mountain_average, mountain_keyword_tweets, mountain_total_tweets),
                    (pacific_average, pacific_keyword_tweets, pacific_total_tweets)
                    ]

    # generates exception
    except IOError as excpt:
        return x


