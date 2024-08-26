import streamlit as st
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

def scraper_buscalibre(user_input):
    url = "https://www.buscalibre.pe/libros/search/?q="
    url_final = url + user_input

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

    response = requests.get(url_final, headers=headers)

    # Verify response status
    if response.status_code == 200:
        soup = bs(response.text, "html.parser")
        st.write(f"You have searched for '{user_input}'")

        # Store information in lists
        titles = []
        prices_before = []
        prices_now = []
        discounts = []

        for objeto in soup.find_all("div", class_="box-producto"):
            title = objeto.find("h3").text.strip()
            price_before = objeto.find("p", class_="precio-antes").text.strip()
            price_before = price_before.replace("S/  ", "")
            price_before = price_before.replace(",", ".")
            price_before = float(price_before)
            price_now = objeto.find("p", class_="precio-ahora").text.strip()
            price_now = price_now.replace("S/  ", "")
            price_now = price_now.replace(",", ".")
            price_now = float(price_now)

            discount = round((price_before - price_now) / price_before * 100, 2)
            
            titles.append(title)
            prices_before.append(price_before)
            prices_now.append(price_now)
            discounts.append(discount)

        # Create a DataFrame with the results
        df = pd.DataFrame({
            "Title" : titles,
            "Price before" : prices_before,
            "Price now" : prices_now,
            "Discount" : discounts
        })

        # Show dataframe
        st.dataframe(df)

        # Get the book with the minimum price
        min_price_book = df[df['Price now'] == df['Price now'].min()]

        # Get the book with the maximum discount
        max_discount_book = df[df['Discount'] == df['Discount'].max()]

        # Show the book with the minimum price
        st.write(f"The book with the minimum price is **{min_price_book.iloc[0, 0]}** with a total cost of S/{min_price_book.iloc[0, 2]}")

        # Show the book with the maximum discount
        st.write(f"The book with the maximum discount is **{max_discount_book.iloc[0, 0]}** with a discount of {max_discount_book.iloc[0, 3]}% and a total cost of S/{max_discount_book.iloc[0, 2]}")
    
    else:
        st.error(f"Error {response.status_code}: Could not access the website")


