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

