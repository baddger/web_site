import requests

url = "https://api.themoviedb.org/3/discover/movie?api_key=aa6f28690f0d7b328c28c663a992bd70&primary_release_year=1980"
#url = "https://api.themoviedb.org/3/movie/550?api_key=aa6f28690f0d7b328c28c663a992bd70"
headers = {
    "accept": "application/json",
    "Authorization": "Bearer aa6f28690f0d7b328c28c663a992bd70"
}

response = requests.get(url, headers=headers)

print(response.text)
