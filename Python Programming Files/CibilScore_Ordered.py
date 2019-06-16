import numpy as np
import pandas as pd
import sqlalchemy
from datetime import datetime,timedelta

# Create database connection and get get the usernames
engine = sqlalchemy.create_engine('mysql+pymysql://subbu123:subbu123@localhost:3306/csservice')
users_cs = pd.read_sql_table('users_cs',engine)
print(users_cs.head())

users_cs_sample = users_cs.sample(n=1000, random_state=1)
users_cs_sample.drop('id', axis=1, inplace=True)
print(users_cs_sample.head())

now = datetime.now()
print(now.date())
print(now.date()-timedelta(days=10))

users_cs_sample['date_ordered'] = now.date()-timedelta(days=10)
print(users_cs_sample.head())

import sqlalchemy
engine = sqlalchemy.create_engine('mysql+pymysql://subbu123:subbu123@localhost:3306/mybank')
users_cs_sample.to_sql('users_cs_ordered',con=engine,index=False,if_exists='append')