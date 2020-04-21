# -*- coding: utf-8 -*-
"""M32.04 - Assignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1k8HXa2-VEbZvxp_1NvHcdG8N5OMwHQGh
"""

#1. Given the variable 
my_list = ['h', 'e', 'l', 'l', 'o']
print(len(my_list))

#2. Given the variables
list_1 = [1, 2, 3]
list_2 = [4]

# What is the result of the below? 
print(list_1 + list_2)
print(list_2 + list_1)

#3. Given a dictionary 
d = {"Barry":762, "Hank":755}

#which items are keys, and which are values

#ANSWER: Barry is the key with the value of 762
#ANSWER: Hank is the key with the value of 755

#4. Which of the below variables are valid dictionaries?
d_1 = {}  #Valid Dictionary
d_2 = {"Barry":762, "Hank":755} #Valid Dictionary
d_3 = {762:"Barry", 755:"Hank"} #Valid Dictionary

print(d_3[762])

#5. What is the result of the below? 
d = {"Barry":762, "Hank":755}
#Result: 755

d["Hank"] #or 
print(d["Hank"])

