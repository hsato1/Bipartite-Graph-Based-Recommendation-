# Graph Based Recommendation System Approach with Random Walk Algorithm

## Name
Hiroki Sato (Under Supervision of Dr. Daniel S Myers at Rollins College)

## Description
I have been inspired by what artificial intelligence is capable of and how extensively it can be used to better our society. The recommendation engine is a great example of artificial intelligence as an application. 
The project is a recommendation system which provide a list of twenty movies as a personalized and diverse recommendation which user might like based on movies given from a user. The system model a recommendation system which uses a random walk algorithm, used by a Pixie, recommendation engine for Pinterest.   
### Given movies, it will create a list of recommended movies.
``` 
Enter the number of movies you have watched: 1      # you could enter more than one name of a movie
Enter the name of the movie: Indiana Jones and the Last Crusade
```

## Concept / Libraries used for this projects
Random Walk Algorithm.  
Bipartite Graph.  
Python.  
sklearn to process string information and draw similarity using cosine similarity index.
nltk: Natural Langualge Tool Kit to pre-process string before applying functions from sklearn.  
Pandas.   
Jaccard Similarity Index.  
Cosine Similarity Index.  


## What is Pixie?? 
Pixie is a graph-based recommendation system used by Pinterest to produce personalized recommendations. The application is organized in terms of boards and pins and the recommendation engine takes an advatage of how the informations are organized.  
The traditional recommendation approach such as Collaborative Filtering and Content Based Filtering that heavily relies on user's histories which could lead to some drawbacks such as cold start problem when there's not enough data and the recommendation might lack of novelty since approach is deterministic to the user's behavior. In addition to that, Pinterest consists of billions of pins and millions of boards so the size of data the recommendation engine had to be able to handle without compromising the real time response requirement to the user's action. 
They overcame these shortcoming by constructing a bipartite graph of pins and boards, and executing a random walk algorithm. 

## Random Walk Algorithm 


