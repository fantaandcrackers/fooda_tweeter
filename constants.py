import base64

CONSUMER_KEY = 'xz2O5TriP78jbr5ScbUZqqukw'
CONSUMER_SECRET = '7kUB2lWGyVqXI0OLILDxjfpNkftIiqHEWRSPabyY0cAPLVRITY'
ENCODED_CONSUMER_KEY = base64.b64encode(CONSUMER_KEY + ':' + CONSUMER_SECRET)
REQUEST_TOKEN_URL = 'https://api.twitter.com/oauth2/token'