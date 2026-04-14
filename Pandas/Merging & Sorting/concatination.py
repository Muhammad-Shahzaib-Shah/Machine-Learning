import pandas as pd

df_reg1 = pd.DataFrame({
    'CustID':[1,2,3],
    'Name':['Shahzaib','Jahanzeb','khanzeb']
})
df_reg2 = pd.DataFrame({
    'CustID':[4,5],
    'Name':['Ali', 'Bilal']
})
df_conacat= pd.concat([df_reg1,df_reg2],axis=1, ignore_index=True)
print(df_conacat)