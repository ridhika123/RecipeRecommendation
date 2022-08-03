
pip install import-ipynb
pip install selenium
pip install nltk
pip install unidecode
pip install gensim
pip install sklearn

import streamlit as st
import pandas as pd
import numpy as np
# from streamlit import SessionState
# import SessionState
import os
# from PIL import Image

import import_ipynb

# import config, rec_sys
from Cleaning_Data import ingredient_cleaner
from recommendation_final import get_recs

import nltk

st.header("Food Recommendation System: Sanjeev Kapoor Recipes")
st.text("By Ridhika Agrawal")

# Input bar 1
ingredients = st.text_input("Enter ingredients separated by a comma (example entered):",
                            "peanut, honey, chocolate")

if st.button("Generate Recommendation!"):
    recipe = get_recs(ingredients, mean=True)
    recipe_without_score = recipe[['recipe', 'ingredients', 'url', 'preperation_time', 'cook_time', 'serves', 'level_of_cooking', 'taste']]
    st.table(recipe_without_score)
    # st.text("1. \nline")
    # st.header(recipe['recipe'][0]) 
    # recipe['ingredients'][0], recipe['url'][0], recipe['preperation_time'][0], recipe['cook_time'][0], recipe['level_of_cooking'][0], recipe['taste'][0]
    