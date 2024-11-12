#
# Author: Fatima Oliveira

# Libraries.
import re
import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
from datetime import datetime

# log doc.
logfile="./data/access.log"

# function that reads in the strings, and strips off the firsts and last characters
def parse_str(x):
    return x[1:-1]

# Write a function to read in the date in the format, it will also need to strip the first and last characters (ie the [])

def parse_datetime(x):
    dt = datetime.strptime(x[1:-1], '%d/%b/%Y:%H:%M:%S')
    return dt

df = pd.read_csv(logfile, sep=r'\s(?=(?:[^"]*"[^"]*")*[^"]*$)(?![^\[]*\])', 
                 engine='python', na_values='-', header=None, usecols=[0, 3, 4, 5, 6, 7, 8],
                 names=['ip', 'time', 'request', 'status', 'size', 'referer','user_agent'],
                 converters={'time': parse_datetime,'request': parse_str,'status': int,
                'size': int,'referer': parse_str,'user_agent': parse_str})

# https://docs.python.org/3/library/re.html


# New excel file with clean data.
#excelFilename = './data/log.xlsx'
#df.to_excel(excelFilename, index=False, sheet_name='data')

request = df.pop('request').str.split()
df['resource'] = request.str[1] # after the /, inclusive
df['method'] = request.str[0] # before the /, exclusive
# yes I could have used regex for this
# from the request get the string before the ?
df['url'] = request.str[1].str.split('?').str[0] # between the / and ?(/ inclusive)
#print(df["url"].head(3))

dfbyhour=df.resample('H',on='time').sum()
dfbyhour['hour'] = dfbyhour.index.hour
dfbyhour['date'] = dfbyhour.index.date


#sns.lmplot(x="hour", y="size", order=1 ,data=dfbyhour, x_jitter=0.5)
#sns.lmplot(x="hour", y="size", order=5 ,data=dfbyhour, x_jitter=0.5)
sns.residplot(x="hour", y="size", data=dfbyhour, order=1)
plt.show()