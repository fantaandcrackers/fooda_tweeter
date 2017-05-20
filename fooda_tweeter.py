import click
import tweeter_requests

@click.command()
@click.argument('handle')
@click.argument('num')
def tweeter(handle, num):
  tweets = tweeter_requests.get_tweets(handle[1:], num)
  cleaned_tweet_array = map(lambda x: x['text'] + '\nPosted on ' + x['created_at'] + '\n', tweets)

  click.echo( 'Displaying the {} most recent tweets for {}'.format(handle[1:], num) )
  click.echo( '\n'.join(cleaned_tweet_array) )