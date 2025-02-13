import streamlit as st

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