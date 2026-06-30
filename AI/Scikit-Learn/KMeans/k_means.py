# 1. Import Required Libraries
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

# 2. Prepare the Data (12 Customers with Income and Spending Score)
#    Income is in Rupees, Spending Score is from 0 to 100
X = np.array([
    [12000, 15],  # Customer 1
    [15000, 20],  # Customer 2
    [10000, 10],  # Customer 3
    [90000, 95],  # Customer 4
    [100000, 90], # Customer 5
    [85000, 88],  # Customer 6
    [50000, 50],  # Customer 7
    [55000, 55],  # Customer 8
    [48000, 45],  # Customer 9
    [95000, 20],  # Customer 10
    [88000, 15],  # Customer 11
    [92000, 25],   # Customer 12
    [36000, 99]   # Customer 12
])

# 3. Create the KMeans Model (K=4 because we want 4 types of customers)
#    random_state=42 ensures we get the same result every time
model = KMeans(n_clusters=4, random_state=42)
model.fit(X)

# 5. Based on the centers above, create a Dictionary (Map) to convert numeric labels to text
segment_names = {
    0: "Saver (Rich but tight-fisted)",
    1: "Economy (Low Income, Low Spend)",
    2: "High Roller (Rich and spends a lot)",
    3: "Average (Middle)"
}

# 6. Convert the Numeric Labels to Text Labels
numeric_labels = model.labels_
text_labels = [segment_names[i] for i in numeric_labels]

# 7. Display the Final Result in a DataFrame
df = pd.DataFrame(X, columns=["Annual Income (Rs.)", "Spending Score"])
df["Cluster_Number"] = numeric_labels
df["Segment Name"] = text_labels

print("\n=== FINAL CUSTOMER SEGMENTATION ===")
print(df)