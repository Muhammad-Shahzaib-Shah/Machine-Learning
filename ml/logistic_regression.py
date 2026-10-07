from sklearn.linear_model import LogisticRegression

X = [[1],[2],[3],[4],[5]]
y = [0,0,1,1,1]

model = LogisticRegression()
model.fit(X , y)
hours = float(input("Enter how many hours you study: "))
result = model.predict([[hours]])

if result == 1:
    print("You are likely to Pass")

else:
    print("You are likely to Fail")

