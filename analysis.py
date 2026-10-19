import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
 
df = pd.read_csv('Ecommerce_Sales.csv')
df['Order_Date'] = pd.to_datetime(df['Order_Date'])
df['Month'] = df['Order_Date'].dt.month_name()
 
month_order = ['January','February','March','April','May','June','July','August','September','October','November','December']
df['Month'] = pd.Categorical(df['Month'], categories=month_order, ordered=True)
 
# 1. Sales by Category
plt.figure(figsize=(8,5))
sns.countplot(data=df, x='Category', palette='viridis')
plt.title('Sales by Category')
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig('01_Sales_by_Catagory.png')
 
# 2. Monthly Sales Trend
monthly = df.groupby('Month', observed=True)['Sales_Amount'].sum().reindex(month_order)
plt.figure(figsize=(10,5))
plt.plot(month_order, monthly.values, marker='o')
plt.title('Monthly Sales Trend (2023)')
plt.tight_layout()
plt.savefig('02_monthly_sales_Trend.png')
 
# 3. Top 5 Products
top_products = df.groupby('Product')['Sales_Amount'].sum().sort_values(ascending=False).head(5)
plt.figure(figsize=(8,5))
sns.barplot(x=top_products.values, y=top_products.index, palette='magma')
plt.title('Top 5 Products by Sales')
plt.tight_layout()
plt.savefig('03_Top_5_Products.png')
