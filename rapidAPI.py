import requests
import pandas as pd

url = "https://twitter154.p.rapidapi.com/search/search"

querystring = {"query":"yellowknife evacuation","section":"top","limit":"2","start_date":"2023-08-16","language":"en","end_date":"2023-08-30"}

headers = {
	"X-RapidAPI-Key": "d45b9a1078msha79487cd2e6d99dp170cefjsnb4aae6ae0ae8",
	"X-RapidAPI-Host": "twitter154.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())

res = response.json()


twitter_append = []
for ite in res['results']:
    twitter_data = {'tweet_id' :ite['tweet_id'],
                    'creation_date':ite['creation_date'],
                    'text': ite['text'],
                    'location': ite['user']['location']}
    twitter_append.append(twitter_data)

df = pd.DataFrame(twitter_append)