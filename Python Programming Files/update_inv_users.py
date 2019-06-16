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

def invnumber(index):
    start_no = 5462563672311111
    return start_no + index

random_users['invno'] = random_users.index.map(invnumber)
#print(random_users.head())

investments = ['mutualfunds','goldschemes','recdeposit','flexiblerd']
def invtype(uname):
    random_investment_no = np.random.randint(0, len(investments))
    return investments[random_investment_no]

random_users['invtype'] = random_users['username'].apply(invtype)

def random_invamount(uname):
    random_no = np.random.randint(1, 100)*100000
    return random_no

random_users['invamount'] = random_users['username'].apply(random_invamount)
print(random_users.head())

import sqlalchemy
engine = sqlalchemy.create_engine('mysql+pymysql://subbu123:subbu123@localhost:3306/mybank')
random_users.to_sql('users_inv', con=engine, index=False, if_exists='append')