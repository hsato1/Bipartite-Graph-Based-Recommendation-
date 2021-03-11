# importing neccessary libraries
import nltk
nltk.download('stopwords')
import string
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
stopwords = stopwords.words('english')


def calculate_Jaccard_Similarity_Index(q,m1):
    intersect = 0
    
    for i in movies[m1]:
        if(i in movies[q]):
            intersect = intersect + 1
    
    JSI = intersect/(len(movies[q])+len(movies[m1]) - intersect)
    
    return JSI

def get_jaccard_sim(str1, str2): 
    
    str1 = clean_string(str1)
    str2 = clean_string(str2)
    
    a = set(str1.split()) 
    b = set(str2.split())
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))


def calculate_Cosine_Sim_Coefficient(query,movie):
    
    #when we are creating recommendation based on the genre
    movie_str = clean_string(movies[movie])
    query_str = clean_string(movies[query])
    
    data = list([query_str,movie_str])
    print(data)
    vectorizer = CountVectorizer().fit_transform(data)
    vectors = vectorizer.toarray()
    
    score = score = cosine_sim_vectors(vectors[0],vectors[1])
    
    return score


def clean_string(movie):
    
    data = ""
    for word in movie:
        data = data + word
        data = data + " "
    return data.lower()

def cosine_sim_vectors(v1,v2):
    v1 = v1.reshape(1,-1)
    v2 = v2.reshape(1,-1)
   
    
    return cosine_similarity(v1,v2)[0][0]
  
