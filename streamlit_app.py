import streamlit
import pandas
import requests
import snowflake.connector

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
