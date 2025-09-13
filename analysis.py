

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


'''
This loads our data as csv from our repository
'''
stress_df = pd.read_csv('Stress_Dataset.csv')
stress_level_df = pd.read_csv('StressLevelDataset.csv')



'''
This just does the StressLevelDataset.csv

'''


plt.figure(figsize=(12, 8))
sns.heatmap(stress_level_df.corr(), annot=True, fmt='.2f', cmap='coolwarm')
plt.title('Heatmap - StressLevelDataset.csv')
plt.tight_layout()
plt.show()


'''
This is for the Stress_DataSet.csv
'''
plt.figure(figsize=(12, 8))
sns.heatmap(stress_df.corr(numeric_only=True), annot=True, fmt='.2f', cmap='coolwarm')
plt.title('Heatmap - Stress_Dataset.csv')
plt.tight_layout()
plt.show()