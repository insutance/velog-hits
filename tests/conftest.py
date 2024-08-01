import os
from datetime import datetime
from pathlib import Path

import pytest


def pytest_addoption(parser):
  parser.addini("test_username", "My Velog Username For Test")
  parser.addini("test_access_token", "My Access Token For Test")


@pytest.fixture(scope="session")
def username(request):
  return request.config.getini("test_username")


@pytest.fixture(scope="session")
def access_token(request):
  return request.config.getini("test_access_token")


# Deprecated
@pytest.fixture(scope="session")
def velog_hits_path():
  return Path.cwd()


# Deprecated
@pytest.fixture(scope="session")
def html_file_path(velog_hits_path):
  html_file_name = f"{datetime.today().strftime('%Y%m%d')}.html"
  return os.path.join(velog_hits_path, "htmlhits", html_file_name)


# Deprecated
@pytest.fixture(scope="session")
def html_file_path(velog_hits_path):
  json_file_name = f"{datetime.today().strftime('%Y%m%d')}.html"
  return os.path.join(velog_hits_path, "htmlhits", json_file_name)


# Deprecated
@pytest.fixture(scope="session")
def css_file_path(velog_hits_path):
  css_file_name = "table.css"
  return os.path.join(velog_hits_path, "htmlhits", css_file_name)


# Deprecated
@pytest.fixture(scope="session")
def js_file_path(velog_hits_path):
  js_file_name = "sorttable.js"
  return os.path.join(velog_hits_path, "htmlhits", js_file_name)
