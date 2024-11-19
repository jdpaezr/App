import streamlit as st
import pandas as pd
import plotly.express as px

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css") 

st.title("A Random App")
st.subheader("Welcome")

tab1, tab2, tab3 = st.tabs(["Home", "EDA", "Prediction"])

with tab1:
    st.write("Welcome to the Home Page!")
    st.write("Welcome to this app created using streamlit and css. As you can see its a much mre detailed page with color and better graphics")

with tab2:
    st.write("### Exploratory Data Analysis (EDA)")
    
    data = {
        "Genres": ["Pop", "Rock", "Jazz", "Classical"],
        "Danceability": [0.8, 0.6, 0.5, 0.3],
        "Energy": [0.7, 0.8, 0.4, 0.2],
        "Popularity": [85, 78, 65, 50],
        "Tempo": [120, 130, 90, 80]
    }
    df = pd.DataFrame(data)

    # Graph 1: Danceability by Genre
    fig1 = px.bar(df, x="Genres", y="Danceability", title="Danceability by Genre")
    st.plotly_chart(fig1)

    # Graph 2: Energy by Genre
    fig2 = px.bar(df, x="Genres", y="Energy", title="Energy by Genre", color="Genres")
    st.plotly_chart(fig2)

    # Graph 3: Popularity by Genre
    fig3 = px.line(df, x="Genres", y="Popularity", title="Popularity by Genre")
    st.plotly_chart(fig3)

    # Graph 4: Tempo by Genre
    fig4 = px.scatter(df, x="Genres", y="Tempo", title="Tempo by Genre", size="Popularity", color="Genres")
    st.plotly_chart(fig4)

    # Graph 5: Danceability vs Energy
    fig5 = px.scatter(df, x="Danceability", y="Energy", title="Danceability vs Energy", color="Genres", size="Popularity")
    st.plotly_chart(fig5)

with tab3:
    st.write("### Prediction Page")
    st.write("This section will contain the prediction model.")
    st.write("For now, this is a placeholder for future predictions.")
