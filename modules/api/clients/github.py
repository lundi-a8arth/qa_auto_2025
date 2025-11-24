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

        return r.status_code, r.json()

    def search_repo(self, name):
        r = requests.get(
            "https://api.github.com/search/repositories",
            params={"q": name},
            headers=self.headers,
        )

        return r.status_code, r.json()

    def get_commit_from_repo(self, owner, repo, commit_ref):
        r = requests.get(
            f"https://api.github.com/repos/{owner}/{repo}/commits/{commit_ref}",
            headers=self.headers,
        )

        return r.status_code, r.json()

    def get_rate_limit(self):
        r = requests.get("https://api.github.com/rate_limit", headers=self.headers)

        return r.status_code, r.json()
