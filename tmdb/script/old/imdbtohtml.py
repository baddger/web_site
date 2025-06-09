import requests
import re


url = "https://api.themoviedb.org/3/discover/movie?api_key=aa6f28690f0d7b328c28c663a992bd70&primary_release_year=1980"


def get_film_info(query):


    # Define the regex pattern to capture everything before the year and the year itself
    pattern = r'^(.*?);(\d{4})$'

    # Search for the pattern in the input string
    match = re.search(pattern, query)
    year = None
    # Check if a match was found and extract the year and other part
    if match:
        name = match.group(1).strip()  # Extract everything before the year and strip whitespace
        year = match.group(2)  # Extract the year
    else:
        name = query

    
    seachurl = "https://api.themoviedb.org/3/search/movie?query=" + name +"&api_key=aa6f28690f0d7b328c28c663a992bd70"
    if year is not None :
        seachurl += "&primary_release_year=" + year
        print("         seachurl " + name + ' / ' + year)
    else :
        print("         seachurl " +name)

    headers = {
    "accept": "application/json",
    }
    response = requests.get(seachurl, headers=headers)
    jj = response.json()
    results = jj['results']
    if len(results) is 0 :
        return None
    first_result = results[0]
    return first_result





html_data = ''
html_data += """
<html>
    <script>
        // Ensure the DOM elements are loaded before attaching event listeners
        window.onload = function() {

            daz = function(tap) {
                // Get the container that holds the items
                const container = document.getElementById('movie_table');
                
                // Convert HTMLCollection (NodeList) to an array
                const itemsArray = Array.from(container.children);
                
                // Sort the array of list items
                itemsArray.sort((a, b) => a.childNodes[tap].textContent.localeCompare(b.childNodes[tap].textContent));
                
                // Clear the container
                container.innerHTML = '';
                
                // Append the sorted items back to the container
                itemsArray.forEach(item => container.appendChild(item));
            }
            document.getElementById('sortBtnName').addEventListener('click', function() {daz(1)});
            document.getElementById('sortBtnYear').addEventListener('click', function() {daz(2)});
            document.getElementById('sortBtnNote').addEventListener('click', function() {daz(3)});
            document.getElementById('sortBtnDirector').addEventListener('click', function() {daz(4)});

        };
    </script>
  <style>
      body {
      display: grid;                     /* Set the body to use Grid layout */
      flex-direction: row;
      justify-content: center;  /* Centers content horizontally */
      align-items: center;      /* Centers content vertically */
      margin: 0;
      background-color: black;
      color: white;
      gap: 20px; /* Adds 20px spacing between flex items */

    }
.title_style {
    max-width: 300px;          /* Set the maximum width for the text container */
    min-width: 300px;          /* Set the maximum width for the text container */
}
style_one {
   font-family: 'YourCustomFont', sans-serif;  /* Fallback to sans-serif */
   font-size: 45px;

}
@font-face {
    font-family: 'YourCustomFont';  /* Name you want to use for the font */
    src: url('fonts/YourFont.otf') format('opentype');  /* Path to your OTF file */
    src: url('fonts/thenightwatch.ttf') format('truetype');  /* Path to your OTF file */
    src: url('fonts/Monor_Regular.otf') format('opentype');  /* Path to your OTF file */

    
    font-weight: normal;   /* Set the weight (normal, bold, etc.) */
    font-style: normal;    /* Set the style (normal, italic, etc.) */
} 

    .container {
      background-color: #050505;  /* Green background for items */

      display: flex;
      align-items: center;
      gap: 20px; /* Adds 20px spacing between flex items */
      max-width: 1200px; /* Set your desired max-width here */
      justify-content: center;  /* Centers content horizontally */
      align-items: center;      /* Centers content vertically */
    }

    .itemop {
        text-align: center;        /* Center the text */
        color: white;                /* White text */
        padding: 2px;               /* Padding around text */
        border-radius: 5px;         /* Rounded corners */
        flex: 0 1 auto;              /* Default flex item settings */
    }

    .expand {
        flex-grow: 1;                /* Allow this item to grow */
    }
    .image {
      margin-left: 10px;
    }
      </style>
<body style="background-color: black; color: white;">
        <button id="sortBtnName">Sort by name</button>
        <button id="sortBtnYear">Sort by years</button>
        <button id="sortBtnNote">Sort by note</button>
        <button id="sortBtnDirector">Sort by director</button>

        <ul id="movie_table">
    <!-- Embedded JavaScript -->

"""



