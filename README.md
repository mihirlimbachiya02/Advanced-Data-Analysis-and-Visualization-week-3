# Advanced-Data-Analysis-and-Visualization-week-3

1. INTRODUCTION & DATASET STRUCTURE
- Objective: To perform an in-depth Exploratory Data Analysis (EDA) and generate insightful visualizations using Python to uncover operational bottlenecks, cost drivers, and performance trends in logistics.
- Dataset Structure: A simulated logistics and supply chain dataset comprising 1,500 records across key variables: shipment_id, distance_km, package_weight_kg, transit_time_mins, transportation_cost_inr, traffic_density_index, and delivery_status (On-Time vs. Delayed).

2. EXPLORATORY DATA ANALYSIS (EDA) & STATISTICAL METRICS
- Central Tendencies & Distributions: Statistical summaries reveal that average transit time is 38.4 minutes with a standard deviation of 11.2 minutes. Average transportation cost scales linearly with distance, averaging INR 450 per shipment.
- Correlation Analysis: A strong positive correlation (r = 0.82) exists between traffic density index and transit duration, identifying traffic congestion as a primary operational bottleneck. Package weight shows a moderate correlation with transportation cost (r = 0.54).

3. VISUALIZATION METHODOLOGY & JUSTIFICATION
To translate raw metrics into strategic decisions, four visualizations are implemented:
- Histogram / KDE Plot: Illustrates the distribution of delivery transit times, helping managers identify skewness and frequency of tail-end delays.
- Scatter Plot with Regression Line: Maps transportation cost against shipment distance to highlight cost inefficiencies and pricing outliers.
- Correlation Heatmap: Displays numeric feature correlations to isolate key cost drivers (e.g., weight vs. distance).
- Box Plot: Compares traffic density distributions across On-Time versus Delayed shipment categories.

4. ANALYTICAL INSIGHTS & STRATEGIC RECOMMENDATIONS
- Bottleneck Identification: Visualizations confirm that high traffic density indexes (>= 7) are the core driver of delivery delays, shifting shipments past the 50-minute threshold.
- Cost Optimization: Cost-to-distance regression shows scaling inefficiencies on specific regional corridors, indicating a need for dynamic multi-stop route consolidation.
- Recommendations: Implement real-time traffic-aware dynamic rerouting during peak congestion windows to protect On-Time Delivery Rates (OTDR) and control operational expenses.
