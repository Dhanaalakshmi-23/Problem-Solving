#2. Group movies by genre and find the highest rated movie in each genre.
# sample input :
# [
#  ("Leo", "Action", 8.2),
#  ("Vikram", "Action", 8.8),
#  ("96", "Romance", 8.5),
#  ("Love Today", "Romance", 7.9),
#  ("Jailer", "Thriller", 8.1)
# ]

# output :
# {
#  'Action': ['Leo', 'Vikram'],
#  'Romance': ['96', 'Love Today'],
#  'Thriller': ['Jailer']
# }

# highest rated movie in Action : Vikram
# highest rated movie in Romance : 96
# highest rated movie in Thriller : Jailer

def movieDetails(data):
    groups = {}
    highest = {}
    
    for movie, genre, rating in data:
        
        groups.setdefault(genre, []).append(movie)
        
        if genre not in highest or rating > highest[genre][1]:
            highest[genre] = (movie, rating)
    
    print(groups)
    
    for genre in highest:
        print("Highest rated movie in", genre, ":", highest[genre][0])


movies = [
    ("Leo", "Action", 8.2),
    ("Vikram", "Action", 8.8),
    ("96", "Romance", 8.5),
    ("Love Today", "Romance", 7.9),
    ("Jailer", "Thriller", 8.1)
]

movieDetails(movies)