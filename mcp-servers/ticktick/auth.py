import os
import httpx

TICKTICK_AUTH_URL = "https://ticktick.com/oauth/authorize"
TICKTICK_TOKEN_URL = "https://ticktick.com/oauth/token"

CLIENT_ID = os.environ["TICKTICK_CLIENT_ID"]
CLIENT_SECRET = os.environ["TICKTICK_CLIENT_SECRET"]
ACCESS_TOKEN = os.environ.get("TICKTICK_ACCESS_TOKEN")


def get_auth_headers() -> dict:
    return {"Authorization": f"Bearer {ACCESS_TOKEN}"}
