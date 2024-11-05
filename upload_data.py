from pymongo.mongo_client import MongoClient
import pandas as pd
import json
 

#url
uri="mongodb+srv://Pragatibandal:Pragati%40123@cluster0.qgkym.mongodb.net/?retryWrites=true&w=majority"

client=MongoClient(uri)

#create a database name and collection name

DATABASE_NAME="Sensor_project"
COLLECTION_NAME="Waferfault"

df = pd.read_csv("C:\Users\praga\Desktop\DataAnalytics\ML project\notebooks\wafer_23012020_041211.csv")
df
df.head()
df=df.drop("Unnamed: 0",axis=1)
df

json_record=list(json.loads(df.T.to_json()).values())

type(json_record)
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)