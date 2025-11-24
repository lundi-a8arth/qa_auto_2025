import os
import requests
from dotenv import load_dotenv


class GitHub:

    def __init__(self):
        load_dotenv()

        token = os.getenv("GITHUB_TOKEN")

        self.headers = {}
        if token:
            self.headers = {"Authorization": f"Bearer {token}"}

    def get_user_by_username(self, username):
        r = requests.get(
            f"https://api.github.com/users/{username}", headers=self.headers
        )
        body = r.json()

        return body

    def search_repo(self, name):
        r = requests.get(
            "https://api.github.com/search/repositories",
            params={"q": name},
            headers=self.headers,
        )
        body = r.json()

        return body

    def get_rate_limit(self):
        r = requests.get("https://api.github.com/rate_limit", headers=self.headers)
        body = r.json()

        return body
