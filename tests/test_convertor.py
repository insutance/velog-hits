import os
import pytest

from pathlib import Path
from datetime import datetime
from velog_hits.convertor import DF2HTMLConverter
from velog_hits.crawler import HitsCrawler


class TestUpdateColumn:
  @pytest.fixture(scope="class")
  def post_infos(self, username, access_token):
    hits_crawler = HitsCrawler(username, access_token)
    return hits_crawler.get_post_infos()

  @pytest.fixture(scope="class")
  def html_convertor(self):
    return DF2HTMLConverter()

  def test_modify_date_format(self, post_infos, html_convertor):
    df = html_convertor._modify_date_format(post_infos)
    # print(df["latest_day"])

  def test_create_url(self, username, post_infos, html_convertor):
    df = html_convertor._create_url(post_infos, f"https://velog.io/@{username}/")
    assert "url" in df.columns

  def test_create_html_link(self, username, post_infos, html_convertor):
    post_infos = html_convertor._create_url(post_infos, f"https://velog.io/@{username}/")
    df = html_convertor._create_html_link(post_infos)
    assert "post" in df.columns

  def test_convert_df_to_html(self, post_infos, html_convertor):
    assert html_convertor.convert_df_to_html(post_infos)

    velog_hits_path = Path.cwd()
    index_html_path = os.path.join(velog_hits_path, "htmlhits", "index.html")
    assert os.path.isfile(index_html_path)


def test_df2html(username, access_token):
  hits_crawler = HitsCrawler(username, access_token)
  post_infos = hits_crawler.get_post_infos()

  convertor = DF2HTMLConverter()
  df_result = convertor.get_result_dataframe(post_infos, f"https://velog.io/@{username}/")
  assert convertor.convert_df_to_html(df_result)

  velog_hits_path = Path.cwd()
  file_name = datetime.today().strftime("%Y%m%d")
  result_directory_path = os.path.join(velog_hits_path, "htmlhits")
  html_file_path = os.path.join(result_directory_path, f"{file_name}.html")
  assert os.path.isfile(html_file_path)
