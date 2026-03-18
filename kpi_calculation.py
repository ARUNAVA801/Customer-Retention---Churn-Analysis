import pandas as pd
import matplotlib.pyplot as plt
import Churn

total_customers = Churn.df['customerID'].nunique()
churn_count = (Churn.df['Churn'] == 'Yes').sum()
churn_rate = (churn_count / total_customers) * 100

print("="*50)

#churn analysis kpi report
print("CHURN ANALYSIS KPI REPORT")
print("="*50)
#total customers, churned customers, churn rate
print(f"Total Customers: {total_customers}")
print(f"Churned Customers: {churn_count}")
print(f"Churn Rate: {churn_rate:.2f}%")
print("="*50)

#retention rate
retention_rate = 100 - churn_rate
print(f"Retention Rate: {retention_rate:.2f}%")

#Average Monthly Spend, Average Tenure, CLV
avg_tenure = Churn.df['tenure'].mean()
print(f"Average Lifetime: {avg_tenure:.2f} months")

avg_monthly_spend = Churn.df['MonthlyCharges'].mean()
print(f"Average Monthly Spend: ${avg_monthly_spend:.2f}")

clv = avg_monthly_spend * avg_tenure
print(f"Average CLV: ${clv:.2f}")

