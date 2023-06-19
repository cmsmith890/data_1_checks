import pandas as pd
import requests as re
import json

api_endpoint = "https://api.agify.io?name=meelad"

response = re.get(api_endpoint)
response_json = response_json()
df = pd.json_normalize(response_json)(["Name"], "year", "age, "gender",)
df.head()
print('Age')
print('Gender')

