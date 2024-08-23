import os
import json
import streamlit as st
import openai
from dotenv import load_dotenv
import re  
from openai import OpenAI

# Configuración de Streamlit
st.set_page_config(page_title="Chatbot 💬", layout="centered")

with st.sidebar:
    st.title('Interactive Chatbot')
    st.markdown('''
    ## About this bot
    This is a chatbot that allows you to talk about the economic, political and social situation of Peru.
    The PDFs are loaded in this database: https://drive.google.com/drive/folders/1jvad9cFABAtXFTRwkjMPiwqVM1uQx9zC?usp=sharing
                ''')

load_dotenv()

# Define load_chunks_from_json function
def load_chunks_from_json(input_file='data/docs_chunks.json'):
    with open(input_file, 'r', encoding='utf-8') as f:
        docs_chunks = json.load(f)
    return docs_chunks

# Load the chunks from the JSON file
docs_chunks = load_chunks_from_json('data/docs_chunks.json') # Load the chunks from the JSON file

def main():
    st.header("Chat with Database 💬")

# Define the system_prompt
system_prompt = """
You are an expert in the documents provided, which are documents regarding the history and current state of Peruvian economy and society. 
Answer the questions based on the data in the documents."""

if "messages" not in st.session_state:
    st.session_state["messages"] = []

prompt = st.text_input("Your inquiry:", "")


openai.api_key = st.secrets['openai_key']

def find_relevant_chunks(question, docs_chunks, max_chunks=5):
    # Tokeniza la pregunta para extraer palabras clave significativas
    question_keywords = set(re.findall(r'\w+', question.lower()))
    relevance_scores = []

    # Calcula un puntaje de relevancia para cada chunk (puede ser el conteo de palabras clave coincidentes)
    for chunk in docs_chunks:
        chunk_text = chunk["content"].lower()
        chunk_keywords = set(re.findall(r'\w+', chunk_text))
        common_keywords = question_keywords.intersection(chunk_keywords)
        relevance_scores.append((len(common_keywords), chunk))

    # Ordena los chunks por su puntaje de relevancia, de mayor a menor
    relevant_chunks = [chunk for _, chunk in sorted(relevance_scores, key=lambda x: x[0], reverse=True)]

    # Retorna los top N chunks más relevantes
    return relevant_chunks[:max_chunks]

def send_question_to_openai(question, docs_chunks):
    # Encuentra los chunks más relevantes para la pregunta
    relevant_chunks = find_relevant_chunks(question, docs_chunks)
    
    # Construye el prompt completo con el system_prompt y los chunks de texto relevantes
    prompt_text = system_prompt + "\n\n" + "\n\n".join([chunk["content"] for chunk in relevant_chunks]) + "\n\nQuestion: " + question

    # Llama a la API de OpenAI con el prompt para chat
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ]
    )
    
    # Return the message content directly
    return response.choices[0].message.content

if st.button("Send"):
    if prompt:  # Check if the prompt is not empty
        user_message = {"role": "user", "content": prompt}
        st.session_state.messages.append(user_message)

        with st.spinner("Generating answer..."):
            response_text = send_question_to_openai(prompt, docs_chunks)
            if response_text:  # Check if the response_text is not None or empty
                assistant_message = {"role": "assistant", "content": response_text}
                st.session_state.messages.append(assistant_message)
            else:
                st.error("Failed to get a response.")  # Display an error if no response was received

# Display the messages
for index, message in enumerate(st.session_state.messages):
    if message["role"] == "user":
        st.text_area("Question", value=message["content"], height=75, disabled=True, key=f"user_{index}")
    elif message["role"] == "assistant":  # Ensure this is an 'elif' to check specifically for "assistant" role
        st.text_area("Answer", value=message["content"], height=100, disabled=True, key=f"assistant_{index}")

if __name__ == "__main__":
    main()