import os, json
import pandas as pd
from pandas.io.json import json_normalize

path ='C:\\Users\\Christopher\\craigslist\\'
jsn = 'results-jobs-multi-pages-content.json'
json_data = open(os.path.join(path, jsn))

raw = json.load(json_data)
text = raw.read()
df = pd.io.json.json_normalize(raw)


jsn ='C:\\Users\\Christopher\\craigslist\\results-jobs-multi-pages-content.json'
with open(jsn) as json_data:
    data = json.load(json_data)


df = pd.io.json.json_normalize(data.json())
df = pd.read_json(data)