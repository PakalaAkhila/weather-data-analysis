# weather_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('weather.csv')  # ✅ Your renamed file
print("✅ Dataset loaded successfully!")

# Convert date to proper format and extract only the date
data['Formatted Date'] = pd.to_datetime(data['Formatted Date'], utc=True)
data['Date'] = data['Formatted Date'].dt.date

# Preview the data
print("\n📊 First 5 rows:")
print(data.head())

# Summary statistics
print("\n📈 Summary statistics:")
print(data.describe())

# Check for missing values
print("\n🔍 Missing values in each column:")
print(data.isnull().sum())

# Drop rows with missing values
data.dropna(inplace=True)

# 📆 Temperature trend
plt.figure(figsize=(10, 5))
plt.plot(data['Date'], data['Temperature (C)'], label='Temperature (C)', color='orange')
plt.plot(data['Date'], data['Apparent Temperature (C)'], label='Apparent Temp (C)', color='blue')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('📅 Daily Temperature Trend')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ☔ Precipitation Type Distribution
plt.figure(figsize=(6, 4))
sns.countplot(data['Precip Type'], palette='coolwarm')
plt.title('☁️ Precipitation Type Count')
plt.xlabel('Precipitation Type')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# 💧 Humidity vs Temperature
plt.figure(figsize=(8, 5))
sns.scatterplot(x='Temperature (C)', y='Humidity', hue='Precip Type', data=data, alpha=0.6)
plt.title('Humidity vs Temperature')
plt.tight_layout()
plt.show()

# 🔗 Correlation Heatmap
plt.figure(figsize=(7, 6))
sns.heatmap(data.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('🔗 Feature Correlation Heatmap')
plt.tight_layout()
plt.show()

print("\n✅ Weather data analysis completed.")
