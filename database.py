import pandas as pd
from sqlalchemy import create_engine
import pymysql

host = "localhost"
port = "3306"  
database = "redbus"
username = "root"
password = "Javi%40571998"
engine_string = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
engine = create_engine(engine_string)
tenstate=pd.read_csv('tenstate.csv')
table_name = "redbus"
tenstate.to_sql(table_name, engine,if_exists='replace', index=False)  #['fail', 'replace', 'append']
print("Data successfully pushed to PostgreSQL table!")