import json
import pandas as pd
import requests
import sys

from velog_hits.graphql import graphql_posts, graphql_get_status


class HitsCrawler:
  def __init__(
      self,
      username,
      access_token=None
  ) -> None:
    self.username = username
    self.url = f"https://velog.io/@{username}/"
    self.access_token = access_token

  def check_username(func):
    def decorate(*args, **kwargs):
      self = args[0]
      response = requests.get(f"https://velog.io/@{self.username}")
      if response.status_code == 404:
        print("해당 유저는 존재하지 않습니다.")
        sys.exit()
      return func(*args, **kwargs)
    return decorate

  def check_access_token(func):
    def decorate(*args, **kwargs):
      self = args[0]
      if self.access_token is None:
        print("Access Token이 존재하지 않습니다.")
        sys.exit()
      return func(*args, **kwargs)
    return decorate

  @check_username
  @check_access_token
  def get_post_infos(self) -> pd.DataFrame:
    posts = self.get_posts()
    hits = self.get_hits()

    df_posts = pd.DataFrame.from_dict(posts)
    df_hits = pd.DataFrame.from_dict(hits)
    post_infos = pd.merge(left=df_posts, right=df_hits, how="inner", on="id")

    return post_infos

  @check_username
  def get_posts(self) -> list:
    posts = []
    cursor = None

    while True:
      if cursor is None:
        query = graphql_posts(self.username)
      else:
        query = graphql_posts(self.username, cursor)

      response = requests.post(url="https://v2.velog.io/graphql", json=query)
      response_data = json.loads(response.text)
      posts.extend(response_data["data"]["posts"])

      cursor = posts[-1]["id"]

      if len(response_data["data"]["posts"]) < 20:
        break

    return posts

  @check_username
  @check_access_token
  def get_hits(self) -> list:
    posts = self.get_posts()
    headers = {"Authorization": f"Bearer {self.access_token}"}

    hits = []
    for post in posts:
      query = graphql_get_status(post["id"])
      response = requests.post(
          url="https://v2.velog.io/graphql",
          json=query,
          headers=headers
      )
      response_data = json.loads(response.text)
      try:
        hits.append(
            {
                "id": post["id"],
                "total": response_data["data"]["getStats"]["total"],
                "latest_count": response_data["data"]["getStats"]["count_by_day"][0]["count"],
                "latest_day": response_data["data"]["getStats"]["count_by_day"][0]["day"]
            }
        )
      except TypeError:
        print("Access Token이 잘못된 형식이거나 만료 되었을 수 있습니다.")
        sys.exit()

    return hits
