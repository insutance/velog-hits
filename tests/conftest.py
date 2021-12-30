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
