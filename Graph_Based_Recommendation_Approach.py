# import necessary libraries
import pandas as pd
import csv
import string
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stopwords = stopwords.words('english')
import random

# random walk algorithm and helper function

def random_walk(user_input,Recommendations,query_len):
    
    query = user_input
    total_steps = 0
    MSteps = 10000/query_len
    RV = Recommendations

    while total_steps <= MSteps:
    
        currMovie = query
        currSteps = random.randint(1,6)
      
        for i in range(0,currSteps):
        
            #1. select the genre to choose a movie from
            currGenres = movies[currMovie]
            currGenre = subrange(query,currGenres)
            #currGenre = currGenres[random.randint(0,len(currGenres)-1)]
            #2.Goes into the genre hashmap and corresponding key to get the list of movies
            currMovies = genres[currGenre]
            #3. select the movie at random and set as current movie 
            currMovie= currMovies[random.randint(0,len(currMovies)-1)]
        
        
        distribute_score(RV,currMovie,query)    
        total_steps = total_steps + currSteps
        
        
    return RV
    
    
def subrange(query_movie,current_genres):
    
    subrange = movies[query_movie]
    current_genre = current_genres[random.randint(0,len(current_genres)-1)]
    satisfy = False
    while(satisfy == False):
        current_genre = current_genres[random.randint(0,len(current_genres)-1)]
        if(current_genre in subrange):
            satisfy = True
    
    return current_genre


#https://www.kaggle.com/ruchi798/movies-on-netflix-prime-video-hulu-and-disney
# dataset taken from kaggle


with open('MoviesOnStreamingPlatforms_updated.csv','r') as file:

    reader = csv.DictReader(file)
    print(reader.fieldnames)
    
    movies=dict()
    genres= dict()
    
    for row in reader:
        
        movie_title=row['Title']
        g = row['Genres'].split(',')
        ds = row['Directors'].split(',')
        
      # creating/allocating movie to proper key-value pair in the genre HashMap
        for c in g:
            if(c in genres):
                genres[c].append(movie_title)
            else:
                genres[c] = [movie_title]

        #add the key-value pair to the movies 
        for category in g:
            if(movie_title in movies):
                movies[movie_title].append(category)
            else:
                movies[movie_title]=[category]
                
                
                

