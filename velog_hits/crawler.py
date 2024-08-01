import asyncio
import json

import aiohttp
import pandas as pd
import requests
import streamlit as st

from graphql import graphql_posts, graphql_get_status

LIMIT = 50


class HitsCrawler:
  def __init__(
      self,
      username,
      access_token
  ) -> None:
    self.username = username
    self.url = f"https://velog.io/@{username}/"
    self.access_token = access_token
    self.headers = {"Authorization": f"Bearer {access_token}"}

  def is_exist_user(self):
    response = requests.get(f"https://velog.io/@{self.username}")
    return False if response.status_code == 404 else True

  def get_post_infos(self) -> pd.DataFrame:
    posts = self.get_posts()
    hits = asyncio.run(self.get_hits(posts))

    df_posts = pd.DataFrame.from_dict(posts)
    df_hits = pd.DataFrame.from_dict(hits)
    post_infos = pd.merge(left=df_posts, right=df_hits, how="inner", on="id")

    return post_infos

  def get_posts(self) -> list:
    posts = []
    cursor = None

    while True:
      if cursor is None:
        query = graphql_posts(self.username, LIMIT)
      else:
        query = graphql_posts(self.username, LIMIT, cursor)

      response = requests.post(url="https://v3.velog.io/graphql", json=query)
      response_data = json.loads(response.text)
      posts.extend(response_data["data"]["posts"])

      cursor = posts[-1]["id"]
      if len(response_data["data"]["posts"]) < LIMIT:
        break

    return posts

  async def get_hits(self, posts: list) -> list:
    async with aiohttp.ClientSession() as session:
      tasks = [self.get_view_by_post(session, post) for post in posts]
      hits = await asyncio.gather(*tasks)
    return hits

  async def get_view_by_post(self, session: aiohttp.ClientSession, post: dict) -> dict:
    query = graphql_get_status(post["id"])
    async with session.post(
        url="https://v2cdn.velog.io/graphql",
        json=query,
        headers=self.headers,
        ssl=False
    ) as response:
      response_data = await response.json()
      try:
        return {
          "id": post["id"],
          "total": response_data["data"]["getStats"]["total"],
          # NOTE: 임시 비활성화로 인해 주석 처리, https://github.com/velog-io/velog/issues/22
          # "latest_count": response_data["data"]["getStats"]["count_by_day"][0]["count"],
          # "latest_day": response_data["data"]["getStats"]["count_by_day"][0]["day"]
        }
      except TypeError:
        st.error("Access Token이 잘못된 형식이거나 만료 되었을 수 있습니다.")
        st.stop()
