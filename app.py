import pickle
import streamlit as st
import pandas as pd

course_link = []


def recommend(course):
    course_index = coursera[coursera['course_name'] == course].index[0]
    distances = similarity[course_index]

    course_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[0:11]

    recommended_course = []
    for i in course_list:
        # fetch link from coursera
        recommended_course.append(coursera.iloc[i[0]].course_name)
        course_link.append(coursera.iloc[i[0]].course_url)
    return recommended_course


coursera = pickle.load(open('coursera.pkl', 'rb'))
coursera_list = coursera['course_name'].values

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("Course Recommender System")

selected_course = st.selectbox(
    "Search fo a Course",
    coursera_list
)

if st.button('Recommend'):
    recommendations = recommend(selected_course)

    for i in range(len(recommendations)):
        df = f'<a target="_blank" href="{course_link[i]}">{recommendations[i]}</a>'
        st.write(df, unsafe_allow_html=True)
