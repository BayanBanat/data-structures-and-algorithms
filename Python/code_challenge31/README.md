# Code Challenge: Class 31
# hashmap-repeated-word

## Whiteboard Process
![img1](./repeated.jpg)

## Approach & Efficiency
time complexity of the function is O(N + M), where N is the length of the input string and M is the number of words in the list.
space complexity of the function is O(N + M) ,where N is the length of the input string and M is the number of words in the list.


## Solution

python Python/code_challenge31/hashmap_repeated_word/hashmap_repeated_word.py

```python
if __name__ == "__main__":
    input_string1 = "Once upon a time, there was a brave princess who..."
    print(repeated_word(input_string1))  
    input_string2 = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    print(repeated_word(input_string2)) 
    input_string3 = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    print(repeated_word(input_string3))

```