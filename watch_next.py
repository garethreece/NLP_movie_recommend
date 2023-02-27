# A program to determine a recommendation for what the user watches next based on the description of films

# IMPORT
# You need to have spaCy installed for this import to work.
import spacy
nlp = spacy.load('en_core_web_md')

# GLOBAL VARIABLES
movies = []

# DEFINE FUNCTIONS
# This function will read the file data and sort it into the relevant format for the movies list variable
def read_file():
    # Try to open the file movies.txt. If it is missing it will give a warning and quit
    try:
        file = open("movies.txt", "r", encoding = "utf-8-sig")
    except FileNotFoundError:
        print("The file is missing, please create \"movies.txt\" with relvant data for this program to work!")
        quit()
    # Once the file is open it will loop through the file one line at a time and format it so that it can be appended into the movies list
    for film in file:
        film = film.replace("\n", "").split(" :")
        movies.append(film)
    file.close()

# The function returns the description of the hulk film
# It could be programmed to get the data of the the last film (or several films) descriptions that were watched... if required
def hulk():
    return "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

# The main function to compare the descriptions in the file (movie list), with the description of the last film watched (hulk) 
def similarity():
    # Use the score variable so that it can compare with the biggest percentage in similarity as it works through the movie list
    score = 0
    # Loops through all the movies in the list tokenises with nlp the description and compares themn to the recent description for similarities
    for movie in movies:
        similarity = nlp(movie[1]).similarity(recent_movie)
        # If the score is lower than the similarity then it will save the name and description and the top score in the variables
        # If a similarity beats the current highest score, then the variables will be replaced with the new current film data
        if score <= similarity:
            movie_name, movie_des, score = movie[0], movie[1], similarity
    # Once the loops have finished it will return the film with the highest similarity and its associated data
    return movie_name, movie_des, score

# Main Program
# calls on the read file function
read_file()
# calls on the description of the last film watched (hulk)
watched = hulk()
# tokenises the string of the most recent film watched ready for the similarity comparison (hulk)
recent_movie = nlp(watched)
# goes to the similarity function for movie description comparisons and returns most relevant film data
recommended_movie, recommended_description, percentage= similarity()

# Prints the recommendation (film with the highest similarity) for the user
print(f"""
Based on your recent viewing history...
The recommended movie is: {recommended_movie}
Movie description: {recommended_description}
With a percentage recommended score of {percentage * 100:.1f}%
ENJOY!
""")