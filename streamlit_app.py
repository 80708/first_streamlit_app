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

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['avacado','strawberries']

# Display the table on the page
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_to_show = my_fruit_list.loc[fruits_selected]
