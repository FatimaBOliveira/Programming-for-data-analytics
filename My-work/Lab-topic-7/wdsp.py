# Program that checks is there's any relation between the windspeed and the month in knock
#"https://cli.fusio.net/cli/climate_data/webdata/mly4935.csv"
# Author: Fatima Oliveira

# Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("https://cli.fusio.net/cli/climate_data/webdata/mly4935.csv", skiprows=19)
print(df.head(3))
#print(df.dtypes)

# Correlation between month and mean temperature.
corrtemp = df["month"].corr(df["meant"])
print(corrtemp) # +-0.261, no correlantion

#############################################################################################
# New DataFrame with only Month and Wind Speed.
cleandf = df[["month","wdsp"]]

# Replace empty spaces with NaN.
cleandf['wdsp']= cleandf.loc[:,('wdsp')].replace(' ', np.nan)

# Drop the rows with NaN values.
cleandf.dropna(inplace=True)
#print(cleandf.head(3))

# Changes values to float type to do correlation.
cleandf['wdsp'] = cleandf['wdsp'].astype(float)

corrwind = cleandf["month"].corr(cleandf["wdsp"])
print (f"wind correlation {corrwind}")  # +- -0.199, weak correlation

# Linear regression for better analysis.
sns.set_style('whitegrid')
#sns.scatterplot(x="month",y="wdsp",data=cleandf)
sns.lmplot(x='month', y='wdsp', order=3, data=cleandf)
plt.show()