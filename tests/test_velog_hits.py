# Deprecated
import pytest

from velog_hits.convertor import DF2HTMLConverter
from velog_hits.crawler import HitsCrawler
from velog_hits.html.creator import CssJsCreator


def test_velog_hits(username, access_token):
  print(f"'{username}'님의 조회수 데이터를 가져오고 있으니 잠시만 기다려주세요:)")
  hits_crawler = HitsCrawler(username, access_token)
  post_infos = hits_crawler.get_post_infos()
  print(f"'{username}'님의 조회수 데이터를 모두 가져왔습니다!!")

  print("HTML로 변환을 시작합니다...")
  convertor = DF2HTMLConverter()
  df_result = convertor.get_result_dataframe(post_infos, f"https://velog.io/@{username}/")

  css_js_creator = CssJsCreator()

  assert (
      convertor.convert_df_to_html(df_result)
      and convertor.convert_df_to_json(df_result)
      and css_js_creator.copy_css_file()
      and css_js_creator.copy_js_file()
  ), "Velog Fail"

  print("Velog Hits Success!!")
  print(f"Velog Hits Result: {convertor.html_file_path}")
