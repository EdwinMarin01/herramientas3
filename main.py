# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import streamlit as st
import plotly.express as px
import pandas as pd
import plotly.figure_factory as ff
import accessAPI as servicio
import json
import pandas as pd

data_path = 'data_set/data_banco.csv'
df_banco = pd.read_csv(data_path)
listaJob = df_banco['job'].unique().tolist()
listaMarital = df_banco['marital'].unique().tolist()
listaEducation = df_banco['education'].unique().tolist()
listaDefault = df_banco['default'].unique().tolist()
listaHousing = df_banco['housing'].unique().tolist()
listaLoan = df_banco['loan'].unique().tolist()
listaContact = df_banco['contact'].unique().tolist()
listaMonth = df_banco['month'].unique().tolist()
listaDayOfWeek = df_banco['day_of_week'].unique().tolist()
listaPoutcome = df_banco['poutcome'].unique().tolist()


st.title('Predicción de Créditos Bancarios')
st.write('By Edwin Antonio Marín Manzanero')

# Define the form fields
age = st.slider('Age', 16, 100, 25)
job = st.selectbox('Job', listaJob)
marital = st.selectbox('Marital', listaMarital)
education = st.selectbox('Education', listaEducation)
default = st.selectbox('Default', listaDefault)
housing = st.selectbox('Housing', listaHousing)
loan = st.selectbox('Loan', listaLoan)
contact = st.selectbox('Contact', listaContact)
month = st.selectbox('Month', listaMonth)
day_of_week = st.selectbox('Day_of_week', listaDayOfWeek)
duration = st.slider('Duration', 0, 5000, 4050)
campaign = st.slider('Campaign', 0, 60, 40)
pdays = st.slider('Pdays', 0, 1000,490)
previous = st.slider('Previous', 0, 10,7)
poutcome = st.selectbox('Poutcome', listaPoutcome)
emp_var_rate = st.slider('Emp. Var. Rate', -4.0, 2.0,-1.5)
cons_price_idx = st.slider('Cons. Price. Idx', 90.000, 95.000,94.203)
cons_conf_idx = st.slider('Cons. Conf. Idx', -51.00, -25.00,-35.40)
euribor3m = st.slider('Euribor3m', 0.000, 6.000,4.120)
nr_employed = st.slider('Nr.employed', 4900.0, 5300.0,4991.6)

if st.button('Predict'):
    result = servicio.llamarServicio(age, job, marital, education, default, housing, loan, contact, month, day_of_week,
                                     duration, campaign, pdays, previous, poutcome, emp_var_rate, cons_price_idx,
                                     cons_conf_idx, euribor3m, nr_employed)
    result2 = json.loads(result.decode("utf-8"))
    resultado = result2["Results"][0]
    if resultado == "yes":
        st.success("Apto para recibir credito bancario")
    else:
        st.error("No apto para recibir credito bancario")
