def graphql_posts(username, cursor=None):
  """블로그 게시물 목록 가져오는 GraphQL"""
  if cursor is None:
    cursor = "null"
  else:
    cursor = f"\"{cursor}\""

  return {
      "query": f"""
    query {{
      posts(cursor: {cursor}, username: "{username}") {{
        id
        title
        url_slug
        tags
        comments_count
        likes
        }}
      }}
  """
  }


def graphql_get_status(post_id):
  """통계 정보 가져오는 GraphQL"""
  return {
      "query": f"""
    query {{
    getStats(post_id: "{post_id}") {{
      total
      count_by_day {{
        count
        day
        __typename
      }}
      __typename
    }}
  }}
  """
  }
