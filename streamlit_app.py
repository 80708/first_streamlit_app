import streamlit
streamlit.title('myparents new healthy dinner')
streamlit.title ('🥣 i know iam good')
streamlit.header('🥗 🐔 🥑🍞Breakfast Menu')
streamlit.text('🐔 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥑Kale, Spinach & Rocket Smoothie')
streamlit.text('🍞BHard-Boiled Free-Range Egg')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
