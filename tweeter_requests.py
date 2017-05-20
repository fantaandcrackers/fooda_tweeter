import requests
from constants import ENCODED_CONSUMER_KEY, REQUEST_TOKEN_URL

def get_bearer_token():
  headers = {}
  headers['Authorization'] = 'Basic' + ' ' + ENCODED_CONSUMER_KEY
  headers['Content-Type'] = 'application/x-www-form-urlencoded;charset=UTF-8'
  data = 'grant_type=client_credentials'

  response = requests.post(REQUEST_TOKEN_URL, headers=headers, data=data)
  return response.json()['access_token']

bearer_token = get_bearer_token()

def send_authenticated_request(url):
  headers = {}
  headers['Authorization'] = 'Bearer' + ' ' + bearer_token
  response = requests.get(url, headers=headers)
  return response.json()

def get_twitter_url(handle, num):
  return "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name={}&count={}".format(handle, str(num)) 

def get_tweets(handle, num):
  url = get_twitter_url(handle, num)
  return send_authenticated_request(url)