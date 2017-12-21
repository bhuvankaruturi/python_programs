from sklearn import tree

X = [[180,80,44],[177,70,43],[160,60,38],[154,54,37],
     [166,65,40], [190,90,47], [175,64,39], [177,70,40],
     [159,55,39], [171,75,42], [181,85,43]]

Y = ['male', 'female', 'female', 'female', 'male', 'male',
     'male', 'female', 'male', 'female', 'male']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(X, Y)

prediction = clf.predict([[181,85,43]])

print(prediction[0])
