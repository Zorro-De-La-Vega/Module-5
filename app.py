import streamlit as st
import os
import together

st.set_page_config(page_title="Together AI Python Code Generator", layout="centered")
st.title("Together AI Python Code Generator")

st.markdown("""
This app uses Together AI to generate Python code from your description.\n
Enter a prompt describing the Python code you want to generate, and click **Generate**.
""")

api_key = os.environ.get("TOGETHER_API_KEY")
if not api_key:
    api_key = st.text_input("Enter your Together AI API Key", type="password")

prompt = st.text_area("Describe the Python code you want to generate:", "Write a Python script to reverse a string.")

if st.button("Generate"):
    if not api_key:
        st.error("Please enter your Together AI API Key.")
    elif not prompt.strip():
        st.error("Please enter a prompt.")
    else:
        with st.spinner("Generating code..."):
            client = together.Together(api_key=api_key)
            response = client.chat.completions.create(
                model="meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
                messages=[{"role": "user", "content": prompt}]
            )
            code = response.choices[0].message.content
            st.code(code, language="python")
            st.success("Code generated!")
