# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import streamlit as st
import plotly.express as px
import pandas as pd
import plotly.figure_factory as ff



df = px.data.gapminder()
st.dataframe(df)
listaPaises = df["country"].unique().tolist()
st.write(listaPaises)
#data_canada = px.data.gapminder().query("country == 'Canada'")
#fig = px.bar(data_canada, x='year', y='pop')
pais="Canada"
with st.sidebar:
    pais = st.selectbox("Paises",listaPaises)
    st.write(pais)

datosPais = df.query("country == '"+pais+"'")
fig = px.bar(datosPais, x='year', y='pop')
st.plotly_chart(fig, use_container_width=True)

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    st.header("Hola desde Streamlit!")
    st.subheader("Probando..1..2..3")
    st.write("Hola,Soy Edwin")
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Edwin')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
