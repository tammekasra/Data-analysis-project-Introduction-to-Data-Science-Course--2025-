

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
These below just check if we have any missing data
'''
print(stress_df.isnull().sum())
print(stress_level_df.isnull().sum())

'''
This just uploads the StressLevelDataset.csv

'''

'''
Figure 1 - heatmap
'''

plt.figure(figsize=(12, 8))
sns.heatmap(stress_level_df.corr(), annot=True, cmap='coolwarm')
plt.title('Heatmap - StressLevelDataset.csv')
plt.tight_layout()
plt.show()



'''
This makes the heatmap look prettier
(figure 2.)
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


'''
Figure 3 - Median of for stress levels
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


'''
Picture 4 - Here we make a scatter plot. We add self-esteem and sleep-quality together
and future career concerns and anxiety levels.

This allows us to see if two attributes combined will show any meaningful representation.
'''

stress_level_df['protection_score'] = stress_level_df['self_esteem'] + stress_level_df['sleep_quality']
stress_level_df['risk_score'] = stress_level_df['future_career_concerns'] + stress_level_df['anxiety_level']


plt.figure(figsize=(10, 6))
sns.scatterplot(x='risk_score', y='protection_score', hue='stress_group', 
                data=stress_level_df, alpha=0.7)
plt.title('Self-esteem and Sleep Quality  vs  Future Career Concerns and Anxiety')
plt.xlabel('Anxiety + Career Concerns')
plt.ylabel('Self-esteem +sleep')
plt.show()





'''
Plot 5 - RandomTreeForest Classifier - it predicts which features affect stress the most via

Measures how much each feature reduces impurity (or improves predictions) across all trees.

It considers interactions between variables and non-linear relationships.

A feature that is weakly correlated linearly with stress might still be very useful for prediction
in combination with other features.
'''


from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


features = ['anxiety_level','self_esteem','mental_health_history',
            'depression','headache','blood_pressure','sleep_quality',
            'breathing_problem','noise_level','living_conditions',
            'safety','basic_needs','academic_performance','study_load',
            'teacher_student_relationship','future_career_concerns','social_support'
            ,'peer_pressure','extracurricular_activities','bullying'
]


X = stress_level_df[features]
y = stress_level_df['stress_level']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

importances = pd.Series(clf.feature_importances_, index=features)
importances.sort_values().plot(kind='barh', figsize=(12, 12), color='skyblue')
plt.title('Random Forest Feature Importance for Stress Levels', fontsize=16)
plt.xlabel('Importance Score', fontsize=14)
plt.ylabel('Features', fontsize=14)
plt.tight_layout()
plt.show()



'''
Plot 6 - this helps to group three stress levels within the Random Tree Forest
'''

#import shap

#class_names = ['No Stress', 'Somewhat Stressed', 'Very Stressed']
#explainer = shap.Explainer(clf, X, feature_names=X.columns)
#shap_values = explainer(X)
#shap.summary_plot(shap_values, X, plot_type="bar", class_names=class_names)
#shap.summary_plot(shap_values, X, class_names=class_names)


'''

Model evluation
'''

from sklearn.metrics import classification_report, confusion_matrix

y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=['No Stress','Somewhat','Very Stressed'],
            yticklabels=['No Stress','Somewhat','Very Stressed'])
plt.title('Random Forest Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()











import math

numeric_features = ['sleep_quality', 'self_esteem', 'academic_performance',
                    'future_career_concerns', 'anxiety_level', 'depression']

plt.figure(figsize=(14, 10))
for i, col in enumerate(numeric_features):
    plt.subplot(3, 3, i+1)
    sns.histplot(stress_level_df[col], kde=True, bins=20, color='skyblue')
    plt.title(f'{col} Distribution')
plt.tight_layout()
plt.show()




num_plots = len(numeric_features)
cols = 1  # Only 1 column for more vertical space
rows = num_plots

plt.figure(figsize=(10, 6*rows))  

for i, col in enumerate(numeric_features):
    plt.subplot(rows, cols, i+1)
    sns.kdeplot(
        data=stress_level_df, 
        x=col, 
        hue='stress_group', 
        fill=True, 
        common_norm=False, 
        alpha=0.5
    )
    plt.title(f'{col} by Stress Group')

plt.tight_layout()
plt.show()



