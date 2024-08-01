# Deprecated
import pytest

from velog_hits.command import CommandParser


@pytest.fixture()
def command():
  return CommandParser()


def test_username_accesstoken(username, access_token, command):
  args = command.parser.parse_args(["-u", username, "-at", access_token])
  assert isinstance(args.username, list) and len(args.username) == 1
  assert isinstance(args.accesstoken, list) and len(args.accesstoken) == 1
