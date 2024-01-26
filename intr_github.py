import requests

url = 'https://api.github.com/users/{username}/repos'
keys = ["id", "name", "html_url", "description", "language"]
headers = {"Accept": "application/vnd.github.v3+json"}

#print(f"Status code: {res.status_code}")

dictfilt = lambda x, y: dict([ (i,x[i]) for i in x if i in set(y) ])

def call_github_api(github_username):
    res = requests.get(url.format(username = github_username), headers=headers)
    reps = []

    for idx, rep in enumerate(res.json()):
        if idx > 4:
            break

        reps.append(dictfilt(rep, keys))


    return reps


