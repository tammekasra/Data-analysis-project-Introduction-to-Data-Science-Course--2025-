# Data-analysis-project-Introduction-to-Data-Science-Course--2025-
## 1. Introduction
Analyzing the connections of different factors in large datasets by hand is tedious. For this reason, honing and testing various methods to trace these connections for any dataset helps make this problem more manageable. In this project, we aim to determine practical solutions for tackling this problem by using a query dataset on factors that cause student stress from Kaggle (https://www.kaggle.com/datasets/mdsultanulislamovi/student-stress-monitoring-datasets).  The stress dataset was ideal for this because many aspects of our well-being correlate with the quality of stress we experience, aiding in the study of these correlations.

The solutions we are trying here include simpler correlation functions and predictive machine learning modeling. These methods were selected for assessment in this project because they are the most straightforward solutions to our problem. We observed that the strength of the correlation functions lies in their ability to more accurately evaluate two parts of the dataset, while predictive machine learning modeling is more helpful in providing a broader view of the entire dataset.
Our hypothesis for this project is that there are clear correlations in the dataset, which can be detected and assessed by our approaches to the scientific problem described here. These correlations should be similar but not entirely the same among the methods used. Additionally, we believe that the results provide insight into the effectiveness of these methods, helping us evaluate them as potential solutions to similar issues.


## 2. Materials and methods
### 2.1.	Stress monitoring dataset
The dataset is designed to collect information about stress, general well-being, and stress indicators in students' lives. It uses a varying  scales based on numbers that tell how often topic of the question happens. The query consists of 23 questions and includes 843 answers from college students aged 18-21. The dataset is also anonymized and otherwise preprocessed. This also means that there are no ethical concerns relating to the use of the dataset.

### 2.2.	Correlation function
The correlation function used in this project was the basic corr-function from the pandas Python package. This was done by using the Pearson correlation coefficient.  The function calculates the linear correlation between two sets of data. It gives a number between -1 and 1 as its answer, which is the ratio that defines how much the two datasets in question correlate with each other. with -1 having the opposite correlation with each other, 1 having a straightforward correlation, and 0 means that there is not any correlation. This method cannot detect other correlations that are not linear, but for the purposes of this project, this method suffices

### 2.3.	 Random forest
The machine learning model we decided to try was a random forest method. This method works by creating decision trees during the model's training and then outputting the average of the predicted trees, creating a linear regression model. This method considers the whole dataset when doing the correlation analysis, and it can account for non-linear correlations.

## 3. Results
### 3.1. Correlation function

A heatmap (Figure 1) is a valuable tool for assessing correlations across all attributes in a dataset, providing fast, reliable results. high values close to 1 are marked red and they show strong correlation so in this case if a value increases, so does another attribute's value. Low values close to -1 are marked blue shows negative correlation, meaning if a value increases, another attribute's value will decrease, and vice versa. White shows no correlation. 
Even if there is or is not a correlation within the graph shown, it does not necessarily mean there is nothing to be found, since it only looks at linear relationships. These other type of connections are tried to find with other methods, since this is a limitation with the correlation function.

![Heatmap Visualization](https://github.com/tammekasra/Data-analysis-project-Introduction-to-Data-Science-Course--2025-/blob/main/Heat_matp_visualization.png)
_Figure 1. Heatmap of the stress level dataset_

The problem with Heatmap is that with large number of attributes it becomes messy and hard to read and/or analyze. Thus we can modify the heatmap such that the correlation cofficient are in order.
We can pick the attributes that are correlated with stress and have these in an ascended order for easier representation (Figure 2). We were most interested in the correlations with general stress level so we decided to use it as the point that we can correlate the other coefficients on.

![Correlation Cofficients - Stress vs Other Attributes](https://github.com/tammekasra/Data-analysis-project-Introduction-to-Data-Science-Course--2025-/blob/main/Correlation_Coefficient.png)
_Figure 2. Coefficients in order as a function of stress_

From the correlation coefficient data we can clearly see that the top attributes in increasing stress are in order - 1) Bullying, 2)Future Career Concerns, 3) Anxiety level and 4) Depression.
The attributes that has that higher impact on lowering stress are 1)Self-esteem, 2)Sleep Quality, 3)Academic Performance and 4)Safety.

