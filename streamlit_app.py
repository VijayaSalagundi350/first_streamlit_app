import streamlit

streamlit.title('My Moms new Healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('Omega3 and Blueberry Oatmeal')
streamlit.text('Kale, spinach & Rocket smoothie')
streamlit.text('Hard-boiled free-ranged eggs')
streamlit.text('Avocado Toast')
streamlit.header('Build your own Fruit Smoothie')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# let's put a picklist to allow users to select fruit and want to include
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruit_to_show = my_fruit_list.loc[fruits_selected]
#display the table on the page
streamlit.dataframe(fruit_to_show)
fruits_to_show = my_fruit_list.loc[fruits_selected]

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermemlon")
streamlit.text(fruityvice_response)
