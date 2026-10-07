import pandas as pd

df = pd.DataFrame({
    "Color": ["Red", "Blue", "Green", "Red"]
})

df_encoded = pd.get_dummies(df, columns=["Color"], dtype=int)
print("Column order:", df_encoded.columns.tolist())
print("Array:")
print(df_encoded.to_numpy())