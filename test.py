import pandas as pd
import sqlite3

# Read sqlite query results into a pandas DataFrame
con = sqlite3.connect("RaMBLE-test1.sqlite")

cursorObj = con.cursor()

cursorObj.execute('SELECT name from sqlite_master where type= "table"')

print("Tables in loaded file: ", cursorObj.fetchall())


df = pd.read_sql_query("SELECT * from devices", con)

# Verify that result of SQL query is stored in the dataframe
print(df.columns)

print(df.loc[df['device_name'] == "JamppaMini", ['raw_adv_data']])


con.close()
