# %%
# Imports
import pandas as pd
from datetime import datetime
import re
import matplotlib.pyplot as plt

#%% 
from textblob import TextBlob
import spacy
from gensim import corpora, models
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
import seaborn as sns
from multiprocessing import freeze_support

# %%%

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

# %%

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

# %% 
# Import the wordcloud library
from wordcloud import WordCloud
# Join the different processed titles together.
long_string = ','.join(list(twitter_data['text_normalized'].values))
# Create a WordCloud object
wordcloud = WordCloud(background_color="white", max_words=5000, contour_width=3, contour_color='steelblue')
# Generate a word cloud
wordcloud.generate(long_string)
# Visualize the word cloud
wordcloud.to_image()
# %%
print(long_string)
# %%
import gensim
from gensim.utils import simple_preprocess
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
stop_words.extend(['from', 'subject', 're', 'edu', 'use', 'https', 'tco'])
def sent_to_words(sentences):
    for sentence in sentences:
        # deacc=True removes punctuations
        yield(gensim.utils.simple_preprocess(str(sentence), deacc=True))
def remove_stopwords(texts):
    return [[word for word in simple_preprocess(str(doc)) 
             if word not in stop_words] for doc in texts]
data = twitter_data.text_normalized.values.tolist()
data_words = list(sent_to_words(data))
# remove stop words
data_words = remove_stopwords(data_words)
print(data_words[:1][0][:30])


# %%
import gensim.corpora as corpora
# Create Dictionary
id2word = corpora.Dictionary(data_words)
# Create Corpus
texts = data_words
# Term Document Frequency
corpus = [id2word.doc2bow(text) for text in texts]
# View
print(corpus[:1][0][:30])
# %%
from pprint import pprint
# number of topics
num_topics = 5
# Build LDA model
lda_model = gensim.models.LdaMulticore(corpus=corpus,
                                       id2word=id2word,
                                       num_topics=num_topics)
# Print the Keyword in the 5 topics
pprint(lda_model.print_topics())
doc_lda = lda_model[corpus]
# %%

# %%
