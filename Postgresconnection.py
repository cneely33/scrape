# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 20:57:17 2017

@author: Christopher
"""
#tutorial
# https://wiki.postgresql.org/wiki/Psycopg2_Tutorial

import psycopg2

try:
    conn = psycopg2.connect("dbname='Spyder' user='postgres' host='localhost' password=''")
except:
    print("Unable to connect to database")
    

#create postgresql cursor
cur = conn.cursor()

#select the names of all DBs
cur.execute("""SELECT datname from pg_database""")

#assin the list of DB names to rows
rows = cur.fetchall()

#print the DB names
print("\nShow me the databases:\n")
for row in rows:
    print("   ", row[0])