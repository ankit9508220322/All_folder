import pandas as pd
import requests
import numpy as np

responce = requests.get(
    'https://rapidapi.com/rapidapi/api/movie-database-alternative/playground/apiendpoint_19019426-1f2d-467a-8e67-80f62266eac1'
)
data = pd.DataFrame(responce.json)
print(data)