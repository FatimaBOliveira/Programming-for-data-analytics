# Program tips that shows regression of tips.
# Author: Fatima Oliveira

# Libraries.
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# load the dataset
dataset = sns.load_dataset('tips')
print(dataset.head())

sns.set_style('whitegrid')
#sns.lmplot(x='total_bill', y='tip', order=1, data=dataset)

#sns.lmplot(x="size", y="tip", data=dataset)
#sns.lmplot(x="size", y="tip", data=dataset, x_jitter=.05) # jitter, random  uniform noise added, "size" has discrete values
# "This can be helpful when plotting variables that take discrete values."

# Estimate mean tip 
sns.lmplot(x="size", y="tip", data=dataset, x_estimator=np.mean)

plt.show()