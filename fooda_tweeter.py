import click
import urlparse
import oauth2 as oauth

consumer_key = 'xz2O5TriP78jbr5ScbUZqqukw'
consumer_secret = '7kUB2lWGyVqXI0OLILDxjfpNkftIiqHEWRSPabyY0cAPLVRITY'
request_token_url = 'https://api.twitter.com/oauth/request_token'

@click.command()
@click.argument('handle')
@click.argument('num')
def tweeter(handle, num):
  """Example script."""
  token_key, token_secret = get_token()
  click.echo( oauth_req(get_twitter_url(handle, num), token_key, token_secret, consumer_key, consumer_secret))

def get_twitter_url(handle, num):
  return "https://api.twitter.com/1.1/statuses/user_timeline.json?screenname=%s&count=%s" % (handle, str(num)) 

def get_token():
  consumer = oauth.Consumer(consumer_key, consumer_secret)
  client = oauth.Client(consumer)
  resp, content = client.request(request_token_url, "GET")
  if resp['status'] != '200':
      raise Exception("Invalid response %s." % resp['status'])
  request_token = dict(urlparse.parse_qsl(content))
  token_key = request_token['oauth_token']
  token_secret = request_token['oauth_token_secret']
  return token_key, token_secret

def oauth_req(url, token_key, token_secret, consumer_key, consumer_secret):
  consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)
  token = oauth.Token(key=token_key, secret=token_secret)
  client = oauth.Client(consumer, token)
  click.echo(token)
  resp, content = client.request(url, method="GET")
  return content

