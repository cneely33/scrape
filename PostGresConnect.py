import psycopg2
#import sys

conn_string = "host='localhost' dbname='Spyder' user='postgres' password='DiabloOverwatchEnd'"

print("Connecting to database {0}".format(conn_string))

conn = psycopg2.connect(conn_string)

cursor = conn.cursor()
print("Connected!\n")
