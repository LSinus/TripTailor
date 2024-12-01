import streamlit as st
from openai import OpenAI
from utils import *
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key = os.getenv("API_KEY")
)



# Titolo dell'app
st.title("TripTAILor")
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def form1():
    with st.form("select_form"):
        def set_page(page):
            st.session_state.step = 2
        # Chiedi la scelta iniziale (solo una selezione)
        travel_type = st.radio(
            "Choose the type of trip:",
            ("Single city", "Itinerant")
        )
        
        # Salva la scelta nella sessione
        st.session_state.travel_type = travel_type
            
            # Clicca "Next" per passare al secondo form
        st.form_submit_button("Next", on_click=set_page, args=['2'])


# Funzione per il secondo form
def form2():

    with st.form("booking_form"):
        col1, col2 = st.columns(2)
    
        with col1:
           place = st.text_input("City", placeholder="E.g. 'Budapest'")
        
        
        with col2:
            period = st.selectbox("Travel period", options=months)

        col3, col4 = st.columns(2)

        with col3:
            duration = st.text_input("Duration", placeholder="E.g. '3 days' or 'one week'")

        with col4:
            num_people = st.text_input("Number of people", placeholder="E.g. '2 Adults and 2 kids', '3 Adults'")

        
        interests = st.text_area("Interests of journey", placeholder="E.g. 'Historical Sites, Typical Restaurants...'\n'Tell me a travel itinerary with green choices for transportation'")
        
        col5, col6 = st.columns(2)
        
        with col5:
            price = st.text_area("Price range", placeholder="E.g. 'I would like to spend a maximum of 30€ per person on food'\n'My budget for museums is 200€'")

        with col6:
            others = st.text_area("Other specifications", placeholder="E.g. 'Tell me the names of the restaurants'\n'Include activities that children might enjoy'")

        confirm = st.form_submit_button("Get Ideas")

        if confirm:
            form_data = {
                "place": place,
                "period": period,
                "interests": interests,
                "duration": duration,
                "price": price,
                "num_people": num_people,
                "others": others
            }
            prompt = create_prompt(form_data)
            with st.spinner("Travelling..."):
                response = query_chatgpt(prompt, client)
            st.success("Results:")
            st.write(response)
            
            st.form_submit_button("Generate PDF!")
        


if "step" not in st.session_state:
    st.session_state.step = 1  # Imposta il passo iniziale

# Mostra il form in base al passo attuale
if st.session_state.step == 1:
    form1()
elif st.session_state.step == 2:
    form2()






