def compareNumbers(a, b):
    if a == b:
        return 0
    if a < b:
        return -1
    if a > b:
        return 1

def compare(a, b):
    if a > b:
        return 1
    if a < b:
        return -1
    return 0


def sortByYear(movies):
    return sorted(movies, key=lambda movie: movie['year'], reverse=True)

def stripLeadingArticle(title):
    articles = ['A', 'An', 'The']
    words = title.split(' ')
    if words[0] in articles:
        return ' '.join(words[1:])
    return title

def sortByTitle(movies):
    return sorted(movies, key=lambda movie: stripLeadingArticle(movie['title']))


movies = [
    { 'title': 'The Dark Knight', 'year': 2008, 'genres': ['Action', 'Drama'] },
    { 'title': 'Pulp Fiction', 'year': 1994, 'genres': ['Crime', 'Drama'] },
    { 'title': 'The Shawshank Redemption', 'year': 1994, 'genres': ['Drama'] },
    { 'title': 'Inception', 'year': 2010, 'genres': ['Action', 'Adventure', 'Sci-Fi'] }
]

sortedByYear = sortByYear(movies)
print("Sorted by Year:")
for movie in sortedByYear:
    print(f"{movie['title']} ({movie['year']})")


sortedByTitle = sortByTitle(movies)
print("\nSorted by Title:")
for movie in sortedByTitle:
    print(movie['title'])

