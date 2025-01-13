import berserk
from dotenv import load_dotenv


lichess_token = load_dotenv(".env")["LICHESS_TOKEN"]
# Set up Lichess API client
session = berserk.TokenSession()
client = berserk.Client(session)

def get_player_profile(username):
    profile = client.users.get_public_data(username)
    return {
        "username": profile["username"],
        "title": profile.get("title", "None"),
        "rating": profile["perfs"]["blitz"]["rating"],
        "games_played": profile["perfs"]["blitz"]["games"]
    }

# Example: Fetch player profile
player_data = get_player_profile("MagnusCarlsen")
print(player_data)
