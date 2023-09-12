import pandas as pd
import sqlite3

DBNAME = "r3spons3s.db"
TABLENAME = "PANDASRGOOD"

db = sqlite3.connect(DBNAME, check_same_thread=False)

df = pd.read_sql_query("SELECT * FROM {}".format(TABLENAME), db)

print(df)

df.to_csv("responses.csv")
