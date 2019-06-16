import numpy as np
import pandas as pd
import re

def remove_non_alpha(name):
    name = re.sub('[^a-zA-Z\s]', '', name)
    name = re.sub('\s+', ' ', name)
    return name

def fill_NaN(name):
    if re.compile('[a-zA-Z]+').search(name):
        return name
    else:
        return np.nan

male_names = pd.read_csv('D:\Python_Subbu\Project\indian-names\Indian-Names.csv')
pd.set_option('display.max_columns', None)
male_names.index.name = 'id'
#print(male_names.head())
male_names.drop('race', inplace=True, axis=1)

#remove non alpha values
male_names['name'] = male_names['name'].apply(remove_non_alpha)

#replacing names with only whitespaces or no values at all with NaN
male_names['name'] = male_names['name'].apply(fill_NaN)

male_names.dropna(inplace=True, how='any')

#male_names.to_csv('test.csv')
#print('Null Values are', male_names['name'].isnull().sum().sum())

male_names['password'] = 'pass123'
print(male_names.head())

# Generate usernames
def generate_user_name(username):
    return str(username.replace(" ", ""))

male_names['username'] = male_names['name'].apply(generate_user_name)

#male_names.drop('uname',inplace=True,axis=1)

#print(male_names.head())

# Generate mobile phone numbers
def generate_mobile_no(index):
    start_no = 9111111111
    return start_no + index

male_names['mobilephone'] = male_names.index.map(generate_mobile_no)
print(male_names.head())

# Generate Landline numbers
def generate_landline_no(index):
    start_no = 4011111111
    return start_no + index

male_names['landphone'] = male_names.index.map(generate_landline_no)
print(male_names.head())

# Updating address
male_names['address'] = 'test apartments,' \
                        '123 test street,' \
                        'Hyderabad - 500087'

print(male_names.head())
male_names.columns = ['firstname', 'gender', 'password','username','mobilephone','landphone','address']
#print(male_names.head())

import sqlalchemy
engine = sqlalchemy.create_engine('mysql+pymysql://subbu123:subbu123@localhost:3306/mybank')
male_names.to_sql('users',con=engine,index=False,if_exists='append')