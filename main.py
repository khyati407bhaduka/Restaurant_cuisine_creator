
import streamlit as st
st.title("Restaurant Name Generator")
cuisine = st.sidebar.selectbox("Pick your favourite cuisine",("Indian","American","Italian","Arabic"))

import langchain_function_helper
if cuisine :
    response = langchain_function_helper.genarte_restaurant(cuisine)
    st.header(response["restaurant_name"])
    restaurant_menu=response["restaurant_menu"].split(",")
    st.write("menu items for this restuarnt")
    for item in restaurant_menu:
        st.write("-",item)
