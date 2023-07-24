# Sorting: Comparisons 
 
 
**sortByYear** and **sortByTitle**, which operate on an array of Movie objects. The sortByYear function sorts the movies by the most recent year first, using the sorted function with a custom key. The sortByTitle function sorts the movies alphabetically by title, ignoring any leading "A"s, "An"s, or "The"s. It uses the sorted function with a lambda function as the key to remove the leading articles.

The **compareNumbers** function compares two numbers, a and b. It returns 0 if a is equal to b. If a is less than b, it returns -1. If a is greater than b, it returns 1. This function follows the convention of returning -1, 0, or 1 to represent the comparison results.

The **compare** function compares two values, a and b. It assumes that the values being compared support the greater than (>) and less than (<) operators. If a is greater than b, it returns 1. If a is less than b, it returns -1. If a is equal to b, it returns 0. This function can be used to compare various types of data, such as strings, numbers, or objects, as long as the necessary comparison operators are defined for the data type.