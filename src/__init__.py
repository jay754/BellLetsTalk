import twitter
import simplejson as json
import time
import requests
import urllib2

"""

Twitter Bot

License: Do whatever you want

"""

def check_request(url):
    try:
        return requests.get(url).status_code
    except Exception as e:
        print str(e)

def generate_data():
    url = "http://numbersapi.com/random?json"
    results = json.load(urllib2.urlopen(url))
    data = str(results["text"]) + "#BellLetsTalk"

    return data

def main(**kwargs):
    url = "http://numbersapi.com/random?json"
    consumer_key = kwargs.get("consumer_key")
    consumer_secret = kwargs.get("consumer_secret")
    access_token_key = kwargs.get("access_token_key")
    access_token_secret = kwargs.get("access_token_secret")
    api = twitter.Api(consumer_key, consumer_secret, access_token_key, access_token_secret)
    results = generate_data()
    count = 1

    while True:
    	print count

    	if check_request(url) is not 200:
      	    raise Exception("bad request")
      	elif check_request(url) == 200:
            try:
                count +=1
                status = api.PostUpdate(results)
                if len(results) < 140:
                    continue
            except Exception as e:
                print str(e)

        time.sleep(2)

        if count > 10:
            break

if __name__ == '__main__':
	print main(consumer_key="", consumer_secret="", access_token_key="", access_token_secret="")