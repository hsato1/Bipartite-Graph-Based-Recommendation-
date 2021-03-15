# Graph Based Recommendation System Approach with Random Walk Algorithm

## Name
Hiroki Sato (Under Supervision of Dr. Daniel S Myers at Rollins College)

## Description
I have been inspired by what artificial intelligence is capable of and how extensively it can be used to better our society. The recommendation engine is a great example of artificial intelligence as an application. 
The project is a recommendation system which provide a list of twenty movies as a personalized and diverse recommendation which user might like based on movies given from a user. The system model a recommendation system which uses a random walk algorithm, used by a Pixie, recommendation engine for Pinterest.   
### Constructing Bipartite Graph using Hashmap.  
This recommendation approach requires a bipartite graph. We modeled bipartite graph creating two Hashmaps of movies and genres. 
### Given movies, it will create a list of recommended movies.
``` 
Enter the number of movies you have watched: 1      # you could enter more than one name of a movie
Enter the name of the movie: Indiana Jones and the Last Crusade
```
### Python execute the random walk algorithm on bipartite graph & produce a pandas data frame of twenty movies that are most relevant to the query based on the algorithm.  
<img width="344" alt="Screen Shot 2021-03-14 at 8 05 07 PM" src="https://user-images.githubusercontent.com/71889206/111089101-b9491200-8500-11eb-81e8-edcd6730cf56.png">


## Concept / Libraries used for this projects
Python.   
Jupyternotebook.  
Pandas.  
sklearn to process string information and draw similarity using cosine similarity index.  
nltk: Natural Langualge Tool Kit to pre-process string before applying functions from sklearn. 
Random Walk Algorithm.  
Bipartite Graph.     
Jaccard Similarity Index.  
Cosine Similarity Index.  


## What is Pixie?? 
Pixie is a graph-based recommendation system used by Pinterest to produce personalized recommendations. The application is organized in terms of boards and pins and the recommendation engine takes an advatage of how the informations are organized.  
The traditional recommendation approach such as Collaborative Filtering and Content Based Filtering that heavily relies on user's histories which could lead to some drawbacks such as cold start problem when there's not enough data and the recommendation might lack of novelty since approach is deterministic to the user's behavior. In addition to that, Pinterest consists of billions of pins and millions of boards so the size of data the recommendation engine had to be able to handle without compromising the real time response requirement to the user's action. 
They overcame these shortcoming by constructing a bipartite graph of pins and boards, and executing a random walk algorithm. 

## Random Walk Algorithm 
<img width="883" alt="Screen Shot 2021-03-14 at 7 54 57 PM" src="https://user-images.githubusercontent.com/71889206/111088763-2e1b4c80-84ff-11eb-82f9-5250026131e3.png">

The random walk algorithm is executed on a bipartite graph, using the board or pins that user interacted as starting point of this algorithm, algorithm select the next vertex in a graph to visit. This sequence of choosing the next vertex to step onto, visit is repeated fix amount of time. We record the number of times each vertex was visited and vertex with more frequent visit during this algorithm is cosidered to be relevant.  
### Drawback of basic random walk algorithm
With my first try, algorithm did not work as I expected. As I recorded the number of visit in each vertex, the record resulted in hundreds of movies with only single visit, which indicated that the random walk went too extensive and too far away from the starting vertex, thus resulting in visiting verticies that were absolutely irrelevant. 

### Pinterest had solutions 
Pixie modified the basic random walk by: 
1. Biasing the random edge selection - Biased the random walk in a user-specific way by biasing the edge selection during the walk based on the user features so that the random walk would be executed more likely on a partial subset of an entire graph which is relevant to the user than irrelevant
2. Multiple query pins with weights - Ability to take in multiple queries and assign each query a weight based on the time since the user interacted and type of action, they took with the it
3. Multi-hit booster - boost the score of the pins that are visited by the sequence of steps that is from different pins
4. Early stopping - tops the walk when a certain number of pins exceeded the certain score.  

### My solution - Subrange and Jaccard / Cosine Similarity index for scoring. 
Since we implement the bipartite graph by using hash maps, we cannot demonstrate biasing the random edge selection like Pixie based on the user feature, but what we could do, is to create a subrange of the entire graph, meaning that allowing to pick only movies of the genres that are related to the query. As a result, it prevents random walk to visit irrelevant movies in the walk therefore visiting only movies that are relevant more frequently.
To identify the relevance of movies itself, I used genres of movies, Jaccard Similarity index and Cosine Similarity to calculate the similarity of the moveis that were visited. The movies with more genres in common would have higher score compared to the movies that does not have any genre in common.   


