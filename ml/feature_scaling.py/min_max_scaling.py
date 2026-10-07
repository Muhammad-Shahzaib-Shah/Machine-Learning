import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Student data
data = {
    "Age": [18, 19, 20, 21, 22, 23, 24, 25, 26, 27],
    "StudyHours": [2, 3, 4, 5, 6, 7, 8, 6, 9, 10],
    "Marks": [45, 50, 55, 60, 65, 70, 75, 72, 85, 90]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# MinMaxScaler
scaler = MinMaxScaler()

# Scale the data
scaled_data = scaler.fit_transform(df)

# Convert back to DataFrame
scaled_df = pd.DataFrame(
    scaled_data,
    columns=df.columns
)

print("\nScaled Data:")
print(scaled_df.round(2))