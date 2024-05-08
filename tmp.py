import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

# Load data tables
table1 = pd.read_csv('./code_and_data/data/excel/table_1a.csv')
table3 = pd.read_csv('./code_and_data/data/excel/table_3.csv') 
table4a = pd.read_csv('./code_and_data/data/excel/table_4a.csv')
table4b = pd.read_csv('./code_and_data/data/excel/table_4b.csv')

# Analysis using Table 1
plt.figure()
table1.groupby('par_stateabbrv')[['inventor', 'top5cit']].mean().plot.bar()
plt.title('Innovation Rates by State')

plt.figure()
table1[['inventor_g_m', 'inventor_g_f']].mean().plot.bar()
plt.title('Innovation Rates by Gender')

plt.figure()
table1[['inventor_pq_1', 'inventor_pq_2', 'inventor_pq_3', 'inventor_pq_4', 'inventor_pq_5']].mean().plot.bar()
plt.title('Innovation Rates by Parental Income Quintile')

# Analysis using Table 3
plt.figure()
table3.groupby('instnm')[['inventor', 'top5cit']].mean().plot.bar(figsize=(10,5))
plt.title('Innovation Rates by College')

plt.figure()
table3[['inventor_pq1', 'inventor_pq2', 'inventor_pq3', 'inventor_pq4', 'inventor_pq5']].mean().plot.bar()
plt.title('Innovation Rates by Parental Income Quintile (College)')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set matplotlib parameters for prettier charts
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 14
sns.set_style("whitegrid")

# Extract data by gender from Table 1a
gender_data = table1[['inventor_g_m', 'inventor_g_f', 'top5cit_g_m', 'top5cit_g_f']]
gender_data = gender_data.rename(columns={'inventor_g_m': 'inventor_male', 'inventor_g_f': 'inventor_female',
                                          'top5cit_g_m': 'top5cit_male', 'top5cit_g_f': 'top5cit_female'})

# Calculate summary statistics for innovation rates by gender
gender_summary = gender_data.describe()
print("Summary Statistics for Innovation Rates by Gender:")
print(gender_summary)

# Visualize innovation rates by gender
gender_data.plot(kind='bar', rot=0)
plt.title('Innovation Rates by Gender')
plt.xlabel('Gender')
plt.ylabel('Rate')
plt.show()

# Extract data by parent income quintile from Table 1a
income_data = table1[[col for col in table1.columns if col.startswith('inventor_pq_') or col.startswith('top5cit_pq_')]]

# Calculate summary statistics for innovation rates by parent income quintile
income_summary = income_data.describe()
print("\nSummary Statistics for Innovation Rates by Parent Income Quintile:")
print(income_summary)

# Visualize innovation rates by parent income quintile
income_data.plot(kind='bar', rot=0)
plt.title('Innovation Rates by Parent Income Quintile')
plt.xlabel('Parent Income Quintile')
plt.ylabel('Rate')
plt.show()