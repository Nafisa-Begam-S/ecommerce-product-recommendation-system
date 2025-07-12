E-Commerce Product Recommendation System App

Created by Nafisa Begam



import streamlit as st

import pandas as pd

from sklearn.metrics.pairwise import cosine\_similarity



\# Load data

events = pd.read\_csv('events.csv')



\# Filter for transaction events

events = events\[events\['event'] == 'transaction']



\# Create user-item matrix

user\_item\_matrix = events.pivot\_table(index='visitorid', columns='itemid', values='transactionid', aggfunc='count', fill\_value=0)



\# Compute item-item cosine similarity

item\_similarity = cosine\_similarity(user\_item\_matrix.T)

item\_similarity\_df = pd.DataFrame(item\_similarity, index=user\_item\_matrix.columns, columns=user\_item\_matrix.columns)



\# Function to get similar items

def get\_similar\_items(item\_id, top\_n=5):

&nbsp;   if item\_id in item\_similarity\_df:

&nbsp;       similar\_scores = item\_similarity\_df\[item\_id].sort\_values(ascending=False)

&nbsp;       similar\_scores = similar\_scores.drop(item\_id)

&nbsp;       return similar\_scores.head(top\_n)

&nbsp;   else:

&nbsp;       return "Item not found in data"



\#  Streamlit App Interface

st.title("🛒 E-Commerce Product Recommendation System")

st.subheader("📊 Created by Nafisa Begam")



\# Dropdown to select an item ID

item\_ids = events\['itemid'].unique()

selected\_item = st.selectbox("Select a Product (Item ID):", item\_ids)



\# Button to get recommendations

if st.button("Recommend Similar Products"):

&nbsp;   recommendations = get\_similar\_items(selected\_item)

&nbsp;   st.write("###  Top Recommended Products:")

&nbsp;   if isinstance(recommendations, str):

&nbsp;       st.error(recommendations)

&nbsp;   else:

&nbsp;       st.table(recommendations)



\# Footer

st.markdown("---")

st.markdown("\*\* Developed with love by Nafisa Begam\*\*")



