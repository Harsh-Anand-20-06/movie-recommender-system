import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=API_KEY"
    try:
        response = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"}, verify=False)
        response.raise_for_status()
        data = response.json()
        return "https://image.tmdb.org/t/p/w500" + data['poster_path']
    except requests.exceptions.RequestException as e:
        print("Error fetching poster:", e)
        return "https://via.placeholder.com/500x750.png?text=No+Poster"



def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse = True,key = lambda x:x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)  #printing back title of movie based on index
        #fetch poster from api
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters

movies = pickle.load(open('movies.pkl', 'rb'))  #yha new_df aa jayega
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies_list = movies['title'].values


st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    "Movie",
   movies_list,
)

if st.button('Get Movie Recommendations'):
    names,posters = recommend(selected_movie_name)
    cols = st.columns(5)
    for idx, col in enumerate(cols):
        col.text(names[idx])
        col.image(posters[idx])

