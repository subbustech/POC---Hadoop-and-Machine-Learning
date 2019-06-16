import numpy as np
import pandas as pd
import sqlalchemy
import datetime
from sklearn.utils import shuffle

# Create database connection and get get the usernames
engine = sqlalchemy.create_engine('mysql+pymysql://subbu123:subbu123@localhost:3306/mybank')
users = pd.read_sql_table('users',engine, columns=['username'])
print(users.head())

# List of different IP Addresses
ipaddr = ['1.7.255.255','1.23.255.255','1.39.255.255','5.101.108.255','13.32.39.255','13.32.44.255','14.192.31.255','16.242.233.255','17.1.106.255','20.46.221.255','23.5.161.255','27.116.43.255']
# lists of different pages
majorsections = ['creditcards','personalloans','homeloans','carloans','investments']
investments = ['mutualfunds','goldschemes','recdeposit','flexiblerd']
pages = ['welcome.html','apply.html','terms.html','offers.html',]

count = 0
now = datetime.datetime.now()
fileext = str(now.year)+'_'+str(now.month)+"_"+str(now.day)+'_'+str(now.hour)+'_'+str(now.minute)+'_'+str(now.second)+'_'+str(now.microsecond)
print(fileext)
outF = open("mylogfile"+fileext+".txt", "w")
print(outF)
while(count < 100):
    random_ip_no = np.random.randint(0, len(ipaddr))
    ipaddress = ipaddr[random_ip_no]

    # Select random user by shuffling the dataframe and selecting the first row of the dataframe
    df = shuffle(users)
    random_user = df.iloc[0]['username']

    # select the major pages of major sections
    random_majorsection = np.random.randint(0, len(majorsections))

    # If the random major page is investments select the sub pages and form the first url
    # Else use the major page only to form the first url
    if(majorsections[random_majorsection] == 'investments'):
        random_investment_no = np.random.randint(0, len(investments))
        majorsectionpage = majorsections[random_majorsection]+'/'+investments[random_investment_no]
    else:
        majorsectionpage = majorsections[random_majorsection]

    # Get a random page no. and get the random sub page
    random_page_no = np.random.randint(0, len(pages))
    urlstr = majorsectionpage+'/'+pages[random_page_no]

    # Create the log file line
    log = ipaddress+' - '+random_user+' [10/Oct/2000:13:55:36 -0700] "GET /apache_pb.gif HTTP/1.0" 200 2326 "http://www.mybank.com/'+urlstr+'" "Mozilla/4.08 [en] (Win98; I ;Nav)'
    outF.write(log)
    outF.write("\n")
    print(log)
    count = count+1
outF.close()