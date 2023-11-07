import requests
import pandas as pd

url = "https://twitter154.p.rapidapi.com/search/search"


# 16th August
querystring = {"query":"yellowknife evacuation","section":"top","limit":"50","start_date":"2023-08-16","language":"en","end_date":"2023-08-17"}

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
                    'username': ite['user']['username'],
                    'name': ite['user']['name'],
                    'creation_date':ite['creation_date'],
                    'text': ite['text'],
                    'location': ite['user']['location']}
    twitter_append.append(twitter_data)

df1 = pd.DataFrame(twitter_append)

import requests
import pandas as pd

url = "https://twitter154.p.rapidapi.com/search/search"

# 17th August
querystring = {"query":"yellowknife evacuation","section":"top","limit":"50","start_date":"2023-08-17","language":"en","end_date":"2023-08-18"}

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
                    'username': ite['user']['username'],
                    'name': ite['user']['name'],
                    'creation_date':ite['creation_date'],
                    'text': ite['text'],
                    'location': ite['user']['location']}
    twitter_append.append(twitter_data)

df2 = pd.DataFrame(twitter_append)


url = "https://twitter154.p.rapidapi.com/search/search"

# 18th August
querystring = {"query":"yellowknife evacuation","section":"top","limit":"50","start_date":"2023-08-18","language":"en","end_date":"2023-08-19"}

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
                    'username': ite['user']['username'],
                    'name': ite['user']['name'],
                    'creation_date':ite['creation_date'],
                    'text': ite['text'],
                    'location': ite['user']['location']}
    twitter_append.append(twitter_data)

df3 = pd.DataFrame(twitter_append)

url = "https://twitter154.p.rapidapi.com/search/search"

# 19th August
querystring = {"query":"yellowknife evacuation","section":"top","limit":"50","start_date":"2023-08-19","language":"en","end_date":"2023-08-20"}

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
                    'username': ite['user']['username'],
                    'name': ite['user']['name'],
                    'creation_date':ite['creation_date'],
                    'text': ite['text'],
                    'location': ite['user']['location']}
    twitter_append.append(twitter_data)

df4 = pd.DataFrame(twitter_append)

url = "https://twitter154.p.rapidapi.com/search/search"

# 20th August
querystring = {"query":"yellowknife evacuation","section":"top","limit":"50","start_date":"2023-08-20","language":"en","end_date":"2023-08-21"}

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
                    'username': ite['user']['username'],
                    'name': ite['user']['name'],
                    'creation_date':ite['creation_date'],
                    'text': ite['text'],
                    'location': ite['user']['location']}
    twitter_append.append(twitter_data)

df5 = pd.DataFrame(twitter_append)

url = "https://twitter154.p.rapidapi.com/search/search"

# 21th August
querystring = {"query":"yellowknife evacuation","section":"top","limit":"50","start_date":"2023-08-21","language":"en","end_date":"2023-08-22"}

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
                    'username': ite['user']['username'],
                    'name': ite['user']['name'],
                    'creation_date':ite['creation_date'],
                    'text': ite['text'],
                    'location': ite['user']['location']}
    twitter_append.append(twitter_data)

df6 = pd.DataFrame(twitter_append)

url = "https://twitter154.p.rapidapi.com/search/search"

# 22th August
querystring = {"query":"yellowknife evacuation","section":"top","limit":"50","start_date":"2023-08-22","language":"en","end_date":"2023-08-23"}

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
                    'username': ite['user']['username'],
                    'name': ite['user']['name'],
                    'creation_date':ite['creation_date'],
                    'text': ite['text'],
                    'location': ite['user']['location']}
    twitter_append.append(twitter_data)

df7 = pd.DataFrame(twitter_append)

url = "https://twitter154.p.rapidapi.com/search/search"

# 23th August
querystring = {"query":"yellowknife evacuation","section":"top","limit":"50","start_date":"2023-08-23","language":"en","end_date":"2023-08-24"}

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
                    'username': ite['user']['username'],
                    'name': ite['user']['name'],
                    'creation_date':ite['creation_date'],
                    'text': ite['text'],
                    'location': ite['user']['location']}
    twitter_append.append(twitter_data)

