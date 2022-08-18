def top_ten_retweets(data_json):
    tweets_sorted = sorted(data_json, key=lambda k: k['retweetCount'])
    for x in list(tweets_sorted)[0:11]:
        print(tweets_sorted[content])