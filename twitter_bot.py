
import tweepy

# Replace with your keys
API_KEY = 'Q7KcxuhC34PZvoJhsbtd9Xc9O'
API_SECRET = 'XazwQqxndTqi8v7ueJ9DQsEJkyOGGumGhpdaz0Ufdl32ZGWEGm'
ACCESS_TOKEN = '956238058977931265-d9y3eHzpB1DPRmh29B8GzdUMoSAbJrl'
ACCESS_SECRET = 'dCQeYpFlmDqHSCezMNJLjpiAUja3fWvlkbEvXla1U2YWQ'

# Authenticate with Twitter
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# Tweet something
# api.update_status("Hello Twitter! This is my first bot tweet 🤖")
# print("Tweet sent!")

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)
user = api.get_friends()
print(user)
# bearer_token =AAAAAAAAAAAAAAAAAAAAAAZ33AEAAAAAvTficeDo9uBdlrXmZ4W9ax%2FMMIA%3DS1nrlNAnuJMa5USBtNQhuF4xhSPacTeksBYyFIaRRwRvL958NK