import streamlit as st


with st.sidebar:
    with st.form(key='form', border=False):
        username = st.text_input(
            label="사용자 이름을 입력해주세요👇",
            placeholder="username"
        )

        access_token = st.text_input(
            label="Access Token 값을 입력해주세요👇",
            placeholder="access token"
        )

        submit = st.form_submit_button(label="데이터 가져오기")
        if submit:
            if not username or not access_token:
                st.error("사용자 이름 또는 Access Token을 입력해주세요:)")