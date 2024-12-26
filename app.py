import pickle
import pandas as pd
import streamlit as st

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:7]

    recommended_movie = []
    for i in movies_list:
        movie_id = i[0]
        recommended_movie.append(movies.iloc[i[0]].title)
    return recommended_movie

similarity = pickle.load(open('similarity.pkl','rb'))

movies_dict = pickle.load(open('movie.pkl','rb'))
movies = pd.DataFrame(movies_dict)

st.title('Movies Recommendation system')

selected_movie_name = st.selectbox(
    "Please Select a Movie",
    (movies['title'].values),
)

if st.button("Recommend"):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)

