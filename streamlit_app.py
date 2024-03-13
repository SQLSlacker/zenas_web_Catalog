# Import python packages
import streamlit as st
import snowflake.connector
import pandas

streamlit.title('Zena\'s Amazing Athleisure Catalog')

cnx = st.connection("snowflake")
session = cnx.session

my_cur = cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(),CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
