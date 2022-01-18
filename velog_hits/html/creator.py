import os
import shutil

from pathlib import Path


class CssJsCreator:
  def __init__(self) -> None:
    self.velog_hits_path = Path.cwd()

  def copy_css_file(self) -> bool:
    file_name = "table.css"
    css_file_path = self.get_copy_file_path(file_name)
    destination_path = self.get_destination_file_path(file_name)

    if self.file_copy(css_file_path, destination_path):
      return True
    return False

  def copy_js_file(self) -> bool:
    file_name = "sorttable.js"
    js_file_path = self.get_copy_file_path(file_name)
    destination_path = self.get_destination_file_path(file_name)

    if self.file_copy(js_file_path, destination_path):
      return True
    return False

  def get_copy_file_path(self, file_name) -> str:
    return os.path.join(self.velog_hits_path, "velog_hits", "html", file_name)

  def get_destination_file_path(self, file_name) -> str:
    return os.path.join(self.velog_hits_path, "htmlhits", file_name)

  def file_copy(self, copy_file_path, destination_path) -> bool:
    try:
      if not os.path.exists(destination_path):
          shutil.copy2(copy_file_path, destination_path)
      return True

    except:
      return False
