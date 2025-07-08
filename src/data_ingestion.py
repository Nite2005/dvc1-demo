
import pandas as pd
import numpy as np
import os
df = pd.read_csv('https://raw.githubusercontent.com/araj2/customer-database/refs/heads/master/Ecommerce%20Customers.csv')

df.drop(columns=['Length of Membership'],inplace=True)

df.iloc[:,3:]

df.to_csv(os.path.join('data','customer.csv'))
