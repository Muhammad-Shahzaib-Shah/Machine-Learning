import pandas as pd

data = {
    "name" : ["Shahzaib" , "Ali", "Amna" ,"Zain"],
    "age": [28,30,26,31],
    "Salary":[20000,30000,40000,22000]
 
    }

df= pd.DataFrame(data)
# df.sort_values(by="age", ascending=True,inplace=True)
df.sort_values(by=["age","Salary"], ascending=[True,True],inplace=True)
print(df)