import pandas as pd
from scipy.stats import chi2_contingency
file_path = r"C:\Users\TAPESH\Downloads\Copy of credit_risk_dataset (1).csv"
df = pd.read_csv(file_path)

# Create a contingency table
contingency_table = pd.crosstab(df['loan_status'], df['person_emp_length'])

# Perform Chi-square test
chi2_stat, p_value, _, _ = chi2_contingency(contingency_table)

# Print results
print(f'Chi-square statistic: {chi2_stat}')
print(f'P-value: {p_value}')

# Interpret the results
alpha = 0.05
if p_value < alpha:
    print('Reject the null hypothesis: There is a significant difference in loan approval rates based on employment length.')
else:
    print('Fail to reject the null hypothesis: No significant difference in loan approval rates based on employment length.')
