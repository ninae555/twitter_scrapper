# %%%
import pandas as pd
import string
import numpy as np
import py
file_path = 'twitter_data.csv'
df = pd.read_csv(file_path)
# %%
print(df.columns)

#print(df['username'].value_counts())
#print(df['location'].value_counts())
print(df.info())

## %%
print(df.loc[ df['username'] == 'p_communityhub', 'text'])

# %%

df['text_words'] = df['text'].str.split()

print(df.head())
# %%
# Remove Punctuation
df['text_words'] = df['text_words'].apply(lambda text_words: [word.translate(str.maketrans('', '', string.punctuation)) for word in text_words])

# %%
# Finding value_counts for the words
all_words = []
common_words = ['are', 'the', 'to', 'of', 'in', 
                'and', 'a', 'for', 'yellowknife', 
                'evacuation', 'on', 'as', 'is'
                ]
for i in df['text_words']:
    for j in i:
        j = j.lower()
        if j not in common_words:
            all_words.append(j)

all_words = pd.Series(all_words)
# %%
print(all_words.value_counts())
# %%
aid_words = ['donation', 'aid', 'indegenous', 'donate']
k = 0 
for i in df['text_words']:
    for j in i:
        j = j.lower()
        if j in aid_words:
            print(df['text'][k])
    k = k + 1


# %%
print(df['location'].value_counts().loc[lambda x : x> 2])

# %%
## unique user 
u_df = df.groupby('username').first()

# %%
print(u_df['location'].value_counts().loc[lambda x : x> 1])
# %%

u_df['location'] = u_df['location'].replace(['Canada', 'Northern Canada', 'Great White North BeaverLodge', 'Allergic to energy vampires', 'Around the world'], np.nan)
u_df['location'] = u_df['location'].replace(['Yellowknife, NT', "Yellowknife, Northwest Territories", "Northwest Territories, Canada", 'Yellowknife, NT, Canada'], "Yellowknife")
u_df['location'] = u_df['location'].replace(['Toronto, Ontario' , 'Ontario, Canada', '4700 Keele St, Toronto, Canada' ], "Toronto")
u_df['location'] = u_df['location'].replace(['Calgary, Alberta', "Calgary, AB"], "Calgary")
u_df['location'] = u_df['location'].replace(['Edmonton, Alberta, Canada', "Edmonton, Alberta"], "Edmonton")
u_df['location'] = u_df['location'].replace(['Vancouver, British Columbia'], "Vancouver")
u_df['location'] = u_df['location'].replace(['Ottawa, Ontario', 'Ottawa Ontario'], "Ottawa")
u_df['location'] = u_df['location'].replace(['Airdrie, Alberta'], "Airdrie")
u_df['location'] = u_df['location'].replace(['Boston, MA'], "Boston")
# %%
pd.set_option("display.max_rows", None)
loca_df = pd.DataFrame(u_df['location'].value_counts().loc[lambda x : x > 1])
loca_df = loca_df.reset_index()
# %%
import matplotlib.pyplot as pyplot
import matplotlib as mpl

loca_df.plot(kind='barh', x='location', y='count', legend=False)
pyplot.ylabel('Cities')
pyplot.xlabel('# of Users')
pyplot.title('Yellowknife Tweets by Location')
pyplot.show()


# %%

# %%
