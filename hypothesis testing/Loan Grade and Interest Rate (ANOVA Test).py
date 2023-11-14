import pandas as pd
from scipy.stats import f_oneway

# Load the dataset
# Replace 'your_dataset.csv' with the actual file path or URL of your dataset
file_path = r"C:\Users\TAPESH\Downloads\Copy of credit_risk_dataset (1).csv"
df = pd.read_csv(file_path)

# Group data by loan grade
loan_grade_groups = df.groupby('loan_grade')['loan_int_rate']

# Perform ANOVA test
f_statistic, p_value = f_oneway(*[group for name, group in loan_grade_groups])

# Print results
print(f'F-statistic: {f_statistic}')
print(f'P-value: {p_value}')

# Interpret the results
alpha = 0.05
if p_value < alpha:
    print('Reject the null hypothesis: There is a significant difference in interest rates between loan grades.')
else:
    print('Fail to reject the null hypothesis: No significant difference in interest rates between loan grades.')
