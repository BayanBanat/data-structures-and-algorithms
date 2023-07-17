from Comparisons import compareNumbers, compare, stripLeadingArticle

def test_compareNumbers():
    assert compareNumbers(5, 10) == -1
    assert compareNumbers(10, 5) == 1
    assert compareNumbers(5, 5) == 0

def test_compare():
    assert compare('apple', 'banana') == -1
    assert compare('banana', 'apple') == 1
    assert compare('apple', 'apple') == 0

def test_stripLeadingArticle():
    assert stripLeadingArticle('The Dark Knight') == 'Dark Knight'
    assert stripLeadingArticle('An Inconvenient Truth') == 'Inconvenient Truth'
    assert stripLeadingArticle('A Beautiful Mind') == 'Beautiful Mind'
    assert stripLeadingArticle('Pulp Fiction') == 'Pulp Fiction'
