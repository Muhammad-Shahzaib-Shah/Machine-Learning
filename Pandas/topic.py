import pandas as pd

data = {
    "name" : ["Shahzaib" , "Ali", "Amna" ,"Zain"],
    "age": [28,30,26,31],
    "Salary":[20000,30000,40000,22000]
 
    }

df = pd.DataFrame(data)

print(df.shape)
print(df.columns)
