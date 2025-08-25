
import pandas as pd
import matplotlib.pyplot as plt
# Load Excel file
df = pd.read_excel('/Users/chiara/ChiaraTarenghi/edge_health/Cardiovascular_health_indicators_2021_Technical_Exercise_ (2).xlsx')

# Display the first few rows of the data

print(df.head()
print(df.columns)
      
# Calculate combined mortality rates for heart disease and stroke (adjust column names based on your dataset)
df['population_total'] = df['Population in Area (under 75yrs)'] + df['Population in Area (75yrs and above)']
df['stroke_total'] = df['Number of stroke mortalities (under 75 yrs)'] + df['Number of stroke mortalities (75 yrs and above)'] + df[  'Number of stroke patients whose last lood pressure reading was under 140/90 mmHg (under 80 yrs)']  + df[ 'Number of stroke patients where an anti-platelet agent or an anti-coagulant was taken (all ages)']
df['heart_diseases_total'] = df['Number of  Heart Disease mortalities (under 75 yrs)'] + df['Number of  Heart Disease mortalities (over 75 yrs)']
df['combined_mortality'] = df['stroke_total'] + df['heart_diseases_total']

# Group by Clinical Commissioning Group (CCG) and sum mortality rates across ages
ccg_mortality = df.groupby('CCG Name')['combined_mortality'].sum().reset_index()
print(ccg_mortality)
      
# Sort by mortality rate and select top 5
top_5_ccgs = ccg_mortality.sort_values(by='combined_mortality', ascending=False).head(5)

# Create bar chart
plt.figure(figsize=(10, 6))
plt.bar(top_5_ccgs['CCG Name'], top_5_ccgs['combined_mortality'], color='blue')
plt.title('Top 5 CCGs with Highest Mortality Rates from Heart Disease and Stroke (2021)')
plt.xlabel('Clinical Commissioning Group (CCG)')
plt.ylabel('Combined Mortality Rate')
plt.xticks(rotation=45)
plt.tight_layout()

# Add source label
plt.figtext(0.5, -0.1, 'Source: Department of Health and Social Care, 2021', ha='center', fontsize=10)

# Save the chart
plt.savefig('top_5_ccgs_mortality.png')

# Show chart
plt.show()
