import pandas as pd

data = {
    "name" : ["Shahzaib" , "Ali", "Amna" ,"Zain", "Mubarrah", "Hania", "Mehreen"],
    "age": [28,30,26,31,21,24,22],
    "Salary":[20000,30000,40000,22000,28000,41000,50000],
    "Performance":[85,78,90,87,88,80,99]
 
    }
df = pd.DataFrame(data)

df["Salary"]=df["Salary"]*1.5
print(df) 