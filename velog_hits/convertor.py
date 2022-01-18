import os
import pandas as pd

from pathlib import Path
from datetime import datetime

from velog_hits.html.base_html import html_string


class DF2HTMLConverter:
  def __init__(self) -> None:
    self.velog_hits_path = Path.cwd()
    self.result_directory_path = os.path.join(self.velog_hits_path, "htmlhits")
    self.file_name = datetime.today().strftime("%Y%m%d")
    self.html_file_path = os.path.join(self.result_directory_path, f"{self.file_name}.html")
    self.json_file_path = os.path.join(self.result_directory_path, f"{self.file_name}.json")

  def create_htmlhits_directroy(func):
    def decorate(*args, **kwargs):
      self = args[0]
      if not os.path.isdir(self.result_directory_path):
        os.mkdir(self.result_directory_path)
      return func(*args, **kwargs)
    return decorate

  @create_htmlhits_directroy
  def convert_df_to_html(self, df) -> bool:
    try:
      with open(self.html_file_path, "w") as html_file:
        html = df.to_html(index=False, escape=False, classes='sortable')
        sort_table_html = html_string.format(dataframe_to_html_table=html)
        html_file.write(sort_table_html)
      return True

    except Exception:
      return False

  @create_htmlhits_directroy
  def convert_df_to_json(self, df) -> bool:
    try:
      with open(self.json_file_path, "w") as json_file:
        json_data = df.to_json(orient="records", date_format="iso")
        json_file.write(json_data)
      return True

    except Exception:
      return False

  def get_result_dataframe(self, df, url) -> pd.DataFrame:
    df = self._create_url(df, url)
    df = self._create_html_link(df)
    df = self._modify_date_format(df)

    df = df[["post", "tags", "comments_count", "likes", "total", "latest_count", "latest_day"]]
    df.rename(
        columns={
            "post": "제목",
            "tags": "태그",
            "comments_count": "댓글",
            "likes": "좋아요",
            "total": "총 방문자",
            "latest_count": "최근 방문자",
            "latest_day": "최근방문날짜"
        },
        inplace=True
    )
    return df

  def _create_url(self, df, url) -> pd.DataFrame:
    df["url"] = url + df["url_slug"]
    return df

  def _create_html_link(self, df) -> pd.DataFrame:
    df["post"] = "<a href='" + df["url"] + "'>" + df["title"] + "</a>"
    return df

  def _modify_date_format(self, df) -> pd.DataFrame:
    df["latest_day"] = pd.to_datetime(df["latest_day"], format="%Y/%m/%d")
    df["latest_day"] = df["latest_day"].dt.date
    return df
