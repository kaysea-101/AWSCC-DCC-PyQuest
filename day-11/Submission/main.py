import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt 

df = pd.read_csv('employees.csv') # i replaced the value inside into a relative path

sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.barplot(x='gender', y='salary', data=df, ci=None, palette='pastel')
plt.title('Average Salary by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Salary')
plt.show()

df = pd.read_csv('employees.csv') # i replaced the value inside into a relative path
print(df)