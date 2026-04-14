import pandas as pd 

data ={
    "Name" : ['Shahzaib', 'Yasir', 'Umer'],
    "City" : ['Karachi', 'Lahore', 'Islamabad'],
    "Age": [20,20,23]
}
df = pd.DataFrame(data)
print(df)
df.to_csv("output.csv", index=False)
df.to_excel("output.xlsx", index=False)
df.to_json("output.json", index=False)