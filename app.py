import streamlit as st
import pickle
import pandas as pd
import requests

# Function to fetch movie posters from TMDB API
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

# Function to recommend movies
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies_names = []
    recommended_movies_posters = []
    for i in movies_list:
         movie_id = movies.iloc[i[0]].movie_id
         # Fetch poster from API
         recommended_movies_names.append(movies.iloc[i[0]].title)
         recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies_names, recommended_movies_posters

# Load movies and similarity data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Title for Streamlit App
st.title("Movie Recommender System")

# Dropdown to select a movie
selected_movie_name = st.selectbox(
    'Type or select a movie from the dropdown',
     movies['title'].values
)

# CSS for fixing alignment
st.markdown(
    """
    <style>
    .movie-title {
        height: 50px; /* Fix height for the text container */
        text-align: center;
        overflow: hidden;
        font-size: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Show Recommendations Button
if st.button('Show Recommendations'):
    recommended_movies_names, recommended_movies_posters = recommend(selected_movie_name)

    # Create columns for recommendations
    col1, col2, col3, col4, col5 = st.columns(5)

    # Add movie titles and posters to each column
    with col1:
        st.markdown(f"<div class='movie-title'>{recommended_movies_names[0]}</div>", unsafe_allow_html=True)
        st.image(recommended_movies_posters[0], use_container_width=True)
    with col2:
        st.markdown(f"<div class='movie-title'>{recommended_movies_names[1]}</div>", unsafe_allow_html=True)
        st.image(recommended_movies_posters[1], use_container_width=True)
    with col3:
        st.markdown(f"<div class='movie-title'>{recommended_movies_names[2]}</div>", unsafe_allow_html=True)
        st.image(recommended_movies_posters[2], use_container_width=True)
    with col4:
        st.markdown(f"<div class='movie-title'>{recommended_movies_names[3]}</div>", unsafe_allow_html=True)
        st.image(recommended_movies_posters[3], use_container_width=True)
    with col5:
        st.markdown(f"<div class='movie-title'>{recommended_movies_names[4]}</div>", unsafe_allow_html=True)
        st.image(recommended_movies_posters[4], use_container_width=True)
