import os
import pytest

from velog_hits.html.creator import CssJsCreator


def test_css_copy(css_file_path):
  CssJsCreator().copy_css_file()
  assert os.path.isfile(css_file_path)


def test_js_copy(js_file_path):
  CssJsCreator().copy_js_file()
  assert os.path.isfile(js_file_path)
