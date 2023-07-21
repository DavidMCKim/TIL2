from pathlib import Path
import os
# main code start
import twitter, time, tweepy

# api_key = ''
# api_secret = ''
# access_key = ''
# access_secret = ''

# auth = tweepy.OAuthHandler()


# twitter api connect
twitter_consumer_key = 'IDMJZssCLurIxyIrqlmb1umgI'
twitter_consumer_secret = '0cQ8DCgZWzSTNG0OKPCsOCoqlNScdk1p0pb1onA0t9rHALSTo3'
twitter_access_token = '1680848134770159616-6npwToWVYKy0Frr5SN8MDvCTbmameq'
twitter_access_secret = 'iXiWib0dXFecZw2qUc4zWdfM4LSHvzvC4E9hIV1fMbFeh'

twitter_api = twitter.Api(consumer_key=twitter_consumer_key,
                          consumer_secret=twitter_consumer_secret, 
                          access_token_key=twitter_access_token, 
                          access_token_secret=twitter_access_secret
                          )

account = "@bts_bighit"
timeline = twitter_api.GetUserTimeline(screen_name=account, count=200, include_rts=True, exclude_replies=False)
print(timeline)