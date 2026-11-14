import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv(r"C:\Users\hdobh\python\project dehradun.py\cleaned project\cleaned_housing.csv")

#1.City Distribution

plt.figure(figsize=(10,6))
sns.countplot(
    y=df['City'],
    order=df['City'].value_counts().index
)
plt.title("Property Listings by City")
plt.savefig("city_distribution.png")
plt.show()

# 2. Property Type Distribution
plt.figure(figsize=(10,6))
sns.countplot(
    y=df['Appartment_type'],
    order=df['Appartment_type'].value_counts().index
)
plt.title("Property Type Distribution")
plt.savefig("property_type_distribution.png")
plt.show()


# 3. Price Distribution
plt.figure(figsize=(10,6))
sns.histplot(df['Price'], bins=20, kde=True)
plt.title("Price Distribution")
plt.savefig("price_distribution.png")
plt.show()

# 4. Area vs Price
plt.figure(figsize=(10,6))
sns.scatterplot(
    data=df,
    x='Area',
    y='Price'
)
plt.title("Area vs Price")
plt.savefig("area_vs_price.png")
plt.show()