import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\ASUS\Downloads\archive (4)\WA_Fn-UseC_-Telco-Customer-Churn.csv")


# #--KPI's
df['Churn_Flag'] = df['Churn'].map({'Yes':1,'No':0})
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

total_customers = df['customerID'].nunique()
churn_rate = df['Churn_Flag'].mean()*100
retention_rate = 100 - churn_rate
avg_lifetime = df['tenure'].mean()
clv = df['MonthlyCharges'].mean() * avg_lifetime

st.title("Customer Retention Dashboard")

kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)

# col1.metric("Total Customers", total_customers)
# col2.metric("Churn Rate", f"{churn_rate:.2f}%")
# col3.metric("Retention Rate", f"{retention_rate:.2f}%")
# col4.metric("Avg Lifetime (months)", f"{avg_lifetime:.1f}")
# col5.metric("CLV ($)", f"{clv:.2f}")

with kpi1:
    st.metric("Total Customers", total_customers)
with kpi2:
    st.metric("Churn Rate", f"{churn_rate:.2f}%")       
with kpi3:
    st.metric("Retention Rate", f"{retention_rate:.2f}%")
with kpi4:
    st.metric("Avg Lifetime (months)", f"{avg_lifetime:.1f}")
with kpi5:
    st.metric("CLV ($)", f"{clv:.2f}")

# Churn Rate by Contract Type
import seaborn as sns
import matplotlib.pyplot as plt

col1, col2 = st.columns(2)
contract_churn = df.groupby('Contract')['Churn_Flag'].mean().reset_index()

fig1, ax = plt.subplots(figsize=(6,4))
sns.barplot(data=contract_churn, x='Contract', y='Churn_Flag', ax=ax)

ax.set_title("Churn Rate by Contract Type")
ax.set_ylabel("Churn Rate")

with col1:
    st.subheader("Churn Rate by Contract Type")
    st.pyplot(fig1)



# Retention by Tenure

# the lower the tenure group the lower the retention rate

# This shows how retention changes with customer lifetime.
df['Tenure_Group'] = pd.qcut(df['tenure'], q=6)

retention = 1 - df.groupby('Tenure_Group')['Churn_Flag'].mean()

fig2, ax = plt.subplots(figsize=(6,4))

retention.plot(kind='bar', ax=ax)

ax.set_title("Retention Rate by Tenure Group")
ax.set_ylabel("Retention Rate")

with col2:
    st.subheader("Retention Rate by Tenure Group")
    st.pyplot(fig2)

st.header("Key Insights")

st.write("""
1. Month-to-month contracts have the highest churn rate.
2. Customers in the first tenure group churn the most.
3. Higher monthly charges correlate with higher churn.
4. Long-term customers show strong retention.
""")


st.header("Business Recommendations")

st.write("""
• Promote long-term contracts with discounts.
• Improve onboarding for new customers.
• Offer bundled pricing to reduce churn.
• Implement loyalty rewards for long-tenure customers.
""")

# Monthly Charges vs Churn

# This shows whether expensive plans cause churn.

# customer paying higher monthky charges churn more.

col3, col4 = st.columns(2)
fig3, ax = plt.subplots(figsize=(6,4))

df['Churn_Flag'] = df['Churn'].map({'Yes':1,'No':0})
sns.boxplot(data=df, x='Churn_Flag', y='MonthlyCharges', ax=ax)
ax.set_title("Monthly Charges vs Churn")

with col3:
    st.subheader("Monthly Charges vs Churn")
    st.pyplot(fig3)
st.header("Monthly Charges vs Churn Analysis: ")
st.write("""Average Monthly Charges by Churn Status:
No     61.265124
Yes    74.441332
Name: MonthlyCharges, dtype: float64""")
# Tenure Distribution
fig4, ax = plt.subplots(figsize=(6,4))

sns.histplot(df['tenure'], bins=30, ax=ax)

ax.set_title("Customer Tenure Distribution")

with col4:
    st.subheader("Customer Tenure Distribution")
    st.pyplot(fig4)

st.header("Customer Tenure Distribution Analysis: ")

st.write("""You often see, many new customers
few long-term customers""")
         
# Customer Lifetime Value (CLV) Distribution

# most powerful churn analysis, shows the distribution of CLV among customers and how it relates to churn.
#the higher the CLV the lower the churn rate, which means that customers with higher CLV are more likely to stay with the company.

col5 = st.columns(1)[0]


pivot = df.pivot_table(
    values='Churn_Flag',
    index='Tenure_Group',
    columns='Contract',
    aggfunc='mean'
)
fig5, ax = plt.subplots(figsize=(6,4))

with col5:
   st.subheader("Churn Heatmap: Tenure vs Contract")
sns.heatmap(pivot, annot=True, fmt=".2f", cmap="YlGnBu", ax=ax)

ax.set_title("Churn Rate by Tenure Group and Contract Type")


st.pyplot(fig5)

st.header("Churn Heatmap Analysis: Tenure vs Contract and Customer Lifetime Value Distribution")
st.write("""Most powerful churn analysis, 
shows the distribution of CLV among customers 
and how it relates to churn.
the higher the CLV the lower the churn rate, 
which means that customers with higher CLV
 are more likely to stay with the company.""")
