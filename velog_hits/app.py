import streamlit as st

from crawler import HitsCrawler

IS_EXECUTE = False
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
        st.error("사용자 이름 또는 Access Token을 입력해주세요-!", icon="🔥")
        st.stop()
      else:
        IS_EXECUTE = True

if IS_EXECUTE is False:
  st.stop()

hits_crawler = HitsCrawler(username, access_token)
if hits_crawler.is_exist_user() is False:
  st.error("존재하지 않는 사용자입니다. 확인 부탁드려요-!", icon="😵")
  st.stop()

post_infos = hits_crawler.get_post_infos()
