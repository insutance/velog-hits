import argparse


class CommandParser:
  def __init__(self) -> None:
    self.parser = argparse.ArgumentParser(description="Velog Hits")
    self.parser.add_argument("-u", "--username", nargs=1, required=True, help="Velog Username")
    self.parser.add_argument("-at", "--accesstoken", nargs=1, required=True, help="Your Velog Access Token")

  def get_args(self):
    return self.parser.parse_args()
