import os
import json
from bs4 import BeautifulSoup
# Get the directory of the current script
script_dir = os.path.dirname(__file__)

# Set the working directory to the script's directory
os.chdir(script_dir)

directory_path = "../tmdb_data"

def get_movie_infos(movie_dir):
    data_file_path = directory_path + '/' + movie_dir + '/' + 'data'
    cast_file_path = directory_path + '/' + movie_dir + '/' + 'cast'
    detail_file_path = directory_path + '/' + movie_dir + '/' + 'detail'
    with open(data_file_path, 'r') as f:
      data = json.load(f)
    movie_info = data
    with open(detail_file_path, 'r') as f:
      data = json.load(f)
    movie_detail = data
    with open(cast_file_path, 'r') as f:
      data = json.load(f)
    movie_credit = data
    return movie_info, movie_detail, movie_credit

def get_movie_html(movie_dir, movie_table):

    movie_info, movie_detail, movie_credit = get_movie_infos(movie_dir)

    crew = movie_credit['crew']
    director = "-"
    director_img_path = "-"
    for guy in crew :
        if guy['job'] == "Director" :
            director = guy['name']
            director_img_path = guy['profile_path']

            break

    original_title = movie_info['original_title']
    overview = movie_detail['overview']
    tagline = movie_detail['tagline']

    title = movie_info['title']
    poster_path = movie_info['poster_path']
    backdrop_path = movie_detail['backdrop_path']
    release_date = movie_info['release_date']
    if poster_path is None :
        poster_path = ''
    vote_average = movie_info['vote_average']

    date_parts = release_date.split('-')
    year = date_parts[0]

    global_height = 300
    h_director = 50

    poster_img = soup.new_tag("img") 
    h = global_height
    w = h / 1.5

    poster_img['width'] = str(w)
    poster_img['height'] = str(h)
    poster_img['src'] = 'http://image.tmdb.org/t/p/w400'+ poster_path

    title_tag = soup.new_tag("div") 
    title_tag2 = soup.new_tag("p") 
    title_tag['id'] = 'title'
    title_tag['class'] = 'title_style'
    title_tag2.string = title
    title_tag2['class'] = 'title_tag2'
    title_tag.append(title_tag2) 


    year_title = soup.new_tag("div") 
    year_title['class'] = 'movie_element'
    year_title.string = 'year'


    year_tag = soup.new_tag("div") 
    year_tag['id'] = 'year'
    year_tag['class'] = 'movie_element year'
    year_tag.string = year


    note_title = soup.new_tag("div") 
    note_title['class'] = 'movie_element'
    note_title.string = 'tmdb'

    note_tag = soup.new_tag("div") 
    note_tag['id'] = 'note'
    note_tag['class'] = 'movie_element'
    note_tag.string = "{:.1f}".format(vote_average)

    score_title = soup.new_tag("div") 
    score_title['class'] = 'movie_element'
    

    score_title.string = 'score'
    
    score_tag = soup.new_tag("div") 
    score_tag['id'] = 'score'
    score_tag['class'] = 'movie_element'
    score_tag.string = '-'

    director_tag = soup.new_tag("div") 
    director_tag['id'] = 'director'
    director_tag['class'] = 'director_element'
    director_tag.string = director
    director_tag['style'] = 'font-size: 20px;'

    director_img = soup.new_tag("img") 
    w_director = h_director / 1.5
    director_img['width'] = str(w_director)
    director_img['height'] = str(h_director)
    director_img['src'] = 'http://image.tmdb.org/t/p/w400'+ director_img_path


    backdrop_img = soup.new_tag("img") 

    h = global_height - 80 -50
    w = h / 0.5625
    backdrop_img['width'] = str(w)
    backdrop_img['height'] = str(h)
    backdrop_img['src'] = 'http://image.tmdb.org/t/p/w400'+ backdrop_path






    director_container = soup.new_tag("div") 
    director_container['class'] = 'Hcontainer'
    director_container['style'] = '  background-color: rgba(0, 0, 0, 0.5);'
  
    director_container.append(director_tag) 
    director_container.append(director_img) 


    info_div3 = soup.new_tag("div") 
    info_div3['class'] = 'Vcontainer'

    column_info = soup.new_tag("div") 
    column_info['class'] = 'Vcontainer column_info'



    year_info = soup.new_tag("div") 
    year_info['class'] = 'Vcontainer'
    year_info.append(year_title) 
    year_info.append(year_tag) 
    column_info.append(year_info) 
    year_info['style'] = '  background-color: rgba(0, 0, 0, 0.5);'

    note_info = soup.new_tag("div") 
    note_info['class'] = 'Vcontainer'
    note_info.append(note_title) 
    note_info.append(note_tag) 
    column_info.append(note_info) 
    note_info['style'] = '  background-color: rgba(0, 0, 0, 0.5);'

    score_info = soup.new_tag("div") 
    score_info['class'] = 'Vcontainer'
    score_info.append(score_title) 
    score_info.append(score_tag) 
    column_info.append(score_info) 
    score_info['style'] = '  background-color: rgba(0, 0, 0, 0.5);'

    info_div = soup.new_tag("div") 
    info_div['class'] = 'Hcontainer'
    info_div.append(column_info) 

    info_div3.append(director_container) 
    info_div3.append(backdrop_img) 
    info_div.append(info_div3) 

    movie_v_container = soup.new_tag("div") 
    movie_v_container['class'] = 'Vcontainer expand'

    movie_v_container.append(title_tag) 
    movie_v_container.append(info_div) 

    movie_div = soup.new_tag("div") 
    movie_div['class'] = 'movie_div Hcontainer'
    movie_div.append(poster_img) 
    movie_div.append(movie_v_container)


    movie_div['year'] = year
    movie_div['director'] = director
    movie_div['vote_average'] = "{:.1f}".format(vote_average)

    movie_table.append(movie_div) 










    # movie_table.append(director_container) 

    return (title+";"+year)

csv_data = ''

directory_list = os.listdir(directory_path)

with open('template.html', 'r') as f:
      data = f.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(data, 'html.parser')      

# Find the element with the ID "my-div"
movie_table = soup.find(attrs={'id':'movie_table'})


for movie_dir in directory_list:
    print(movie_dir)

    vsc_info = get_movie_html(movie_dir, movie_table)
    csv_data += vsc_info + '\n'


with open("../result/output.html", "w", encoding = 'utf-8') as file: 
    
    # prettify the soup object and convert it into a string   
    file.write(str(soup.prettify()))

with open("../result/info.csv", "w") as file:
    file.write(csv_data)