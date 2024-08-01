import altair as alt
import streamlit as st

from crawler import HitsCrawler

st.set_page_config(page_title="Velog Hits", page_icon="🍕", layout="wide")

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

with st.spinner('🍀 데이터를 가져오는 중입니다. 잠시만 기다려 주세요-!'):
  post_infos = hits_crawler.get_post_infos()
  st.balloons()

tab_views, tab_comments, tab_likes = st.tabs(["📈 조회수 순위", "💬 댓글 순위", "♥️ 좋아요 순위"])

chart_views = alt.Chart(post_infos).mark_bar().encode(
  x=alt.X("total", title="조회수"),
  y=alt.Y("title", title="제목", sort="-x"),
  color=alt.Color("total", scale=alt.Scale(scheme="reds"), legend=None),
  tooltip=[alt.Tooltip("title", title="제목"), alt.Tooltip("total", title="조회수", format="d")]
)

chart_comments = alt.Chart(post_infos).mark_bar().encode(
  x=alt.X("comments_count", title="댓글", axis=alt.Axis(format='d')),
  y=alt.Y("title", title="제목", sort="-x"),
  color=alt.Color("comments_count", scale=alt.Scale(scheme="reds"), legend=None),
  tooltip=[alt.Tooltip("title", title="제목"), alt.Tooltip("comments_count", title="댓글", format="d")]
)

chart_likes = alt.Chart(post_infos).mark_bar().encode(
  x=alt.X("likes", title="좋아요", axis=alt.Axis(format='d')),
  y=alt.Y("title", title="제목", sort="-x"),
  color=alt.Color("likes", scale=alt.Scale(scheme="reds"), legend=None),
  tooltip=[alt.Tooltip("title", title="제목"), alt.Tooltip("likes", title="좋아요", format="d")]
)

with tab_views:
  st.altair_chart(chart_views, use_container_width=True)

with tab_comments:
  st.altair_chart(chart_comments, use_container_width=True)

with tab_likes:
  st.altair_chart(chart_likes, use_container_width=True)
