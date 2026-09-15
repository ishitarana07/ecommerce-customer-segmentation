import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load customer data
data = pd.read_csv("customer_data.csv")

print("Customer Data:")
print(data)

# Select information useful for segmentation
features = data[
    ["TotalPurchases", "TotalSpent", "LastPurchaseDays"]
]

# Scale the data
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Create customer groups
model = KMeans(n_clusters=3, random_state=42, n_init=10)
data["CustomerGroup"] = model.fit_predict(scaled_features)

# Display the result
print("\nCustomer Segmentation:")
print(
    data[
        ["CustomerID", "TotalPurchases", "TotalSpent",
         "LastPurchaseDays", "CustomerGroup"]
    ]
)

# Show average values for each group
summary = data.groupby("CustomerGroup")[
    ["TotalPurchases", "TotalSpent", "LastPurchaseDays"]
].mean()

print("\nGroup Summary:")
print(summary)

# Create a simple graph
plt.figure(figsize=(8, 5))
plt.scatter(
    data["TotalPurchases"],
    data["TotalSpent"],
    c=data["CustomerGroup"]
)

plt.xlabel("Total Purchases")
plt.ylabel("Total Spent")
plt.title("Customer Segmentation")
plt.show()
