from velog_hits.command import CommandParser
from velog_hits.convertor import DF2HTMLConverter
from velog_hits.crawler import HitsCrawler


def main():
  args = CommandParser().get_args()
  username = args.username[0]
  access_token = args.accesstoken[0]

  print(f"'{username}'님의 조회수 데이터를 가져오고 있으니 잠시만 기다려주세요:)")
  hits_crawler = HitsCrawler(username, access_token)
  post_infos = hits_crawler.get_post_infos()
  print(f"'{username}'님의 조회수 데이터를 모두 가져왔습니다!!")

  print("HTML로 변환을 시작합니다...")
  convertor = DF2HTMLConverter()
  df_result = convertor.get_result_dataframe(post_infos, f"https://velog.io/@{username}/")
  convertor.convert_df_to_html(df_result)
