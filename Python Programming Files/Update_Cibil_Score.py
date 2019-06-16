import numpy as np
import pandas as pd
import sqlalchemy

# Create database connection and get get the usernames
engine = sqlalchemy.create_engine('mysql+pymysql://subbu123:subbu123@localhost:3306/mybank')
users = pd.read_sql_table('users',engine, columns=['username'])
print(users.head())

def get_creditscore(cr):
    rand_no = np.random.randint(1,6)
    if(rand_no == 1):
        score = np.random.randint(300, 601)
        return score
    if (rand_no == 2):
        score = np.random.randint(601, 650)
        return score
    if (rand_no == 3):
        score = np.random.randint(650, 700)
        return score
    if (rand_no == 4):
        score = np.random.randint(700, 750)
        return score
    if (rand_no == 5):
        score = np.random.randint(750, 900)
        return score


users['cibilscore'] = users['username'].apply(get_creditscore)
print(users.head())
print(users.count())

import sqlalchemy
engine = sqlalchemy.create_engine('mysql+pymysql://subbu123:subbu123@localhost:3306/csservice')
users.to_sql('users_cs',con=engine,index=False,if_exists='append')
