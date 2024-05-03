import streamlit as st
from langchain_helper import generate_restaurant_name_and_items

def main():
    st.title("Restaurant Name Generator")

    cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian", "Italian", "Mexican", "Arabic", "American"))

    if cuisine:
        response = generate_restaurant_name_and_items(cuisine)
        st.write("---")
        st.header(response['restaurant_name'].strip())
        st.subheader("Menu Items")
        menu_items = response['menu_items'].strip().split(",")
        for idx, item in enumerate(menu_items, start=1):
            st.write(f"{idx}. {item.strip()}")

if __name__ == "__main__":
    main()
