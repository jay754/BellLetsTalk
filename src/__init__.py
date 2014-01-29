import twitter
import simplejson as json
import time
import requests
import urllib2

def getRandomData():
	url = "http://numbersapi.com/random?json"
	results = json.load(urllib2.urlopen(url))
	#data = str(results["text"].replace(".","?"))
	data = str(results["text"]) + "#BellLetsTalk"

	if len(data) < 140:
		return data
	else:
		getRandomData()

def main():

	api = twitter.Api(consumer_key='Q2EGXTPpwqeIfrvQiHUAQ',
	                  consumer_secret='2QkSVjD7lW3fsTsX0wU3Q8jrRsYKFLCkZBUZv77ZuCA',
	                  access_token_key='606652366-3a0ieR32ysCusf5ANdU0ukwF8ORCVcz0lsYjCilz',
	                  access_token_secret='icI8PQK0dt36Kzi1USyASOzeO18YuPEMGdYWjwnXooJJu')

	#print api.VerifyCredentials()

	results = getRandomData()
	status = api.PostUpdate(results)

if __name__ == '__main__':
	count = 1
	while True:
		main()

		print count
		#still can be improved
		time.sleep(2)

		if count > 5:
			break

		count +=1