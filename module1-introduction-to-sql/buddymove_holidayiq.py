import numpy
import pandas as pd
import sqlite3
import os

DATABASE_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "module1-introduction-to-sql", "buddymove_holidayiq.csv")
df = pd.read_csv(DATABASE_FILEPATH)
print(df.shape)

FILEPATH = os.path.join(os.path.dirname(__file__), "..", "module1-introduction-to-sql", "buddymove_holidayiq.sqlite3")
conn = sqlite3.connect(FILEPATH)
df.to_sql('buddymove_holidayiq', conn, if_exists='replace')
curs = conn.cursor()
#How many users who reviewed at least 100 `Nature` in the category also
#reviewed at least 100 in the `Shopping` category?
query = '''SELECT COUNT()
from buddymove_holidayiq
where Nature > 99 and Shopping > 99'''
result = curs.execute(query).fetchall()
print("There are", result[0][0], "users who reviewed at least 100 `Nature` in the category also reviewed at least 100 in the `Shopping` category.")