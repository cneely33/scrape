import psycopg2
import pandas as pd
import numpy as np

#### Connect to Postgresql server ####
conn_string = "host='localhost' dbname='Spyder' user='postgres' password='DiabloOverwatchEnd'"

print("Connecting to database {0}".format(conn_string))

conn = psycopg2.connect(conn_string)

cursor = conn.cursor()
print("Connected!\n")

### SQL Statement ###
postgres = "SELECT * FROM public.policejobs"

df = pd.read_sql(postgres, conn)

### Select a random row from dataframe ###
#TODO change this to make the SQL statement pick a random row
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
smtpObj.login('BeTheChangeJohn@gmail.com', 'DiabloOverwatchEnd')
    
    #send a test email
smtpObj.sendmail('BeTheChangeJohn@gmail.com', '4074544725@txt.att.net',
                    'Sarah truly can F**K THA POLICE when you\
 work for Law Enforcement! Apply\
 for {0} at {1} in lovely {2} \
 with link {3}'.format(title, company, location, link))

smtpObj.sendmail('BeTheChangeJohn@gmail.com', '4074544725@txt.att.net',
                    'Sarah truly can FUCK THA POLICE when you\
 work for Law Enforcement! Apply\
 for {0} at {1} in lovely {2} \
 with link {3}'.format(title, company, location, link))

smtpObj.sendmail('BeTheChangeJohn@gmail.com', 'cneely33@gmail.com',
                    'Sarah truly can FUCK THA POLICE when you\
 work for Law Enforcement! Apply\
 for {0} at {1} in lovely {2} \
 with link {3}'.format(title, company, location, link))

smtpObj.sendmail('BeTheChangeJohn@gmail.com', '2258038146@messaging.sprintpcs.com',
                    'Test \
 work for Law Enforcement! Apply\
 for {0} at {1} in lovely {2} \
 with link {3}'.format(title, company, location, link))

#print('Subject: Law Enforcement Jobs! \n Be The Change You Want to See! \
#Apply for a {0} at {1} in lovely {2} \
#with this link {3}'.format(title, company, location, link))

#Eicher
#4074544725@txt.att.net                     
#dupes
#3372902976@txt.att.net  
    #close the SMTP connetion
smtpObj.quit()



conn.close()