df8 = pd.DataFrame(twitter_append)

url = "https://twitter154.p.rapidapi.com/search/search"

# 24th August
querystring = {"query":"yellowknife evacuation","section":"top","limit":"50","start_date":"2023-08-24","language":"en","end_date":"2023-08-25"}

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
                    'username': ite['user']['username'],
                    'name': ite['user']['name'],
                    'creation_date':ite['creation_date'],
                    'text': ite['text'],
                    'location': ite['user']['location']}
    twitter_append.append(twitter_data)

df9 = pd.DataFrame(twitter_append)

url = "https://twitter154.p.rapidapi.com/search/search"

# 25th August
querystring = {"query":"yellowknife evacuation","section":"top","limit":"50","start_date":"2023-08-25","language":"en","end_date":"2023-08-26"}

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
                    'username': ite['user']['username'],
                    'name': ite['user']['name'],
                    'creation_date':ite['creation_date'],
                    'text': ite['text'],
                    'location': ite['user']['location']}
    twitter_append.append(twitter_data)

df10 = pd.DataFrame(twitter_append)

url = "https://twitter154.p.rapidapi.com/search/search"

# 26th August
querystring = {"query":"yellowknife evacuation","section":"top","limit":"50","start_date":"2023-08-26","language":"en","end_date":"2023-08-27"}

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
                    'username': ite['user']['username'],
                    'name': ite['user']['name'],
                    'creation_date':ite['creation_date'],
                    'text': ite['text'],
                    'location': ite['user']['location']}
    twitter_append.append(twitter_data)

df11 = pd.DataFrame(twitter_append)

url = "https://twitter154.p.rapidapi.com/search/search"

# 27th August
querystring = {"query":"yellowknife evacuation","section":"top","limit":"50","start_date":"2023-08-27","language":"en","end_date":"2023-08-28"}

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
                    'username': ite['user']['username'],
                    'name': ite['user']['name'],
                    'creation_date':ite['creation_date'],
                    'text': ite['text'],
                    'location': ite['user']['location']}
    twitter_append.append(twitter_data)

df12 = pd.DataFrame(twitter_append)

url = "https://twitter154.p.rapidapi.com/search/search"

# 28th August
querystring = {"query":"yellowknife evacuation","section":"top","limit":"50","start_date":"2023-08-28","language":"en","end_date":"2023-08-29"}

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
                    'username': ite['user']['username'],
                    'name': ite['user']['name'],
                    'creation_date':ite['creation_date'],
                    'text': ite['text'],
                    'location': ite['user']['location']}
    twitter_append.append(twitter_data)

df13 = pd.DataFrame(twitter_append)

url = "https://twitter154.p.rapidapi.com/search/search"

# 29th August
querystring = {"query":"yellowknife evacuation","section":"top","limit":"50","start_date":"2023-08-29","language":"en","end_date":"2023-08-30"}

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
                    'username': ite['user']['username'],
                    'name': ite['user']['name'],
                    'creation_date':ite['creation_date'],
                    'text': ite['text'],
                    'location': ite['user']['location']}
    twitter_append.append(twitter_data)

df14 = pd.DataFrame(twitter_append)

url = "https://twitter154.p.rapidapi.com/search/search"

# 30th August
querystring = {"query":"yellowknife evacuation","section":"top","limit":"50","start_date":"2023-08-30","language":"en","end_date":"2023-08-31"}

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
                    'username': ite['user']['username'],
                    'name': ite['user']['name'],
                    'creation_date':ite['creation_date'],
                    'text': ite['text'],
                    'location': ite['user']['location']}
    twitter_append.append(twitter_data)

df15 = pd.DataFrame(twitter_append)

url = "https://twitter154.p.rapidapi.com/search/search"

# 31th August
querystring = {"query":"yellowknife evacuation","section":"top","limit":"50","start_date":"2023-08-31","language":"en","end_date":"2023-09-01"}

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
                    'username': ite['user']['username'],
                    'name': ite['user']['name'],
                    'creation_date':ite['creation_date'],
                    'text': ite['text'],
                    'location': ite['user']['location']}
    twitter_append.append(twitter_data)

