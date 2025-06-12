
import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(page_title="From Old to Bold")

# --- Custom Style ---
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Syne&display=swap');

        html, body, [class*="css"]  {
            font-family: 'Syne', sans-serif;
            background-color: #ffffff;
            color: #000000;
        }

        .boxed {
            border: 1px solid #cccccc;
            border-radius: 12px;
            padding: 2rem;
            margin-top: 2rem;
            background-color: #f9f9f9;
        }

        .center-logo {
            display: flex;
            justify-content: center;
            margin-bottom: 1rem;
        }

        .external-button {
            display: flex;
            justify-content: center;
            margin-bottom: 2rem;
        }

        .external-button a {
            background-color: black;
            color: white;
            padding: 10px 18px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: bold;
        }

        .external-button a:hover {
            background-color: #333;
        }
    </style>
""", unsafe_allow_html=True)

# --- Logo zentriert ---
st.markdown('<div class="center-logo"><img src="logo.png" width="180"></div>', unsafe_allow_html=True)

# --- Button unter Logo ---
st.markdown("""
<div class="external-button">
    <a href="https://eager-transform-667249.framer.app/" target="_blank">What is From Old to Bold</a>
</div>
""", unsafe_allow_html=True)

# --- Start Boxed Content ---
st.markdown('<div class="boxed">', unsafe_allow_html=True)

# Material-Auswahl
material = st.selectbox("Select material", ["Silver", "Gold", "Other"])
if material == "Other":
    custom_material = st.text_input("Please specify the material")

# Bild-Upload
uploaded_file = st.file_uploader("Upload an image of your old jewelry", type=["jpg", "jpeg", "png"])

def predict_weight(image):
    return 15.0  # Platzhalter

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded image", use_container_width=True)
    weight = predict_weight(image)
    st.write(f"**Estimated weight:** {weight:.2f} grams")

    df = pd.read_csv("designs.csv")
    tolerance = 0.7
    matched = df[
        (abs(df["weight"] - weight) <= tolerance) &
        (df["material"].str.lower() == material.lower())
    ]

    st.subheader("Matching designs:")
    if not matched.empty:
        for _, row in matched.iterrows():
            st.image(row["filename"], caption=f"{row['name']} – {row['weight']} g", use_container_width=True)
    else:
        st.write("No matching designs found.")

# --- End Boxed Content ---
st.markdown('</div>', unsafe_allow_html=True)
