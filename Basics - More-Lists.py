# -*- coding: utf-8 -*-
"""M31.09 - python_list_drills_starter.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kgwOcYWlJcFlk2yuCt9hB1HvLiCuLIF6

## 1: `longest_word_length`

Create a function called `longest_word` that takes one argument, a list of words, and returns the length of the longest word in the list.

For example, `longest_word(['simple', 'is', 'better', 'than', 'complex'])` should return 7 because the longest word there is complex, at 7 characters.

Your function should *not* modify the input list.
"""

# your code here
words_list = ['simple', 'is', 'better', 'than', 'complex']

def longest_word(words_list):
  words_list.sort(key=len, reverse= True)
  return print(len(words_list[0]))

longest_word(words_list)

"""## 2: `calculate_grade`

You're a statistics professor and the deadline for submitting your students' grades is tonight at midnight. Each student's grade is determined by their mean score across all of the tests they took this semester.

You've decided to automate grade calculation by writing a function `calculate_grade` that takes a list of test scores as an argument and returns a one character string representing the student's grade calculated as follows:

```
90% <= mean score <= 100%: "A",
80% <= mean score < 90%: "B",
70% <= mean score < 80%: "C",
60% <= mean score < 70%: "D",
mean score < 60%: "F"
```


For example, `calculate_grade([92, 94, 99])` would return "A" since the mean score is 95, and `calculate_grade([50, 60, 70, 80, 90])` would return "C" since the mean score is 70.

Your function should handle an input list of any length greater than zero.
"""

# [92, 94, 99]
# [50, 60, 70, 80, 90]

score = [50, 60, 70, 80, 90]    

def calculate_grade(score): 

  sum_score = sum(score)
  len_score = len(score)
  mean_score = sum(score)/len(score)     #This gives the mean score of list

  if mean_score < 60:
    return print("F")
  elif mean_score >= 60 and mean_score < 70:
    return print("D")
  elif mean_score >= 70 and mean_score < 80: 
    return print("C")
  elif mean_score >= 80 and mean_score < 90:
    return print("B")
  elif mean_score >= 90 and mean_score < 100: 
    return print("A")

calculate_grade(score)

"""## 3: `process_data`

You have a two-dimensional list in the following format:

```python
data = [[2, 5], [3, 4], [8, 7]]
```

Each sub-list contains two items, and each item in the sub-lists is an integer.

Write a function `process_data` that processes each sub-list like so:

```
[2, 5] --> 2 - 5 --> -3
[3, 4] --> 3 - 4 --> -1
[8, 7] --> 8 - 7 --> 1
```

and then returns the product of all the processed sub-lists: -3 * -1 * 1 --> 3.
d
For input, you can trust that neither the main list nor the sublists will be empty.
"""

data = [[2, 5], [3, 4], [8, 7]]

def process_data(data):
  y = 1 
  for x in data:
    y *= x[0]-x[1]
  return y

process_data(data)