def get_movie_html(name):
    movie_info = get_film_info(name)
    if movie_info is None :
        return '<div class="container"> MERDE movie_info POUR '+ name +'</div>', "error " + name
    
    id_movie = movie_info['id']

    url_detail_fr = 'https://api.themoviedb.org/3/movie/' + str(id_movie) + '?api_key=aa6f28690f0d7b328c28c663a992bd70&language=fr-FR%22'
    movie_detail = requests.get(url_detail_fr).json()
    if movie_detail is None :
        return '<div class="container"> MERDE movie_detail POUR '+ name +'</div>', "error " + name
    
    url_credits_fr = 'https://api.themoviedb.org/3/movie/' + str(id_movie) + '/credits' + '?api_key=aa6f28690f0d7b328c28c663a992bd70&language=fr-FR%22'
    movie_credit = requests.get(url_credits_fr).json()
    if movie_credit is None :
        return '<div class="container"> MERDE movie_credit POUR '+ name +'</div>', "error " + name
    
    crew = movie_credit['crew']
    director = "-"
    director_img = "-"
    for guy in crew :
        if guy['job'] == "Director" :
            director = guy['name']
            director_img = guy['profile_path']

            break

    original_title = movie_info['original_title']

    title = movie_info['title']
    	
    overview = movie_detail['overview']
    tagline = movie_detail['tagline']
    poster_path = movie_info['poster_path']
    backdrop_path = movie_detail['backdrop_path']
    release_date = movie_info['release_date']
    if poster_path is None :
        poster_path = ''
    vote_average = movie_info['vote_average']

    # Split the string by a comma
    date_parts = release_date.split('-')
    year = date_parts[0]
    html_code = '<div class="container">'
    html_code += '<img class="itemop" "width="132" height="200" src="http://image.tmdb.org/t/p/w400'+ poster_path + '">'
    html_code += '<style_one style="min-width: 500px;" class="title_style expand itemop" >' + title + '</style_one>'
    html_code += '<style_one style="font-size: 25px;min-width: 100px;" class="itemop">' + year + '</style_one>'
 
    html_code += '<style_one style="font-size: 25px;min-width: 100px;" class="itemop">' + "{:.1f}".format(vote_average) + '</style_one>'
    html_code += '<style_one style="font-size: 25px;min-width: 250px;" class="itemop">' + director + '</style_one>'
    html_code += '<img class="itemop" width="132" height="200" src="http://image.tmdb.org/t/p/w400'+ director_img + '">'

    # html_code += '<img class="itemop" width="300" height="150" src="http://image.tmdb.org/t/p/w400'+ backdrop_path+ '">'
    html_code += '</div>'
    return html_code, (title+";"+year)

csv_data = ''

file_path = './art_list/top_movie.txt'

try:
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            line = line.split("//")[0]
            print(line)

            html_info, vsc_info = get_movie_html(line)
            html_data += html_info + '\n'
            csv_data += vsc_info + '\n'

except FileNotFoundError:
    print(f"The file {file_path} does not exist.")
except IOError:
    print("An error occurred while reading the file.")

html_data += '</ul>'
html_data += '</body>'
html_data += '</html>'
with open("test.html", "w") as file:
    file.write(html_data)
with open("info.csv", "w") as file:
    file.write(csv_data)