df16 = pd.DataFrame(twitter_append)

url = "https://twitter154.p.rapidapi.com/search/search"

# 1 Sept
querystring = {"query":"yellowknife evacuation","section":"top","limit":"50","start_date":"2023-09-01","language":"en","end_date":"2023-09-02"}

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
                    'username': ite['user']['username'],
                    'name': ite['user']['name'],
                    'creation_date':ite['creation_date'],
                    'text': ite['text'],
                    'location': ite['user']['location']}
    twitter_append.append(twitter_data)

df17 = pd.DataFrame(twitter_append)

url = "https://twitter154.p.rapidapi.com/search/search"

# 2 Sept
querystring = {"query":"yellowknife evacuation","section":"top","limit":"50","start_date":"2023-09-02","language":"en","end_date":"2023-09-03"}

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
                    'username': ite['user']['username'],
                    'name': ite['user']['name'],
                    'creation_date':ite['creation_date'],
                    'text': ite['text'],
                    'location': ite['user']['location']}
    twitter_append.append(twitter_data)

df18 = pd.DataFrame(twitter_append)

url = "https://twitter154.p.rapidapi.com/search/search"

# 3 Sept
querystring = {"query":"yellowknife evacuation","section":"top","limit":"50","start_date":"2023-09-03","language":"en","end_date":"2023-09-04"}

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
                    'username': ite['user']['username'],
                    'name': ite['user']['name'],
                    'creation_date':ite['creation_date'],
                    'text': ite['text'],
                    'location': ite['user']['location']}
    twitter_append.append(twitter_data)

df19 = pd.DataFrame(twitter_append)

url = "https://twitter154.p.rapidapi.com/search/search"

# 4 sept
querystring = {"query":"yellowknife evacuation","section":"top","limit":"50","start_date":"2023-09-04","language":"en","end_date":"2023-09-05"}

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
                    'username': ite['user']['username'],
                    'name': ite['user']['name'],
                    'creation_date':ite['creation_date'],
                    'text': ite['text'],
                    'location': ite['user']['location']}
    twitter_append.append(twitter_data)

df20 = pd.DataFrame(twitter_append)

url = "https://twitter154.p.rapidapi.com/search/search"

# 5 Sept
querystring = {"query":"yellowknife evacuation","section":"top","limit":"50","start_date":"2023-09-05","language":"en","end_date":"2023-09-06"}

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
                    'username': ite['user']['username'],
                    'name': ite['user']['name'],
                    'creation_date':ite['creation_date'],
                    'text': ite['text'],
                    'location': ite['user']['location']}
    twitter_append.append(twitter_data)

df21 = pd.DataFrame(twitter_append)

url = "https://twitter154.p.rapidapi.com/search/search"

# 6 sept
querystring = {"query":"yellowknife evacuation","section":"top","limit":"50","start_date":"2023-09-06","language":"en","end_date":"2023-09-07"}

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
                    'username': ite['user']['username'],
                    'name': ite['user']['name'],
                    'creation_date':ite['creation_date'],
                    'text': ite['text'],
                    'location': ite['user']['location']}
    twitter_append.append(twitter_data)

df22 = pd.DataFrame(twitter_append)

url = "https://twitter154.p.rapidapi.com/search/search"

# 7 Sept
querystring = {"query":"yellowknife evacuation","section":"top","limit":"50","start_date":"2023-09-07","language":"en","end_date":"2023-09-08"}

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
                    'username': ite['user']['username'],
                    'name': ite['user']['name'],
                    'creation_date':ite['creation_date'],
                    'text': ite['text'],
                    'location': ite['user']['location']}
    twitter_append.append(twitter_data)

df23 = pd.DataFrame(twitter_append)

url = "https://twitter154.p.rapidapi.com/search/search"

# 8 Sept
querystring = {"query":"yellowknife evacuation","section":"top","limit":"50","start_date":"2023-09-08","language":"en","end_date":"2023-09-09"}

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
                    'username': ite['user']['username'],
                    'name': ite['user']['name'],
                    'creation_date':ite['creation_date'],
                    'text': ite['text'],
                    'location': ite['user']['location']}
    twitter_append.append(twitter_data)

