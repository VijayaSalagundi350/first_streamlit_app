import streamlit

streamlit.title('My Moms new Healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('Omega3 and Blueberry Oatmeal')
streamlit.text('Kale, spinach & Rocket smoothie')
streamlit.text('Hard-boiled free-ranged eggs')
streamlit.text('Avacado Toast')
streamlit.header('Build your own Fruit Smoothie')

import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
