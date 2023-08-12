import streamlit as st
import pickle
# st.markdown("<style>body{background-color:Blue;}<style/>",unsafe_allow_html=True)

movies_list = pickle.load(open('movies.pkl', 'rb'))
movies_title = movies_list['title']

similarity = pickle.load(open('similarity.pkl', 'rb'))


def recommend(movies):
    movie_index = movies_list[movies_title == movies].index[0]
    movie_list = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])[1:6]

    recommeneded_movies = []

    for i in movie_list:
        recommeneded_movies.append(movies_list.iloc[i[0]].title)
    return recommeneded_movies


st.title("Movie Recommender System")


selected_movie = st.selectbox('Select your movie',movies_title)

if st.button('Recommend'):
    recommenedation = recommend(selected_movie)
    for i in recommenedation:
        st.write(i)