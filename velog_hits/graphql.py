def graphql_posts(username, limit, cursor=None) -> dict:
  """블로그 게시물 목록 가져오는 GraphQL"""
  return {
    "query": "query velogPosts($input: GetPostsInput!) {\n  posts(input: $input) {\n    id\n    title\n    short_description\n    thumbnail\n    user {\n      id\n      username\n      profile {\n        id\n        thumbnail\n        display_name\n      }\n    }\n    url_slug\n    released_at\n    updated_at\n    comments_count\n    tags\n    is_private\n    likes\n  }\n}\n    ",
    "variables": {
      "input": {
        "cursor": cursor if cursor is not None else None,
        "username": username,
        "limit": limit,
        "tag": ""
      }
    }
  }


def graphql_get_status(post_id):
  """통계 정보 가져오는 GraphQL"""
  return {
    "query": "query GetStats($post_id: ID!) {\n  getStats(post_id: $post_id) {\n    total\n    count_by_day {\n      count\n      day\n      __typename\n    }\n    __typename\n  }\n}\n",
    "variables": {"post_id": post_id}
  }
