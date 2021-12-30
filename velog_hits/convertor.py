import os
import pandas as pd

from pathlib import Path


class DF2HTMLConverter:
  def convert_df_to_html(self, df):
    try:
      root_path = Path((Path(__file__).parent).parent.resolve())
      html_path = os.path.join(root_path, "htmlhits")
      if not os.path.isdir(html_path):
        os.mkdir(html_path)

      with open(os.path.join(html_path, "index.html"), "w") as html_file:
        html = df.to_html(index=False, escape=False)
        html_file.write(html)

      with open(os.path.join(html_path, "hits_data.json"), "w") as json_file:
        json_data = df.to_json(orient="records", date_format="iso")
        json_file.write(json_data)

      print("Velog Hits Crawling Success!!")
      return True

    except Exception as e:
      raise Exception(e)

  def get_result_dataframe(self, df, url):
    df = self._create_url(df, url)
    df = self._create_html_link(df)
    df = self._modify_date_format(df)

    df = df[["post", "tags", "comments_count", "likes", "total", "latest_count", "latest_day"]]
    return df

  def _create_url(self, df, url):
    df["url"] = url + df["url_slug"]
    return df

  def _create_html_link(self, df):
    df["post"] = "<a href='" + df["url"] + "'>" + df["title"] + "</a>"
    return df

  def _modify_date_format(self, df):
    df["latest_day"] = pd.to_datetime(df["latest_day"], format="%Y/%m/%d")
    df["latest_day"] = df["latest_day"].dt.date
    return df
