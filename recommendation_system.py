import pandas as pd

# Load customer data
data = pd.read_csv("customer_data.csv")

# Products available in the store
products = {
    "Clothing": [
        "Casual T-Shirt",
        "Denim Jeans",
        "Summer Dress"
    ],
    "Electronics": [
        "Wireless Earphones",
        "Smart Watch",
        "Bluetooth Speaker"
    ],
    "Beauty": [
        "Face Wash",
        "Body Lotion",
        "Lip Balm"
    ],
    "Home": [
        "Table Lamp",
        "Cushion Set",
        "Storage Box"
    ],
    "Sports": [
        "Yoga Mat",
        "Water Bottle",
        "Sports Shoes"
    ]
}

# Ask for customer ID
customer_id = input("Enter Customer ID (example: C001): ").upper()

# Find the customer
customer = data[data["CustomerID"] == customer_id]

if customer.empty:
    print("Customer not found.")
else:
    category = customer.iloc[0]["FavoriteCategory"]

    print("\nCustomer:", customer_id)
    print("Favorite Category:", category)

    print("\nRecommended Products:")
    for product in products[category]:
        print("-", product)
