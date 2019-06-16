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

def clnumber(index):
    start_no = 1953452456411111
    return start_no + index

random_users['clno'] = random_users.index.map(clnumber)
print(random_users.head())

def random_clamount(uname):
    random_no = np.random.randint(5,26)*100000
    return random_no

random_users['cllimit'] = random_users['username'].apply(random_clamount)
print(random_users.head())

import sqlalchemy
engine = sqlalchemy.create_engine('mysql+pymysql://subbu123:subbu123@localhost:3306/mybank')
random_users.to_sql('users_cl', con=engine, index=False, if_exists='append')