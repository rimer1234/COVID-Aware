import requests
import json
import datetime
from dateutil.parser import parse
import tweepy

response = requests.get("https://njvss-appointments-public.s3.amazonaws.com/data/data.json")
todos = json.loads(response.text)

# Textual month, day and year
today = datetime.date.today()
today_str = today.strftime("%B %d, %Y")

now = datetime.datetime.now()
dt_string = now.strftime("%H:%M:%S")


# Authenticate to Twitter
auth = tweepy.OAuthHandler("XXXXXXXX", "XXXXXXXXXXXXXXXXX")
auth.set_access_token("XXXXXXXXXXXXXXXXXXXXXXX", "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#print only the name and address of vaccine centers in Hudson County
for todo in todos:
    if todo["available"] == "yes" :
        address = todo["official"]
        if (address["County"] == "Hudson"):
            tweet_string = "COVID-19 Vaccine availability in Hudson County " + today_str + " as of " + dt_string + " at " 
            tweet_string = tweet_string + todo["name"] + " " + address["Facility Address"]
            tweet_string += "\n"
            tweet_string += address["Facility Website"]
            print(tweet_string)
            api.update_status(tweet_string)


            




