from email.mime import image
import streamlit as st
from PIL import Image

st.title('ojizouアプリ')
st.caption('これはojizouのテスト用アプリです。')
st.subheader('自己紹介')
st.text('私はojizouです。')

code = '''
def hello():
    print('Hello, World!')
'''
st.code(code, language='python')

# 画像の表示
image = Image.open('my-notion-face-transparent.png')
st.image(image, width=200)

# reloadを制御するためwith構文を使う
with st.form(key='my_form'):
    # テキストボックス
    name = st.text_input('名前を入力してください。')
    address = st.text_input('住所を入力してください。')

    # マルチセレクトボックス
    hobby = st.multiselect('趣味を選択してください。', ('読書', '映画鑑賞', '旅行', '料理'))

    # セレクトボックス
    age_category = st.selectbox('年齢を選択してください。', ['10代', '20代', '30代', '40代', '50代'])

    # ラジオボタン
    sex = st.radio('性別を選択してください。', ['男性', '女性'])

    # ボタン
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')

    if submit_btn:
        st.text(f'{name}さん、{address}に書籍を送ります！')
        st.text(f'趣味は{"・".join(hobby)}、{age_category}、{sex}ですね。')