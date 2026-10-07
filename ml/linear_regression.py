from sklearn.linear_model import LinearRegression

X = [[1],[2],[3],[4],[5]]
y = [40,50,60,70,80]

model = LinearRegression()
model.fit(X , y)
hours = int(input("Enter how many hours you study: "))
predicted_score = model.predict([[hours]])[0]
print(f"Based on your hours your score is {predicted_score}") 