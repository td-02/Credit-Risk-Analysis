from scipy.stats import mannwhitneyu

# Separate data into two groups based on loan status
loan_status_groups = [group['loan_percent_income'] for name, group in df.groupby('loan_status')]

# Perform Mann-Whitney U test
u_stat, p_value = mannwhitneyu(*loan_status_groups)

# Print results
print(f'Mann-Whitney U statistic: {u_stat}')
print(f'P-value: {p_value}')
alpha =0.5
# Interpret the results
if p_value < alpha:
    print('Reject the null hypothesis: There is a significant difference in debt-to-income ratios based on loan status.')
else:
    print('Fail to reject the null hypothesis: No significant difference in debt-to-income ratios based on loan status.')
