import json
import pymysql
from datetime import datetime,timedelta

def sql_str(userslist):
    sqlstr = ''
    length = len(userslist)
    i = 0
    for lst in userslist:
        i = i + 1
        if (i != length):
            sqlstr = sqlstr + "'" + lst + "',"
        else:
            sqlstr = sqlstr + "'" + lst + "'"

    #print(sqlstr)
    return sqlstr

def response_json(userslist):
    sqlstr = sql_str(userslist)
    db = pymysql.connect('localhost', 'subbu123', 'subbu123', 'csservice')
    cur = db.cursor(pymysql.cursors.DictCursor)
    sql = "select * from users_cs where username in ("+sqlstr+")"
    #print(sql)
    cur.execute(sql)

    data = {}

    count = 0
    for row in cur:
        #print(row['username']+' -- '+str(row['cibilscore']))
        data[row['username']] = row['cibilscore']
        json_data = json.dumps(data)
        count = count+1

    return json_data

# Create database connection and get get the usernames
import sqlalchemy
import pandas as pd
from sklearn.utils import shuffle
engine = sqlalchemy.create_engine('mysql+pymysql://subbu123:subbu123@localhost:3306/mybank')
users = pd.read_sql_table('users',engine, columns=['username'])
#print(users.head())

# Shuffle users and get a random sample of 100 users
df = shuffle(users)
random_users = df.sample(n=100, random_state=1)
#print(random_users.head())

users_list = list(random_users['username'])
#print(users_list)

sqlstr = sql_str(users_list)
#print('users are: ',sqlstr)

db = pymysql.connect('localhost', 'subbu123', 'subbu123', 'mybank')
cur = db.cursor(pymysql.cursors.DictCursor)
sql = "select * from users_cs_ordered where username in ("+sqlstr+") and DATEDIFF(CURDATE(), date_ordered) > 1"
#print(sql)
cur.execute(sql)

for row in cur:
    #print("Credit score already ordered for: ")
    #print(row['username']+' -- '+str(row['date_ordered']))
    users_list.remove(row['username'])

#print('updated users list: ')
#print(users_list)
json_data = response_json(users_list)
jsondata = json.loads(json_data)

df_csscores = pd.DataFrame(jsondata.items(), columns=['username', 'cibilscore'])

now = datetime.now()
df_csscores['date_ordered'] = now.date()
print(df_csscores.head())

import sqlalchemy
engine = sqlalchemy.create_engine('mysql+pymysql://subbu123:subbu123@localhost:3306/mybank')
df_csscores.to_sql('users_cs_ordered', con=engine, index=False, if_exists='append')