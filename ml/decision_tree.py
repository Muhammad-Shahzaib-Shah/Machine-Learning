from sklearn.tree import DecisionTreeClassifier

X = [
    [7,2],# size, shade of color
    [8,3],
    [9,7],
    [10,9]
]
y =[0,0,1,1] # apple = 0 , orange =1
model = DecisionTreeClassifier()
model.fit(X , y)

size = float(input("Enter size of fruit in cm: "))
shade = float(input("Enter shade of fruit (0-9) "))
result = model.predict([[size,shade]])[0]


if result == 1:
    print("It's likely an orange")

else:
    print("It's likely an apple")
