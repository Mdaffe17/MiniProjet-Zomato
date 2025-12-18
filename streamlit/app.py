import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("../data/zomato_sample.csv", encoding="latin-1")

st.title("Restaurants à Bengaluru – Analyse Zomato")

fig1 = px.histogram(df, x="rate", title="Distribution des notes")
st.plotly_chart(fig1)

fig2 = px.box(df, y="approx_cost(for two people)", title="Coût pour deux personnes")
st.plotly_chart(fig2)

top_locations = df["location"].value_counts().head(10)
fig3 = px.bar(
    x=top_locations.values,
    y=top_locations.index,
    title="Top 10 quartiers par nombre de restaurants"
)
st.plotly_chart(fig3)
