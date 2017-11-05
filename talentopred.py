from sklearn.neural_network import MLPClassifier
from sklearn import datasets
X, Y = datasets.make_classification(n_samples=200,n_features=7,n_informative=2,n_classes=3,n_clusters_per_class=1)

clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                    hidden_layer_sizes=(5, 2), random_state=1)
clf.fit(X, Y)
result = clf.predict([[0,0.7,0.5,0.7,0.7,0.2,0.4]])
print(result)