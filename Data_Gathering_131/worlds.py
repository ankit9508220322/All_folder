import pandas as pd
import numpy as np
import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="world"
)
data=pd.read_sql_query('SELECT * FROM city',conn)
# print(data)

# ///////////////////////////////////////////////////////////////
# data is convert  json formate
# batsman -> teame name -> run
df = pd.read_csv('IPL Matches 2008-2020.csv')
# print(df)
data= df.groupby(['team1','venue','winner'])['result_margin'].sum().unstack().to_json('convert_json.json')
print(data)
# /////////////////////////////////////////////////

# this data is  convert sql formate
# before import -> 2 module
import pymysql
from sqlalchemy import create_engine
