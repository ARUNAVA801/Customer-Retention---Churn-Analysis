

from matplotlib.dates import MONTHLY
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("C:\\Users\\ASUS\\Downloads\\archive (4)\\WA_Fn-UseC_-Telco-Customer-Churn.csv")
import seaborn as sns
# 1. Churn by Subscription Type
# Convert churn labels to numeric (Yes=1, No=0) so we can average them
churn_by_plan = (
    df
    .groupby('Contract')['Churn']
    .apply(lambda s: s.map({'Yes': 1, 'No': 0}).mean())
)

# Save the chart to a file so it is visible even if display is not available
import os

output_dir = os.path.join(os.path.dirname(__file__), 'output')
os.makedirs(output_dir, exist_ok=True)

chart_path = os.path.join(output_dir, 'churn_by_subscription_type.png')

ax = churn_by_plan.plot(kind='bar')
ax.set_title("Churn Rate by Subscription Type")
ax.set_ylabel("Churn Rate")
ax.set_ylim(0, 1)
fig = ax.get_figure()
fig.tight_layout()
fig.savefig(chart_path)

print(f"Chart saved to: {chart_path}")



#RETENTION ANALYSIS

# Tenure Cohort based Retention
# Convert churn to numeric (1=Yes, 0=No) so we can compute mean churn rates.
df['Churn_Flag'] = df['Churn'].map({'Yes': 1, 'No': 0})

# Use pd.qcut directly (not via Churn) to avoid any module alias confusion
df['Tenure_Group'] = pd.qcut(df['tenure'], q=5)

# Retention = 1 - churn rate (mean of churn flag)
retention = 1 - df.groupby('Tenure_Group')['Churn_Flag'].mean()

print(retention)

# contract vs tenure cohort retention

cohort = df.groupby(['Tenure_Group','Contract'])['customerID'].nunique().unstack()

retention = cohort.divide(cohort.sum(axis=1), axis=0)

sns.heatmap(retention, annot=True, fmt=".1%", cmap="coolwarm")
plt.title("Retention by Tenure and Contract")
plt.show()

# # columns vs churn...contract vs churn, monthly charges vs churn, tenure vs churn


monthly_charges_vs_churn = df.groupby('Churn')['MonthlyCharges'].mean()
contract_vs_churn = df.groupby('Churn')['Contract'].value_counts(normalize=True)
print("\nAverage Monthly Charges by Churn Status:")
print(monthly_charges_vs_churn)
print("\nContract Type Distribution by Churn Status:")
print(contract_vs_churn)


# CHURN DRIVERS ANALYSIS

df['Churn_Flag'] = df['Churn'].map({'Yes': 1, 'No': 0})

# df['Contract'] = pd.qcut(df['Contract'], q=5)

Churn_by_contract = df.groupby('Churn')['Contract'].value_counts(normalize=True)
sns.barplot(data=df,x='Contract',y='Churn_Flag')
plt.title("Churn by Contract Type")
plt.show()

# MONTHLY CHARGES VS CHURN
df['Churn_Flag'] = df['Churn'].map({'Yes': 1, 'No': 0})
monthly_charges_vs_churn = df.groupby('Churn')['MonthlyCharges'].mean()
print("\nAverage Monthly Charges by Churn Status:")
print(monthly_charges_vs_churn)
sns.barplot(data=df,x='MonthlyCharges',y='Churn_Flag')
plt.title("Churn by Monthly Charges")
plt.show()


#COHORT STYLE CHURN ANALYSIS
# Tenure AND Contract vs Churn

df['Churn_Flag'] = df['Churn'].map({'Yes': 1, 'No': 0})
df['Tenure_Group'] = pd.qcut(df['tenure'], q=6)
heat = df.groupby(['Tenure_Group','Contract'])['Churn_Flag'].mean().unstack()

sns.heatmap(heat,annot=True, fmt=".0%", cmap="coolwarm")
plt.title("Churn Rate by Tenure and Contract")
plt.show()