df24 = pd.DataFrame(twitter_append)

url = "https://twitter154.p.rapidapi.com/search/search"

# 9 Sept
querystring = {"query":"yellowknife evacuation","section":"top","limit":"50","start_date":"2023-09-09","language":"en","end_date":"2023-09-10"}

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
                    'username': ite['user']['username'],
                    'name': ite['user']['name'],
                    'creation_date':ite['creation_date'],
                    'text': ite['text'],
                    'location': ite['user']['location']}
    twitter_append.append(twitter_data)

df25 = pd.DataFrame(twitter_append)

url = "https://twitter154.p.rapidapi.com/search/search"

# 10 Sept
querystring = {"query":"yellowknife evacuation","section":"top","limit":"50","start_date":"2023-09-10","language":"en","end_date":"2023-09-11"}

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
                    'username': ite['user']['username'],
                    'name': ite['user']['name'],
                    'creation_date':ite['creation_date'],
                    'text': ite['text'],
                    'location': ite['user']['location']}
    twitter_append.append(twitter_data)

df26 = pd.DataFrame(twitter_append)

url = "https://twitter154.p.rapidapi.com/search/search"

# 11 Sept
querystring = {"query":"yellowknife evacuation","section":"top","limit":"50","start_date":"2023-09-11","language":"en","end_date":"2023-09-12"}

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
                    'username': ite['user']['username'],
                    'name': ite['user']['name'],
                    'creation_date':ite['creation_date'],
                    'text': ite['text'],
                    'location': ite['user']['location']}
    twitter_append.append(twitter_data)

df27 = pd.DataFrame(twitter_append)

url = "https://twitter154.p.rapidapi.com/search/search"

# 12 Sept
querystring = {"query":"yellowknife evacuation","section":"top","limit":"50","start_date":"2023-09-12","language":"en","end_date":"2023-09-13"}

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
                    'username': ite['user']['username'],
                    'name': ite['user']['name'],
                    'creation_date':ite['creation_date'],
                    'text': ite['text'],
                    'location': ite['user']['location']}
    twitter_append.append(twitter_data)

df28 = pd.DataFrame(twitter_append)

url = "https://twitter154.p.rapidapi.com/search/search"

# 13 Sept
querystring = {"query":"yellowknife evacuation","section":"top","limit":"50","start_date":"2023-09-13","language":"en","end_date":"2023-09-14"}

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
                    'username': ite['user']['username'],
                    'name': ite['user']['name'],
                    'creation_date':ite['creation_date'],
                    'text': ite['text'],
                    'location': ite['user']['location']}
    twitter_append.append(twitter_data)

df29 = pd.DataFrame(twitter_append)

url = "https://twitter154.p.rapidapi.com/search/search"

# 14 Sept
querystring = {"query":"yellowknife evacuation","section":"top","limit":"50","start_date":"2023-09-14","language":"en","end_date":"2023-09-15"}

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
                    'username': ite['user']['username'],
                    'name': ite['user']['name'],
                    'creation_date':ite['creation_date'],
                    'text': ite['text'],
                    'location': ite['user']['location']}
    twitter_append.append(twitter_data)

df30 = pd.DataFrame(twitter_append)

url = "https://twitter154.p.rapidapi.com/search/search"

# 15 Sept
querystring = {"query":"yellowknife evacuation","section":"top","limit":"50","start_date":"2023-09-15","language":"en","end_date":"2023-09-16"}

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
                    'username': ite['user']['username'],
                    'name': ite['user']['name'],
                    'creation_date':ite['creation_date'],
                    'text': ite['text'],
                    'location': ite['user']['location']}
    twitter_append.append(twitter_data)

df31 = pd.DataFrame(twitter_append)

dataframes = [df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14, df15, df16, df17, df18, df19, df20, df21, df22, df23, df24, df25, df26, df27, df28, df29, df30, df31]
combined_df = pd.concat(dataframes, ignore_index=True)
combined_df.to_csv('twitter_data.csv', index=False)
