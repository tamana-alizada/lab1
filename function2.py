# Dictionary of movies

movies = [
    {
        "name": "Usual Suspects",
        "imdb": 7.0,
        "category": "Thriller"
    },
    {
        "name": "Hitman",
        "imdb": 6.3,
        "category": "Action"
    },
    {
        "name": "Dark Knight",
        "imdb": 9.0,
        "category": "Adventure"
    },
    {
        "name": "The Help",
        "imdb": 8.0,
        "category": "Drama"
    },
    {
        "name": "The Choice",
        "imdb": 6.2,
        "category": "Romance"
    },
    {
        "name": "Colonia",
        "imdb": 7.4,
        "category": "Romance"
    },
    {
        "name": "Love",
        "imdb": 6.0,
        "category": "Romance"
    },
    {
        "name": "Bride Wars",
        "imdb": 5.4,
        "category": "Romance"
    },
    {
        "name": "AlphaJet",
        "imdb": 3.2,
        "category": "War"
    },
    {
        "name": "Ringing Crime",
        "imdb": 4.0,
        "category": "Crime"
    },
    {
        "name": "Joking muck",
        "imdb": 7.2,
        "category": "Comedy"
    },
    {
        "name": "What is the name",
        "imdb": 9.2,
        "category": "Suspense"
    },
    {
        "name": "Detective",
        "imdb": 7.0,
        "category": "Suspense"
    },
    {
        "name": "Exam",
        "imdb": 4.2,
        "category": "Thriller"
    },
    {
        "name": "We Two",
        "imdb": 7.2,
        "category": "Romance"
    }
]

# 1


def isIMDBabove(movie):
    if movie["imdb"] > 5.5:
        return True
    else:
        return False


for movie in movies:
    print(isIMDBabove(movie))

# 2
movieWithHighIMDB = []
for movie in movies:
    if (isIMDBabove(movie)):
        movieWithHighIMDB.append(movie)
print(movieWithHighIMDB)

print("")


# 3


def categoryFunc(categoryName):
    for movie in movies:
        if categoryName in movie.values():
            print(movie)


categoryFunc('Romance')

# 4


def averageFunc(movielist):
    sum = 0
    for movie in movielist:
        sum += movie['imdb']
    return sum / len(movielist)


print(averageFunc(movies))

# 5


def catergoryAverage(categoryName):
    sum = 0
    i = 0
    for movie in movies:
        if categoryName in movie.values():
            sum += movie['imdb']
            i += 1
    return sum / i


print(catergoryAverage('Romance'))
