from email.mime import image
import streamlit as st
from PIL import Image

st.title('ojizouアプリ')
st.caption('これはojizouのテスト用アプリです。')

image = Image.open('./data/my-notion-face-transparent.png')

st.image(image, width=200)
