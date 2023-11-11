# Imports
import pandas as pd
from datetime import datetime
import re
import matplotlib.pyplot as plt
from textblob import TextBlob
import spacy
from gensim import corpora, models
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
import seaborn as sns
from multiprocessing import freeze_support

# import dash
# from dash import dcc, html
# import plotly.express as px


# Load the CSV file
file_path = 'twitter_data.csv'
twitter_data = pd.read_csv(file_path)

# Display basic information about the dataset
dataset_info = twitter_data.info()

# Display the first few rows of the dataset
sample_data = twitter_data.head()

dataset_info, sample_data

# Preprocessing steps

# Convert 'creation_date' to datetime
twitter_data['creation_date'] = pd.to_datetime(
    twitter_data['creation_date'], format="%a %b %d %H:%M:%S %z %Y")

# Normalize the text: lowercase, remove punctuation and numbers, strip leading/trailing spaces
twitter_data['text_normalized'] = twitter_data['text'].str.lower()
twitter_data['text_normalized'] = twitter_data['text_normalized'].apply(
    lambda x: re.sub(r'[\d.,!?"\':;]', '', x))
twitter_data['text_normalized'] = twitter_data['text_normalized'].str.strip()

# Display the types of each column to confirm the changes and the first few rows of normalized text
twitter_data.dtypes, twitter_data[['text', 'text_normalized']].head()

# Sentiment Analysis
# Function to get the sentiment polarity


def get_sentiment(text):
    return TextBlob(text).sentiment.polarity


# Apply the function to your dataframe
twitter_data['sentiment'] = twitter_data['text_normalized'].apply(
    get_sentiment)


sentiment_time_series = twitter_data.groupby(twitter_data['creation_date'].dt.date)[
    'sentiment'].mean().reset_index()

# Plotting the sentiment trend over time
plt.figure(figsize=(14, 7))
plt.plot(sentiment_time_series['creation_date'],
         sentiment_time_series['sentiment'], marker='o')
plt.title('Sentiment Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Average Sentiment')
plt.xticks(rotation=45)
plt.tight_layout()  # Adjust layout to prevent clipping of xlabel
plt.show()


# Load the pre-trained spaCy model
nlp = spacy.load("en_core_web_sm")

# Function to extract entities from a tweet


def extract_entities(tweet):
    doc = nlp(tweet)
    return [(ent.text, ent.label_) for ent in doc.ents]


# Apply the function to the tweets
twitter_data['entities'] = twitter_data['text_normalized'].apply(
    extract_entities)

# Apply Topic Modeling
# Function to preprocess text for topic modeling


def preprocess(text):
    return [token for token in simple_preprocess(text) if token not in STOPWORDS]


# Preprocess the text
processed_docs = twitter_data['text_normalized'].map(preprocess)

# Create a dictionary representation of the documents
dictionary = corpora.Dictionary(processed_docs)
dictionary.filter_extremes(no_below=15, no_above=0.5, keep_n=100000)

# Create a bag-of-words model for each document
bow_corpus = [dictionary.doc2bow(doc) for doc in processed_docs]

# Create an LDA model
lda_model = models.LdaMulticore(
    bow_corpus, num_topics=10, id2word=dictionary, passes=2, workers=2)

# Display the topics
for idx, topic in lda_model.print_topics(-1):
    print('Topic: {} \nWords: {}'.format(idx, topic))

# Assign Tweets to Topics


def assign_topics_to_tweets(lda_model, bow_corpus):
    topics = [sorted(lda_model[bow], key=lambda x: -x[1])[0][0]
              for bow in bow_corpus]
    return topics


if __name__ == '__main__':
    freeze_support()
    main()


twitter_data['topic'] = assign_topics_to_tweets(lda_model, bow_corpus)

# Calculate the Average Sentiment for Each Topic
average_sentiment_per_topic = twitter_data.groupby(
    'topic')['sentiment'].mean().reset_index()

# Visualize
# Create a line plot for sentiment over time for each topic
plt.figure(figsize=(15, 8))
sns.lineplot(x='creation_date', y='sentiment', hue='topic', data=twitter_data)

plt.title('Sentiment Trend Over Time by Topic')
plt.xlabel('Date')
plt.ylabel('Average Sentiment')
plt.legend(title='Topic')
plt.show()

# Define the list of keywords related to resilience and recovery
keywords = ["recover", "rebuild", "return to normal",
            "resilience", "aid", "support", "heal", "restore"]

# Function to count the occurrences of keywords in the tweets


def count_keywords(text, keywords):
    return sum(text.count(keyword) for keyword in keywords)


# Count occurrences of keywords in each tweet
twitter_data['keyword_count'] = twitter_data['text_normalized'].apply(
    lambda text: count_keywords(text, keywords))

# Group by creation_date to see the frequency of keywords over time
keyword_time_series = twitter_data.groupby(twitter_data['creation_date'].dt.date)[
    'keyword_count'].sum().reset_index()

# Plotting the time series of keyword frequency
plt.figure(figsize=(14, 7))
plt.plot(keyword_time_series['creation_date'],
         keyword_time_series['keyword_count'], marker='o')
plt.title('Frequency of Resilience-Related Keywords Over Time')
plt.xlabel('Date')
plt.ylabel('Frequency of Keywords')
plt.xticks(rotation=45)
plt.tight_layout()  # Adjust layout to prevent clipping of xlabel
plt.show()
