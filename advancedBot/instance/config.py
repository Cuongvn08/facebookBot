# Production config
# Local config: instance/config.py (create one if not already available)
# Remove .example from this file's name after filling out all the keys

# Your own webhook verification token for Facebook to forward to
OWN_VERIFICATION_TOKEN='123456789'

# Do not allow debug mode for production
DEBUG=False

# Facebook Page Access Token
PAT = 'EAAFvuaPtazcBACexTxxlxgujn6uAwoJQ3GwB0mbmajBJUWzqWSJQKvJCrshyPaAWsHPX' \
      'xjSb4IOakseB8FmNLEyXyHJY3fcBgxJe0tBxamFGc6y3X4Ko5qdKqYhYyuzF9DHTRkMmn' \
      'KDXyh71HNq79G3Qgj7mgimZCe0rX2wZDZD'
FACEBOOK_APP_ID = '404318086589239'
FACEBOOK_APP_SECRET = '212680397'

#Yelp
# v2
CONSUMER_KEY=""
CONSUMER_SECRET=""
TOKEN=""
TOKEN_SECRET=""

# v3
YELP_V3_TOKEN = ''

# Heroku MongoDB ============
MONGO_URI = "localhost:27017"
MONGO_DBNAME = 'barryDB' # Get database

SIMSIMI_KEY = ''

# Bot operation variables:
PRINT_INCOMING_PAYLOAD = False
PRINT_INCOMING_MESSAGE = False