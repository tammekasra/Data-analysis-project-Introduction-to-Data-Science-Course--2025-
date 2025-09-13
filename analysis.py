

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


'''
This loads our data as csv from our repository
'''
stress_df = pd.read_csv('Stress_Dataset.csv')
stress_level_df = pd.read_csv('StressLevelDataset.csv')



'''
This just does the StressLevelDataset.csv

'''


plt.figure(figsize=(12, 8))
sns.heatmap(stress_level_df.corr(), annot=True, cmap='coolwarm')
plt.title('Heatmap - StressLevelDataset.csv')
plt.tight_layout()
plt.show()



'''
This makes the heatmap look prettier
'''
stress_corr = stress_level_df.corr()['stress_level']
stress_corr_sorted = stress_corr.sort_values(ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x=stress_corr_sorted.values, y=stress_corr_sorted.index, palette='coolwarm')
plt.title('Correlation of Factors with Stress Level')
plt.xlabel('Correlation Coefficient')
plt.ylabel('Factor')
plt.tight_layout()
plt.show()


'''
This is for the Stress_DataSet.csv
'''
#plt.figure(figsize=(12, 8))
#sns.heatmap(stress_df.corr(numeric_only=True), annot=True, fmt='.2f', cmap='coolwarm')
#plt.title('Heatmap - Stress_Dataset.csv')
#plt.tight_layout()
#plt.show()



'''
We can divide the data into two - low stress and high stress students and see
how they correlate with sleep_quality, self_esteem,academic_performance,future_career_concerns
if there are any signficant changes.
'''

'''
Here we just take median and later split it to low stress (below median values) and high stress
'''
median_stress = stress_level_df['stress_level'].median()



'''
Here we add a new column to the database (StressLevelDataset).
Since we have a median, we can use the np.where function to differtiate the values
e.g if stress value is 1,2,3 then it's low stress and we add True value to it in the column
and if it is 4,5,6 then we add False since it is high stress.

When we have only TRUE and FALSE values instead of numbers we can see how many TRUE
values correlate with other attributes.


	stress_level	stress_group
0	1	Low Stress(True)
1	2	High Stress(False)
2	1	Low Stress(True)
3	2	High Stress(False)
'''

stress_level_df['stress_group'] = np.where(stress_level_df['stress_level'] > median_stress, 
                                          'High Stress', 
                                          'Low Stress')

'''
This is just the attributes that were highly correlated from the heatmap
'''

factors_to_compare = ['sleep_quality', 'self_esteem', 'academic_performance', 'future_career_concerns']


'''
This just calculates the average value for each of those columns within each group."


'''
comparison_df = stress_level_df.groupby('stress_group')[factors_to_compare].mean().T
print(comparison_df)


comparison_df.plot(kind='bar', figsize=(10, 6), color=['lightcoral', 'lightgreen'])
plt.title('Average Factor Levels by Stress Group')
plt.ylabel('Average Score')
plt.legend(title='Stress Group')
plt.show()











