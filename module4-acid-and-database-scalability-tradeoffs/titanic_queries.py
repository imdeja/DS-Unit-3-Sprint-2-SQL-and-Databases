import os
from dotenv import load_dotenv
import pandas as pd
import psycopg2
from psycopg2.extras import execute_values
import json
import numpy as np

load_dotenv()


DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST= os.getenv("DB_HOST")


conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
curs = conn.cursor()

#- How many passengers survived, and how many died?
query = 'SELECT count(survived) from passengers where survived = 0'
curs.execute(query)
hi = curs.fetchone()
print(hi[0], "passengers died.")
query = 'SELECT count(survived) from passengers where survived = 1'
curs.execute(query)
hi = curs.fetchone()
print(hi[0], "passengers survived.")
#- How many passengers were in each class?
class1 = 'SELECT count(pclass) from passengers where pclass =1'
curs.execute(class1)
hi = curs.fetchone()
print("There were", hi[0], "passengers in class 1.")
class2 = 'SELECT count(pclass) from passengers where pclass =2'
curs.execute(class2)
hi = curs.fetchone()
print("There were", hi[0], "passengers in class 2.")
class3 = 'SELECT count(pclass) from passengers where pclass =3'
curs.execute(class3)
hi = curs.fetchone()
print("There were", hi[0], "passengers in class 3.")
#- How many passengers survived/died within each class?
died = 'SELECT count(pclass) from passengers where survived = 0 and pclass =1'
curs.execute(died)
hi = curs.fetchone()
print("There were", hi[0], "passengers who died in class 1.")
survived = 'SELECT count(pclass) from passengers where survived = 1 and pclass =1'
curs.execute(survived)
hi = curs.fetchone()
print("There were", hi[0], "passengers who survived in class 1.")
died1 = 'SELECT count(pclass) from passengers where survived = 0 and pclass =2'
curs.execute(died1)
hi = curs.fetchone()
print("There were", hi[0], "passengers who died in class 2.")
survived1 = 'SELECT count(pclass) from passengers where survived = 1 and pclass =2'
curs.execute(survived1)
hi = curs.fetchone()
print("There were", hi[0], "passengers who survived in class 2.")
died2 = 'SELECT count(pclass) from passengers where survived = 0 and pclass =3'
curs.execute(died2)
hi = curs.fetchone()
print("There were", hi[0], "passengers who died in class 3.")
survived2 = 'SELECT count(pclass) from passengers where survived = 1 and pclass =3'
curs.execute(survived2)
hi = curs.fetchone()
print("There were", hi[0], "passengers who survived in class 3.")
#- What was the average age of survivors vs nonsurvivors?
avg_dead = 'select avg(age) from passengers where survived =0'
curs.execute(avg_dead)
hi = curs.fetchone()
print("The average age of passengers who died was", hi[0])
avg_surv = 'select avg(age) from passengers where survived =1'
curs.execute(avg_surv)
hi = curs.fetchone()
print("The average age of passengers who survived was", hi[0])
#- What was the average age of each passenger class?
class1 = 'select avg(age) from passengers where pclass =1'
curs.execute(class1)
hi = curs.fetchone()
print("The average age of passengers in class 1 was", hi[0])
class2 = 'select avg(age) from passengers where pclass =2'
curs.execute(class2)
hi = curs.fetchone()
print("The average age of passengers in class 2 was", hi[0])
class3 = 'select avg(age) from passengers where pclass =3'
curs.execute(class3)
hi = curs.fetchone()
print("The average age of passengers in class 3 was", hi[0])
#- What was the average fare by passenger class? By survival?
class1 = 'select avg(fare) from passengers where pclass =1'
curs.execute(class1)
hi = curs.fetchone()
print("The average fare of passengers in class 1 was", hi[0])
class2 = 'select avg(fare) from passengers where pclass =2'
curs.execute(class2)
hi = curs.fetchone()
print("The average fare of passengers in class 2 was", hi[0])
class3 = 'select avg(fare) from passengers where pclass =3'
curs.execute(class3)
hi = curs.fetchone()
print("The average fare of passengers in class 3 was", hi[0])
avg_dead = 'select avg(fare) from passengers where survived =0'
curs.execute(avg_dead)
hi = curs.fetchone()
print("The average fare of passengers who died was", hi[0])
avg_surv = 'select avg(fare) from passengers where survived =1'
curs.execute(avg_surv)
hi = curs.fetchone()
print("The average fare of passengers who survived was", hi[0])
#- How many siblings/spouses aboard on average, by passenger class? By survival?
class1 = 'select avg(sib_spouse_count) from passengers where pclass =1'
curs.execute(class1)
hi = curs.fetchone()
print("The average siblings/spouses aboard in class 1 was", hi[0])
class2 = 'select avg(sib_spouse_count) from passengers where pclass =2'
curs.execute(class2)
hi = curs.fetchone()
print("The average siblings/spouses aboard in class 2 was", hi[0])
class3 = 'select avg(sib_spouse_count) from passengers where pclass =3'
curs.execute(class3)
hi = curs.fetchone()
print("The average siblings/spouses aboard in class 3 was", hi[0])
avg_dead = 'select avg(sib_spouse_count) from passengers where survived =0'
curs.execute(avg_dead)
hi = curs.fetchone()
print("The average siblings/spouses aboard of passengers who died was", hi[0])
avg_surv = 'select avg(sib_spouse_count) from passengers where survived =1'
curs.execute(avg_surv)
hi = curs.fetchone()
print("The average siblings/spouses aboard of passengers who survived was", hi[0])
#- How many parents/children aboard on average, by passenger class? By survival?
class1 = 'select avg(parent_child_count) from passengers where pclass =1'
curs.execute(class1)
hi = curs.fetchone()
print("The average parents/children aboard in class 1 was", hi[0])
class2 = 'select avg(parent_child_count) from passengers where pclass =2'
curs.execute(class2)
hi = curs.fetchone()
print("The average parents/children aboard in class 2 was", hi[0])
class3 = 'select avg(parent_child_count) from passengers where pclass =3'
curs.execute(class3)
hi = curs.fetchone()
print("The average parents/children aboard in class 3 was", hi[0])
avg_dead = 'select avg(parent_child_count) from passengers where survived =0'
curs.execute(avg_dead)
hi = curs.fetchone()
print("The average parents/children aboard of passengers who died was", hi[0])
avg_surv = 'select avg(parent_child_count) from passengers where survived =1'
curs.execute(avg_surv)
hi = curs.fetchone()
print("The average parents/children aboard of passengers who survived was", hi[0])
#- Do any passengers have the same name?
name = 'SELECT count(distinct name) from passengers having count(*) >1'
curs.execute(name)
hi = curs.fetchone()
print("All", hi[0], "passengers have a different name.")
#nope!
# (Bonus! Hard, may require pulling and processing with Python) How many married
  #couples were aboard the Titanic? Assume that two people (one `Mr.` and one
  #`Mrs.`) with the same last name and with at least 1 sibling/spouse aboard are
  #a married couple.