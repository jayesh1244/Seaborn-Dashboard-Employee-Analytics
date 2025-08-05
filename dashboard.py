import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('employee_data.csv')

# Load the dataset
df = pd.read_csv('employee_data.csv')

# 👀 Step 1: Basic Overview
print(df.head())
print(df.info())
print(df.describe())

# 👤 Step 2: Pairplot – Experience vs Performance
sns.pairplot(df, vars=["Experience", "PerformanceScore"], hue="Department")
plt.title("Experience vs Performance Score by Department")
plt.show()

# 💰 Step 3: Boxplot – Salary by Department
plt.figure(figsize=(10, 6))
sns.boxplot(x="Department", y="Salary", data=df)
plt.title("Salary Distribution by Department")
plt.xticks(rotation=45)
plt.show()

# 🚹🚺 Step 4: Countplot – Attrition by Gender
sns.countplot(x="Gender", hue="Attrition", data=df)
plt.title("Attrition Rate by Gender")
plt.show()

# 📊 Step 5: Correlation Heatmap (optional but valuable)
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()
plt.savefig("salary_by_department.png")  # before plt.show()
sns.countplot(x="Department", hue="Attrition", data=df)
plt.title("Attrition by Department")
plt.xticks(rotation=45)
plt.show()
sns.barplot(x="Gender", y="Salary", data=df)
plt.title("Average Salary by Gender")
plt.show()

