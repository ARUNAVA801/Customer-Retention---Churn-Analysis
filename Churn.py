# Retention by Tenure

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:\\Users\\ASUS\\Downloads\\archive (4)\\WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Create tenure groups
df['Tenure_Group'] = pd.cut(df['tenure'], bins=[0, 12, 24, 36, 48, 72], labels=['0-12', '12-24', '24-36', '36-48', '48+'])

# Create retention flag (1 for retained, 0 for churned)
df['Retained'] = (df['Churn'] == 'No').astype(int)

# Calculate retention rate per tenure group
retention_rate = df.groupby('Tenure_Group', observed=True)['Retained'].mean().to_frame()

# Reshape for heatmap (1D to 2D - just for visualization)
retention_matrix = retention_rate.T  # Transpose to make it 1 row

# Visualization
if __name__ == '__main__':
    plt.figure(figsize=(10, 2))
    sns.heatmap(retention_matrix, annot=True, fmt=".1%", cmap="Greens", 
                cbar_kws={'label': 'Retention Rate'})
    plt.title("Customer Retention Rate by Tenure Group")
    plt.ylabel("")
    plt.tight_layout()
    plt.show()
    
    print("\n📈 Retention Rates by Tenure:")
    print("="*40)
    print(retention_rate)
