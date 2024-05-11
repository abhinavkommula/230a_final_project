import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from Table 1a and Table 1b
table1a = pd.read_csv('./code_and_data/data/excel/table_1a.csv')
table1b = pd.read_csv('./code_and_data/data/excel/table_1b.csv')

# Experiment with Table 1a (Commuting Zones)
# Extract relevant columns
table1a_low_income = table1a[['par_czname', 'inventor_pq_1', 'top5cit_pq_1']]

# Bar chart for inventor_pq_1 by commuting zone
plt.figure(figsize=(12, 6))
table1a_low_income.sort_values(by='inventor_pq_1', ascending=False, inplace=True)
sns.barplot(x='par_czname', y='inventor_pq_1', data=table1a_low_income.head(20))
plt.xticks(rotation=90)
plt.title('Top 20 Commuting Zones by Share of Inventors among Low-Income Children')
plt.tight_layout()
plt.show()

# Bar chart for top5cit_pq_1 by commuting zone
plt.figure(figsize=(12, 6))
table1a_low_income.sort_values(by='top5cit_pq_1', ascending=False, inplace=True)
sns.barplot(x='par_czname', y='top5cit_pq_1', data=table1a_low_income.head(20))
plt.xticks(rotation=90)
plt.title('Top 20 Commuting Zones by Share of Top 5% Cited Inventors among Low-Income Children')
plt.tight_layout()
plt.show()

# Experiment with Table 1b (States)
# Extract relevant columns
table1b_low_income = table1b[['par_stateabbrv', 'inventor_pq_1', 'top5cit_pq_1']]

# Bar chart for inventor_pq_1 by state
plt.figure(figsize=(8, 6))
table1b_low_income.sort_values(by='inventor_pq_1', ascending=False, inplace=True)
sns.barplot(x='par_stateabbrv', y='inventor_pq_1', data=table1b_low_income)
plt.xticks(rotation=90)
plt.title('Share of Inventors among Low-Income Children by State')
plt.tight_layout()
plt.show()

# Bar chart for top5cit_pq_1 by state
plt.figure(figsize=(8, 6))
table1b_low_income.sort_values(by='top5cit_pq_1', ascending=False, inplace=True)
sns.barplot(x='par_stateabbrv', y='top5cit_pq_1', data=table1b_low_income)
plt.xticks(rotation=90)
plt.title('Share of Top 5% Cited Inventors among Low-Income Children by State')
plt.tight_layout()
plt.show()