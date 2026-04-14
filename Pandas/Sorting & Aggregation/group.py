import pandas as pd

data = {
    "name" : ["Shahzaib" , "Ali", "Amna" ,"Zain"],
    "age": [26,30,26,31],
    "Salary":[20000,30000,40000,22000]
 
    }

df = pd.DataFrame(data)
grp = df.groupby("age")["Salary"].sum()
print(grp)
# max,min,sum,std