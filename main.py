import streamlit as st
import pickle
import requests
# from sklearn.feature_extraction.text import CountVectorizer


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    recommend_Movies=[]
    recommended_movie_posters = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommend_Movies.append(movies.iloc[i[0]].title)
    return recommended_movie_posters,recommend_Movies




movies=pickle.load(open('movie_list.pkl','rb'))
# similarity=pickle.load(open("similarity.pkl",'rb'))
# cv = CountVectorizer(max_features=10000,stop_words='english')
# from sklearn.metrics.pairwise import cosine_similarity
# vector = cv.fit_transform(movies['tags']).toarray()
# similarity = cosine_similarity(vector)


st.title("Movie Recommandor System")
Movies_Name = st.selectbox('How would you like to recomend movies?',movies['title'].values)

if st.button('recommend'):
#     recommended_movie_posters,recommend_Movies=recommend(Movies_Name)
#     col1, col2, col3, col4, col5 = st.columns(5)
#     with col1:
#         st.text(recommend_Movies[0])
#         st.image(recommended_movie_posters[0])
#     with col2:
#         st.text(recommend_Movies[1])
#         st.image(recommended_movie_posters[1])

#     with col3:
#         st.text(recommend_Movies[2])
#         st.image(recommended_movie_posters[2])
#     with col4:
#         st.text(recommend_Movies[3])
#         st.image(recommended_movie_posters[3])
#     with col5:
#         st.text(recommend_Movies[4])
#         st.image(recommended_movie_posters[4])
#

