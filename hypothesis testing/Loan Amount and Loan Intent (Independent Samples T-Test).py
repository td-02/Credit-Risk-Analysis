from scipy.stats import ttest_ind
import pandas as pd

file_path = r"C:\Users\TAPESH\Downloads\Copy of credit_risk_dataset (1).csv"
df = pd.read_csv(file_path)

# Concatenate loan amounts for different loan intents into a single array
loan_intent_groups = [group['loan_amnt'] for name, group in df.groupby('loan_intent')]
all_loan_amounts = pd.concat(loan_intent_groups)

# Perform independent samples t-test
t_stat, p_value = ttest_ind(all_loan_amounts, df['loan_amnt'])

# Print results
print(f'T-statistic: {t_stat}')
print(f'P-value: {p_value}')

alpha = 0.05
# Interpret the results
if p_value < alpha:
    print('Reject the null hypothesis: There is a significant difference in loan amounts between different loan intents.')
else:
    print('Fail to reject the null hypothesis: No significant difference in loan amounts between different loan intents.')
