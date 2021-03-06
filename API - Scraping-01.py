# -*- coding: utf-8 -*-
"""M32.03 - Assignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rlhKCvz6yBNIseakdi5hYWtI9kki8jF0
"""

# Write a program to fetch the names and birth places of all British persons listed in the API
# Refer to 'https://api.harvardartmuseums.org/RESOURCE_TYPE?apikey=YOUR_API_KEY'
# Refer to https://github.com/harvardartmuseums/api-docs/blob/master/sections/person.md

import requests

url = 'https://api.harvardartmuseums.org/person'
query = {'q':'culture:british', 'apikey':'fed58880-5ce3-11ea-8c5a-cb60061dc4a9'}

response = requests.get(url, params=query)
response.status_code

response.ok

data = response.json()

data

