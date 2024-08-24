import streamlit as st
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

# Título de la aplicación
st.title("Web Scraper de Buscalibre")

# Entrada del usuario
user_input = st.text_input("¿Qué tema/autor te interesa?")

if user_input:
    # URL para hacer el scraping
    url = "https://www.buscalibre.pe/libros/search/?q="
    url_final = url + user_input

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

    response = requests.get(url_final, headers=headers)

    # Verificar que la respuesta es exitosa
    if response.status_code == 200:
        soup = bs(response.text, "html.parser")
        st.write(f"Has buscado el tema '{user_input}'")

        # Listas para almacenar la información
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

        # Crear un DataFrame con los resultados
        df = pd.DataFrame({
            "Título" : titles,
            "Precio antes" : prices_before,
            "Precio ahora" : prices_now,
            "Descuento" : discounts
        })

        # Mostrar el DataFrame
        st.dataframe(df)

        # Obtener el libro con el precio mínimo
        min_price_book = df[df['Precio ahora'] == df['Precio ahora'].min()]

        # Obtener el libro con el máximo descuento
        max_discount_book = df[df['Descuento'] == df['Descuento'].max()]

        # Mostrar el libro con el precio mínimo
        st.write(f"El libro con el precio mínimo es **{min_price_book.iloc[0, 0]}** con un costo de S/{min_price_book.iloc[0, 2]}")

        # Mostrar el libro con el máximo descuento
        st.write(f"El libro con el máximo descuento es **{max_discount_book.iloc[0, 0]}** con un descuento de {max_discount_book.iloc[0, 3]}% y un costo de S/{max_discount_book.iloc[0, 2]}")
    else:
        st.error(f"Error {response.status_code}: No se pudo acceder al sitio web")
