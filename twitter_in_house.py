#%%
from  selenium import webdriver
from twitter_scraper_selenium import scrape_keyword
import json
import pandas as pd
import asyncio

#%%

def scrape_profile_tweets_since_2023(username: str, driver: webdriver.Chrome):
  kword = "from:" + username
  path = 'C:/Users/patha/OneDrive/Desktop/MS in USA/DSSD Outreach' + username
  file_path = path + '.csv'
  tweets = scrape_keyword(
      headless=True,
      keyword=kword,
      browser="chrome",
      tweets_count=2, # Just last 2 tweets
      filename=path,
      output_format="csv",
      since="2023-01-01",
      # until="2025-03-02", # Until Right now
      driver=driver
  )
  data = pd.read_csv(file_path)
  data = json.loads(data.to_json(orient='records'))
  return data


from multiprocessing import Pool

# Just one account
# scrape_profile_tweets_since_2023('elonmusk')

# Run in parallely
def functionToRunParallely(i):
    global driver
    if driver is None:
        driver = webdriver.Chrome()
    data = scrape_profile_tweets_since_2023(username=i, driver=driver)
    driver.close()
    return data

noOfPools = 5

if __name__ == "__main__":
    driver = webdriver.Chrome()
    with Pool(noOfPools) as p:
        p.map(functionToRunParallely,['elonmusk', 'BarackObama', 'cathiedwood'])
# %%
