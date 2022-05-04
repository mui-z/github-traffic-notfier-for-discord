import settings
from github import Github
import json
import requests

GITHUB_TOKEN = settings.GITHUB_TOKEN
DISCORD_WEBHOOK_URL = settings.DISCORD_WEBHOOK_URL
USER_NAME = settings.USER_NAME

if __name__ == '__main__':
    github = Github(GITHUB_TOKEN)
    repos = github.get_user(USER_NAME).get_repos()
    contents = []

    total_views = 0
    total_clones = 0

    for repo in repos:
        views = repo.get_views_traffic()["count"]
        clones = repo.get_clones_traffic()["count"]
        contents.append(f"repo: {repo.name}\nviews: {str(views)}\nclones: {str(clones)}\n\n")

        total_clones += clones
        total_views += views

    res = requests.post(DISCORD_WEBHOOK_URL,
        headers=({'Content-Type': "application/json"}),
        data=json.dumps({
            'content': "".join(str(content) for content in contents) + f"\ntotal views: {total_views}\ntotal clones: {total_clones}"
        })
    )