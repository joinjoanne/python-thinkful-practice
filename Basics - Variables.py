# -*- coding: utf-8 -*-
"""M31.03 - Assignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wIKG5Duy9ooG4_93rAGAfIcq0mmktbi2
"""

# Joanne's Answers for M31.03 Assignment

# 1. Which of the following is a valid variable name?
# Answer: [E] None of the above

# 2. Assign the following three variables into a Jupyter cell:
party = "Party"
like = "like it's"
year = "1989!"

print("\n", party, "\n", like, "\n", year)

#3. Create a Python Mad Lib with the format:
# Roses are adjective
# Plural noun are blue
# Singular noun is adjective
# And so are you!

first_line = "Roses are {}"
second_line = "{} are blue"
third_line = "{} is {}"
fourth_line = "And so are you!"

first_line_adjective = input("Pick an adjective.")
second_line_plural_noun = input("Choose a plural noun.")
third_line_singular_noun = input("Choose a singular noun.")
third_line_adjective = input("Pick an adjective.")


print("\n", first_line.format(first_line_adjective), "\n", second_line.format(second_line_plural_noun), "\n",
      third_line.format(third_line_singular_noun, third_line_adjective), "\n", fourth_line)

# 4. Assign the name of a food to the variable food. 
# Then create a single print statement which renders as follows: 
# This food name is [name length] letters long. 
# For example, the result for food = "``pizza``" should be 
# This food name is 5 letters long.

food = "Japchae"
name_length = int(len(food))

print("This food name is ", name_length, " letters long.")

