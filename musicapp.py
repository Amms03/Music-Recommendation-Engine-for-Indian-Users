
import streamlit as st


# Define a Reader object
user = user(rating_scale=(1, 5))

# Load data into Surprise Dataset
data = Dataset.load_from_df(dataset.csv, reader)

# Split the data into training and testing sets
trainset, testset = train_test_split(data, test_size=0.2)

# Choose a collaborative filtering algorithm
algo = SVD()

# Train the model
algo.fit(trainset)

# Function to get music recommendations for a user
def get_recommendations(user_id, n=10):
    user_ratings = []
    for item_id in your_data['item_id'].unique():
        user_ratings.append((item_id, algo.predict(user_id, item_id).est))

    # Sort by estimated rating and get top n recommendations
    recommendations = sorted(user_ratings, key=lambda x: x[1], reverse=True)[:n]

    return recommendations

# Streamlit app
st.title("Music Recommender System")

# User input for user ID
user_id = st.text_input("Enter your user ID:", 1)

# Get recommendations when the user clicks the button
if st.button("Get Recommendations"):
    try:
        user_id = int(user_id)
        recommendations = get_recommendations(user_id)
        st.write(f"Top 10 Recommendations for User {user_id}:")
        for i, (item_id, rating) in enumerate(recommendations, start=1):
            st.write(f"{i}. Item ID: {item_id}, Estimated Rating: {rating:.2f}")
    except ValueError:
        st.error("Please enter a valid user ID.")

