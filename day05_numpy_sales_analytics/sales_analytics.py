import numpy as np

print("\n===== SALES ANALYTICS SYSTEM =====\n")

# Input dimensions
days = int(input("Enter number of days: "))
products = int(input("Enter number of products: "))
regions = int(input("Enter number of regions: "))

# Input prices
prices = []
print("\nEnter price for each product:")
for i in range(products):
    p = float(input(f"Price of Product {i+1}: "))
    prices.append(p)

prices = np.array(prices)

# Input sales data
sales = np.zeros((days, products, regions))

print("\nEnter sales data (units sold):")

for d in range(days):
    print(f"\nDay {d+1}:")
    for p in range(products):
        for r in range(regions):
            sales[d][p][r] = float(input(f"Product {p+1}, Region {r+1}: "))

# Calculations

# Total units per product
total_units = np.sum(sales, axis=(0, 2))

# Revenue per product
revenue_per_product = total_units * prices

# Total revenue
total_revenue = np.sum(revenue_per_product)

# Daily revenue
daily_revenue = np.sum(sales * prices.reshape(1, -1, 1), axis=(1, 2))

# Region-wise sales
region_sales = np.sum(sales, axis=(0, 1))

# Bests
best_product = np.argmax(total_units) + 1
best_region = np.argmax(region_sales) + 1
best_day = np.argmax(daily_revenue) + 1

# Low performing products
avg_units = np.mean(total_units)
low_products = np.where(total_units < avg_units)[0] + 1

# Output
print("\n===== SALES REPORT =====\n")

print("Total Units Sold (per product):", total_units)
print("Revenue per Product:", revenue_per_product)
print("Total Revenue:", total_revenue)

print("\nDaily Revenue:", daily_revenue)
print("Region-wise Sales:", region_sales)

print(f"\nBest Selling Product: Product {best_product}")
print(f"Best Region: Region {best_region}")
print(f"Best Revenue Day: Day {best_day}")

print("\nLow Performing Products:", low_products)
