import twitter
import simplejson as json
import time
import requests
import urllib2

def getRandomData():
	url = "http://numbersapi.com/random?json"
	results = json.load(urllib2.urlopen(url))
	data = str(results["text"].replace(".","?"))

	return data

def main():

	api = twitter.Api(consumer_key='Q2EGXTPpwqeIfrvQiHUAQ',
	                  consumer_secret='2QkSVjD7lW3fsTsX0wU3Q8jrRsYKFLCkZBUZv77ZuCA',
	                  access_token_key='606652366-3a0ieR32ysCusf5ANdU0ukwF8ORCVcz0lsYjCilz',
	                  access_token_secret='icI8PQK0dt36Kzi1USyASOzeO18YuPEMGdYWjwnXooJJu')

	#print api.VerifyCredentials()

	results = getRandomData()
	statusupdate = "Did you know that " + results + "#BellLetsTalk"
	status = api.PostUpdate(statusupdate)

main()