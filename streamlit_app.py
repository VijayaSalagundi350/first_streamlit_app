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
# let's put a picklist to allow users to select fruit and want to include
streamlit.multiselect("pick some fruits:", list (my_fruit_list.index))
#display the table on the page
streamlit.dataframe(my_fruit_list)
