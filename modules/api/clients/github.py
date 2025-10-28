import requests


class GitHub():

    def get_user(self, username):
        r = requests.get(f'https://api.github.com/users/{username}')
        body = r.json()

        return body

    def get_status_code(self, username):
        r = requests.get(f'https://api.github.com/users/{username}')
        return r.status_code