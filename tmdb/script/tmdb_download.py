import requests
import re
import os
import json

# Get the directory of the current script
script_dir = os.path.dirname(__file__)

# Set the working directory to the script's directory
os.chdir(script_dir)


api_key = 'api_key=aa6f28690f0d7b328c28c663a992bd70'
file_path = 'top_movie.txt'
data_directory = '../tmdb_data'
tmdb_adress = 'https://api.themoviedb.org'
def search_movie(query):

    pattern = r'^(.*?);(\d{4})$'
    match = re.search(pattern, query)
    year = None
    if match:
        name = match.group(1).strip()  # Extract everything before the year and strip whitespace
        year = match.group(2)  # Extract the year
    else:
        name = query

    seachurl = tmdb_adress +'/3/search/movie?query=' + name +'&' + api_key
    if year is not None :
        seachurl += '&primary_release_year=' + year

    response = requests.get(seachurl)
    jj = response.json()
    results = jj['results']
    if len(results) == 0 :
        return None
    first_result = results[0]
    return first_result


def get_file_id(movie_info):
    id_movie = movie_info['id']
    title = movie_info['title']
    release_date = movie_info['release_date']
    date_parts = release_date.split('-')
    year = date_parts[0]
    return title +'#' + year +'#' + str(id_movie)
def save_data(query):
    movie_info = search_movie(query)
    if movie_info is None :
        print ('MOVIE NOT FOUND : ' + query)
        return
    
    id_movie = movie_info['id']
    movie_details = get_movie_details(id_movie)
    movie_cast = get_cast_details(id_movie)
    file_id = get_file_id(movie_info)
    file_dir = data_directory + '/' + file_id.replace(":","")

    os.makedirs(file_dir, exist_ok=True)

    with open(file_dir  + '/data', 'w') as file:
        file.write(json.dumps(movie_info, indent=4))
    with open(file_dir + '/detail', 'w') as file:
        file.write(json.dumps(movie_details, indent=4))
    with open(file_dir + '/cast', 'w') as file:
        file.write(json.dumps(movie_cast, indent=4))

def get_movie_details(id_movie):
    url_detail_fr = tmdb_adress + '/3/movie/' + str(id_movie) + '?' + api_key + '&language=fr-FR%22'
    return requests.get(url_detail_fr).json()

def get_cast_details(id_movie):
    url_credits_fr = tmdb_adress + '/3/movie/' + str(id_movie) + '/credits' + '?' + api_key + '&language=fr-FR%22'
    return requests.get(url_credits_fr).json()


if not os.path.exists(data_directory):
    os.makedirs(data_directory)

with open(file_path, 'r') as file:
    for line in file:
        line = line.strip()
        line = line.split('//')[0]
        print(line)
        save_data(line)