Since we previously saw which features highly and lowly correlate with overall-stress - it can be also plausible to divide stress groups into two (Figure 3.). Below the median is low stressed and up-ward median is highly 
stressed. We can see then which features actually influence stress. We can see that the self-esteem is the most significant attribute that influences stress marginally higher compared to other attributes.

![Divide Stress Groups into two and correlate with the previous higher correlations!](https://github.com/tammekasra/Data-analysis-project-Introduction-to-Data-Science-Course--2025-/blob/main/Average_Factor_Levels_By_Stress_Group.png)
_Figure 3. dataset divided to high and low stress_


### 3.2. Random Forest Classifier

![Random Forest Classification Analysis](https://github.com/tammekasra/Data-analysis-project-Introduction-to-Data-Science-Course--2025-/blob/main/Random_Forest_Predictions.png)
_Figure 4. Random forest predictive model_

While correlation analysis is useful for identifying linear relationships, it does not capture complex, non-linear interactions between features. To better understand which factors contribute most to student stress, we used a Random Forest Classifier a machine learning algorithm based on an ensemble of decision trees.
Key points about Random Forest:
                       -It combines multiple decision trees to reduce overfitting and improve prediction accuracy.
                       -Each tree “votes” on the stress level, and the final prediction is determined by majority voting.
                       -Unlike correlation, this method can capture non-linear relationships and interactions between variables.
                       -From the Random Forest analysis, we observed that:
                       -Features such as blood pressure, sleep quality, and anxiety level appear as strong predictors of stress, even if they did not have the highest linear correlations.

Self-esteem remains an important factor, but some health-related or lifestyle variables play a larger role when all variables are considered together (Figure 4.).

![Random Forest Confusion Matrix](https://github.com/tammekasra/Data-analysis-project-Introduction-to-Data-Science-Course--2025-/blob/main/Random%20Forest%20Confusion%20Matrix.png)
_Figure 5. Random forest classification matrix_

This extra analysis by classification matrix (Figure 5.) helps us to depict whether the model that we used, in this case Random Tree Forest, is good or not.

Diagonal (green): Correct predictions
-102 students with "No Stress" correctly identified
-97 students with "Somewhat" stress correctly identified
-98 students with "Very Stressed" correctly identified

Off-diagonal (red): Misclassifications

Very few errors overall, meaning that the results given by the model should be reliable.
## Discussion

Dataset shows us differing amounts of correlation between each part of it which was what we expected. This also means that we are at least to a context quantifying the correlation. The correlation responses of each method used here look quite straightforward and corroborate each other to a certain extent. The differences in methods result were expected, and in this case support the hypothesis. This is of course due the fact that different methods have different strengths and their usage should be evaluated before using them depending on the need of the user.
While we mainly used pretty much only the already pre-processed data, we also wanted to try selectively choosing values. The idea behind this was if something is correlating only negatively/positively and the inverse situation would not have change with the data it would distort the Pearson coefficient being closer to the zero than in actual case. To test a way around this we tried to selectively choose the higher and lower values separately and make heatmaps of both with the correlation function. This did not end up producing anything of use, since the dataset was a little too small making a lot of NaNs in process. Additionally, inconsistent scales made finding sensible results impossible. End product ended up being a partial heatmap that is not reliable (Figure X)
![Heatmap with low values](https://github.com/tammekasra/Data-analysis-project-Introduction-to-Data-Science-Course--2025-/blob/main/oikee.png)

_Figure X. Heatmap with bottom 40 % of values in y-axis. White pots are empty
## Conclusions
In general, we used the correlation function and machine learning methods to find differing amounts of correlations in the dataset. The models were clear and results they gave sensible. Correlation function was useful in finding connections on a smaller scale, while the predictive machine learning models were helpful in covering the weaknesses of the more simple function. We found that these are helpful tools in detecting correlations in large datasets, but the usage should be evaluated in case-by-case basis.
