from sklearn.neighbors import KNeighborsClassifier 

X = [
    [180 ,7],
    [200,7.5],
    [250,8],
    [300,8.5],
    [330,9],
    [360,9.5], 
]
y = [0,0,0,1,1,1]

model = KNeighborsClassifier(n_neighbors = 3)
model.fit(X,y)
weight = float(input("Enter weight in gms: "))
size = float(input("Enter size in cms: "))

result = model.predict([[weight, size]])[0]

if result == 1:
    print("It's likely an orange")

else:
    print("It's likely an apple")
