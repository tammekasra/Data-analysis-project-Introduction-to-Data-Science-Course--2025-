# Data-analysis-project-Introduction-to-Data-Science-Course--2025-
The idea behind the project is to explore possible available tools to measure and analize data associated with student overall mental health.

The data was taken from the following link that is is been data privacy proven and validated -
https://www.kaggle.com/datasets/mdsultanulislamovi/student-stress-monitoring-datasets  



## Heatmap Visualization

Heatmap is a useful tool in assessing correlations across all attributes within a data set for fast and reliable correlations.
-Red shows strong correlation - if a value increases, so does another attributes values
-Blue shows negative correlation - if a value increase, another attribute value will decrease, and vice versa
-White shows no correlation - meaning there is no findable correlation.

(Heatmap uses Pearson correlation coefficient, which measures linear relationships between - measures linear relationship with oneanother - covariance between variables X and Y is divided by standard deviations of X and Y)

!NB - Even if there is or not a correlation within shown graph - it does not necessarily mean there is "nothing" to be found - since it ONLY looks at linear relationships only.

![Heatmap Visualization](https://github.com/tammekasra/Data-analysis-project-Introduction-to-Data-Science-Course--2025-/blob/main/Heat_matp_visualization.png)

From the heatmap we can clearly see that -

Stress correlates strongly with:
Future career concerns are the #2 stress driver (0.74)
Academic performance is the #3 protective factor (0.72)
Study load has moderate impact (0.63) - Manageable but significant

Stress negatively correlates with:
Self-esteem (0.76) - Better self-esteem -> less stress
Sleep quality (0.78) - Low stress -> Better Sleep or vice verca
Academic performance (0.72) - Either poor academic performance causes stress or other way around

![Divide Stress Groups into two and correlate with the previous higher correlations!](https://github.com/tammekasra/Data-analysis-project-Introduction-to-Data-Science-Course--2025-/blob/main/Average_Factor_Levels_By_Stress_Group.png)
