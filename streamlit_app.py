import streamlit
import pandas
import requests
import snowflake.connector

streamlit.title("My Parents New Healthy Dinner")

streamlit.header('Breakfast Favourites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

my_cur.execute("select * from fruit_load_list")

my_data_row = my_cur.fetchall()

my_cur.execute("insert into fruit_load_list values('from streamlit')")
