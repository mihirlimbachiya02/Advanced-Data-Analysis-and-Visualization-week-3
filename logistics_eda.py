logistics_eda.py

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# 1. Simulate Logistics Dataset
np.random.seed(42)
n_samples = 1500

data = {
    "shipment_id": [f"LOG_{i:04d}" for i in range(n_samples)],
    "distance_km": np.random.uniform(2.0, 35.0, n_samples),
    "package_weight_kg": np.random.exponential(scale=4.0, size=n_samples),
    "traffic_density_index": np.random.randint(1, 10, size=n_samples),
}
df = pd.DataFrame(data)

# Simulate dependent target metrics
df["transit_time_mins"] = (
    10
    + (df["distance_km"] * 1.2)
    + (df["traffic_density_index"] * 2.5)
    + np.random.normal(0, 3, n_samples)
)
df["transportation_cost_inr"] = (
    150 + (df["distance_km"] * 18) + (df["package_weight_kg"] * 25)
)
df["delivery_status"] = np.where(
    df["transit_time_mins"] > 50, "Delayed", "On-Time"
)

# 2. Exploratory Data Analysis & Statistical Summaries
print("--- Summary Statistics ---")
print(
    df[["distance_km", "transit_time_mins", "transportation_cost_inr"]].describe()
)

# 3. Generating Visualizations using Matplotlib & Seaborn
plt.figure(figsize=(14, 10))

# Plot 1: Transit Time Distribution (Histogram & KDE)
plt.subplot(2, 2, 1)
sns.histplot(
    df["transit_time_mins"], kde=True, color="teal", bins=30
).set_title("Distribution of Delivery Transit Times")
plt.xlabel("Transit Time (mins)")
plt.ylabel("Frequency")

# Plot 2: Cost vs Distance Scatter Plot
plt.subplot(2, 2, 2)
sns.scatterplot(
    data=df,
    x="distance_km",
    y="transportation_cost_inr",
    hue="delivery_status",
    palette={"On-Time": "green", "Delayed": "red"},
    alpha=0.7,
).set_title("Transportation Cost vs. Distance")
plt.xlabel("Distance (km)")
plt.ylabel("Cost (INR)")

# Plot 3: Correlation Heatmap
plt.subplot(2, 2, 3)
numeric_cols = [
    "distance_km",
    "package_weight_kg",
    "traffic_density_index",
    "transit_time_mins",
    "transportation_cost_inr",
]
sns.heatmap(
    df[numeric_cols].corr(), annot=True, cmap="coolwarm", fmt=".2f", cbar=True
).set_title("Feature Correlation Heatmap")

# Plot 4: Traffic Density impact on Status (Box Plot)
plt.subplot(2, 2, 4)
sns.boxplot(
    data=df, x="delivery_status", y="traffic_density_index", palette="Set2"
).set_title("Traffic Density Index by Delivery Status")
plt.xlabel("Delivery Status")
plt.ylabel("Traffic Density Index (1-10)")

plt.tight_layout()
plt.savefig("logistics_eda_visualizations.png", dpi=300)
print(
    "\nVisualizations successfully generated and saved as 'logistics_eda_visualizations.png'."
)
