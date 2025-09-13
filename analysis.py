import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load datasets
stress_df = pd.read_csv("Stress_Dataset.csv")
mental_df = pd.read_csv("StressLevelDataset.csv")

# Select numeric / Likert-scale columns for heatmap

# Dataset 1: Stress_Dataset
stress_cols = [
    'Age',
    'Have you recently experienced stress in your life?',
    'Have you noticed a rapid heartbeat or palpitations?',
    'Have you been dealing with anxiety or tension recently?',
    'Do you face any sleep problems or difficulties falling asleep?',
    'Have you been getting headaches more often than usual?',
    'Do you get irritated easily?',
    'Do you have trouble concentrating on your academic tasks?',
    'Have you been feeling sadness or low mood?',
    'Do you often feel lonely or isolated?',
    'Do you feel overwhelmed with your academic workload?',
    'Do you lack confidence in your academic performance?',
    'Do you lack confidence in your choice of academic subjects?'
]

stress_numeric = stress_df[stress_cols]

# Dataset 2: StressLevelDataset
mental_cols = [
    'anxiety_level',
    'self_esteem',
    'mental_health_history',
    'depression',
    'headache',
    'blood_pressure',
    'sleep_quality',
    'breathing_problem',
    'noise_level',
    'living_conditions',
    'safety',
    'basic_needs',
    'academic_performance',
    'study_load',
    'teacher_student_relationship',
    'future_career_concerns',
    'social_support',
    'peer_pressure',
    'extracurricular_activities',
    'bullying',
    'stress_level'
]

mental_numeric = mental_df[mental_cols]

# Combine datasets if needed (optional)
combined_df = pd.concat([stress_numeric, mental_numeric], axis=1)

# Compute correlation matrix
corr_matrix = combined_df.corr()

# Plot heatmap
plt.figure(figsize=(15,12))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
plt.title("Correlation Heatmap of Stress and Mental Health Variables")
plt.show()