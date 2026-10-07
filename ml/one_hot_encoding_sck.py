from sklearn.preprocessing import OneHotEncoder

# Data
data = [["Red"], ["Blue"], ["Green"], ["Red"]]

# Encoder
encoder = OneHotEncoder(sparse_output=False)

# Encoding
encoded = encoder.fit_transform(data)

print(encoded)

# Categories/column order
# print(encoder.categories_)