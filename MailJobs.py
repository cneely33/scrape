import psycopg2
import pandas as pd
import numpy as np

from secrets import secrets
from os import getenv

secrets.load_env_vars()

#### Connect to local Postgresql server ####
password = getenv('Local_Postgres')
conn_string = "host='localhost' dbname='Spyder' user='postgres' password={password}".format(password=password)

conn = psycopg2.connect(conn_string)
cursor = conn.cursor()
print("Connected\n")

### SQL Statement ###
postgres = "SELECT * FROM jobs"

df = pd.read_sql(postgres, conn)

conn.close()

### Select a random row from dataframe ###
row = np.random.choice(df.index.values, 1)

df_1 = df.iloc[row]
df_1 = df_1.reset_index(drop=True)

title = df_1.title[0]
link = df_1.link[0]
location = df_1.location[0]
company = df_1.company[0]


    ################################################
    ######## Start Mail Portion of Project #########
    ################################################
import smtplib  
    #Create SMTP Object for Gmail
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    
    #Wake up the SMTP connection
smtpObj.ehlo()
    
    #stat up TLS connection
smtpObj.starttls()
    
    #Login to Gmail account
smtpObj.login('BeTheChangeJohn@gmail.com', getenv('eicher_email'))
    
    #send a test email
smtpObj.sendmail('BeTheChangeJohn@gmail.com', '4074544725@txt.att.net',
                    'Apply for {0} at {1} in lovely {2} with link {3}'.format(title, company, location, link))

smtpObj.quit()

