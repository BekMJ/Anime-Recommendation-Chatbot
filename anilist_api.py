from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

# Set up a GraphQL client to the AniList API
transport = RequestsHTTPTransport(url='https://graphql.anilist.co', use_json=True)
client = Client(transport=transport, fetch_schema_from_transport=True)

def fetch_anime_by_genre(genre):
    # Define your GraphQL query
    query = gql("""
    query ($genre: String) {
      Page(page: 1, perPage: 10) {
        media(genre: $genre, type: ANIME) {
          id
          title {
            romaji
          }
          description
        }
      }
    }
    """)
    variables = {"genre": genre}
    result = client.execute(query, variable_values=variables)
    return result['Page']['media']