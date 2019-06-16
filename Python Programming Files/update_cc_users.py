import numpy as np
import pandas as pd
from sklearn.utils import shuffle
import sqlalchemy

# Create database connection and get get the usernames
engine = sqlalchemy.create_engine('mysql+pymysql://subbu123:subbu123@localhost:3306/mybank')
users = pd.read_sql_table('users',engine, columns=['username'])
print(users.head())

df = shuffle(users)
random_users = df.sample(n=1000, random_state=1)
print(random_users.head())

def ccnumber(index):
    start_no = 5786675456451111
    return start_no + index

random_users['ccno'] = random_users.index.map(ccnumber)
print(random_users.head())

def random_ccamount(uname):
    random_no = np.random.randint(100,1000)*1000
    return random_no

random_users['cclimit'] = random_users['username'].apply(random_ccamount)
print(random_users.head())

import sqlalchemy
engine = sqlalchemy.create_engine('mysql+pymysql://subbu123:subbu123@localhost:3306/mybank')
random_users.to_sql('users_ccards',con=engine,index=False,if_exists='append')