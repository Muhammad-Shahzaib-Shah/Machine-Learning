import pandas as pd

df_cust=pd.DataFrame({
    'CustID':[1,2,3],
    'Name':['Shahzaib','Jahanzeb','khanzeb']
})
df_order=pd.DataFrame({
    'CustID':[1,2,4],
    'OrderAmt':[240,440,444]

})

# df_merged=pd.merge(df_cust,df_order, on="CustID" ,how="inner")
# df_merged=pd.merge(df_cust,df_order, on="CustID" ,how="outer")
# df_merged=pd.merge(df_cust,df_order, on="CustID" ,how="left")
df_merged=pd.merge(df_cust,df_order, on="CustID" ,how="right")
# df_merged=pd.merge(df_cust,df_order, on="CustID" ,how="cross")
print(df_merged)