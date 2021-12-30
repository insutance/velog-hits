import pandas as pd
import pytest

from velog_hits.crawler import HitsCrawler


def test_get_posts(username):
  hits_crawler = HitsCrawler(username)
  posts = hits_crawler.get_posts()
  assert len(posts) > 0
  assert isinstance(posts, list)


def test_get_hits(username, access_token):
  hits_crawler = HitsCrawler(username, access_token)
  hits = hits_crawler.get_hits()
  assert len(hits) > 0
  assert isinstance(hits, list)


def test_check_username(username):
  hits_crawler = HitsCrawler(username + "error_username_test")
  with pytest.raises(Exception) as error:
    hits_crawler.get_posts()
  assert str(error.value) == "해당 유저는 존재하지 않습니다."


def test_check_access_token(username):
  hits_crawler = HitsCrawler(username)
  with pytest.raises(Exception) as error:
    hits_crawler.get_hits()
  assert str(error.value) == "Access Token이 존재하지 않습니다."


def test_get_post_infos(username, access_token):
  hits_crawler = HitsCrawler(username, access_token)
  post_infos = hits_crawler.get_post_infos()
  assert len(post_infos) > 0
  assert isinstance(post_infos, pd.DataFrame)
  # print(post_infos)
