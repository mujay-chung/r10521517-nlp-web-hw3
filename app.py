'''
R10521517 鍾慕捷
NLP and Web Applications hw3
'''

import streamlit as st
import pandas as pd
import numpy as np
import re

# data
df = pd.read_csv('spells_without_dash.csv')
df.drop('Unnamed: 0', inplace=True, axis=1)


st.title('Harry Potter All-Spell Wiki For Muggles')
st.markdown("""
### All Spell List
""")
st.dataframe(df)
# st.table(df)

# filter by types
types = st.sidebar.multiselect (
  "Choose Type of Spells",
  options=['Spell', 'Charm', 'Curse', 'Jinx', 'Hex', 'Enchantment'],
  default=['Spell', 'Charm', 'Curse', 'Jinx', 'Hex', 'Enchantment']
)
type_filt = df['Type'].isin(types)

# create a text box for keyword search
text_box = st.sidebar.text_input('Input your keyword (EX. "water"), press ENTER to search')

# search for keywords
keyword_filt = df['Effect'].str.contains(text_box, flags=re.IGNORECASE)

# filter the data based on all criteria
filt_df = df[(type_filt) & (keyword_filt)]


# show result
st.markdown("""
### Search Results
""")
st.dataframe(filt_df, 800, 400)
