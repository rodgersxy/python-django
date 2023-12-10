import requests

url = "https://api.github.com/users/rodgersxy/repos"

response = requests.get(url)

if response.status_code == 200:
    repos = response.json()
    for repo in repos:
        print(repo["name"])
else:
    print("Failed to retrieve repositories")