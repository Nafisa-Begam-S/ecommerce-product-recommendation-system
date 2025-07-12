import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Page config
st.set_page_config(page_title="E-Commerce Product Recommender", page_icon="🛒")

st.title("🛒 E-Commerce Product Recommendation System")
st.write("A simple recommendation system using product names and cosine similarity.")

# Sample product data (for demo — replace with your product dataset)
data = {
    'itemid': [101, 102, 103, 104, 105],
    'product_name': [
        'Wireless Mouse',
        'Gaming Keyboard',
        'USB Type-C Cable',
        'Laptop Cooling Pad',
        'Wireless Headphones'
    ]
}

df = pd.DataFrame(data)

# Vectorizing product names
vectorizer = CountVectorizer()
count_matrix = vectorizer.fit_transform(df['product_name'])

# Compute Cosine Similarity
cosine_sim = cosine_similarity(count_matrix)

# Function to get recommendations
def recommend(product_name):
    try:
        idx = df[df['product_name'] == product_name].index[0]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:4]  # Top 3 recommendations

        product_indices = [i[0] for i in sim_scores]
        return df['product_name'].iloc[product_indices].tolist()
    except:
        return ["No similar products found."]

# App UI
product_list = df['product_name'].tolist()
selected_product = st.selectbox("Select a product to get recommendations:", product_list)

if st.button("Recommend"):
    recommendations = recommend(selected_product)
    st.subheader("Recommended Products:")
    for rec in recommendations:
        st.write("✅ " + rec)
