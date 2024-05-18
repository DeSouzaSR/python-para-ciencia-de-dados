"""
This program tests the amount of calories in a product, based on a sample.

The null hypothesis is that the average is 31 calories. The alternative hypothesis is that the mean is different.

H0: mu = 31
h1: mu != 31
"""

#import modules
import pandas as pd
import numpy as np

# Read data from a plain text
data_array = np.genfromtxt('../data/raw_data/Amostras-Industria.csv', delimiter=',')

# Create dataframe from numpy array calories
df = pd.DataFrame({'calories':data_array})

# For the null hypothesis, we want mu = 31
mu = 31

# Sample size
n = len(df['calories'])

# Calculate variance and mean
mean = df['calories'].mean()
variance = df['calories'].var()

# Calculate t
t = (mean - mu)/np.sqrt(variance/n)

# Write out results
print('Data:')
for i in df['calories']:
    print(i, end=' ')

print()
print("mu: ", mu)
print("n: ", n)
print("mean: ", mean)
print("variance: ", variance)
print("t: ", t)

