import streamlit as st
import pickle
import numpy as np

# --- Modell & Vektorizer laden ---
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("tfidf.pkl", "rb") as f:
    tfidf = pickle.load(f)

# --- App UI ---
st.set_page_config(page_title="Hotelbewertungs-Analyse", layout="centered")

st.title("🏨 Sentiment-Analyse für Hotelbewertungen")
st.write("Diese App analysiert, ob eine Bewertung **positiv** oder **negativ** ist.")

# Texteingabe
user_input = st.text_area("✍️ Bewertung eingeben:", height=150)

if st.button("🔍 Analyse starten"):
    if user_input.strip() == "":
        st.warning("Bitte eine Bewertung eingeben.")
    else:
        # Text vektorisieren
        input_vector = tfidf.transform([user_input])

        # Vorhersage
        prediction = model.predict(input_vector)[0]
        proba = model.predict_proba(input_vector)[0]

        # Ausgabe
        if prediction == 1:
            st.success("💚 Ergebnis: **Positive Bewertung**")
        else:
            st.error("❤️ Ergebnis: **Negative Bewertung**")

        st.markdown(f"**Wahrscheinlichkeit positiv:** `{proba[1]*100:.2f}%`")
