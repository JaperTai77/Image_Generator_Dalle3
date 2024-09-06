from model import generate_image, generate_image_prompt, process_image_prompt
import streamlit as st
from streamlit_utlis import check_password

if not check_password():
    st.stop()

st.title('Image Generator🐶')
description = st.text_input(r'Describe the image you want. I will give you a few prompt to choose 🐻‍❄️')
prompt = ''

if st.button('GENERATE PROMPT 🐯'):
    st.success('Generating prompts for you, please wait... 🦁')
    response = generate_image_prompt(description)
    result = process_image_prompt(response)

    st.subheader("Here are some prompts for you to use🐧")
    for i in range(len(result)):
        st.code(result[i].replace("- ", ""), language='markdown')

st.divider()

prompt = st.text_input(r"Get a prompt from above or enter your own 🦝")
if st.button('GENERATE IMAGE 🐥'):
    st.success('Generating image for you, please wait... 🐨')
    result = generate_image(prompt)

    st.subheader("Here is your image... 🦭")
    st.image(result, caption=prompt)