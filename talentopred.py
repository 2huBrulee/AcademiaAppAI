from sklearn.neural_network import MLPClassifier
from sklearn import datasets
from flask_api import FlaskAPI

app = FlaskAPI(__name__)

@app.route('/gg/', methods=['GET','POST'])
def index():

    result = clf.predict([[1,0.2,0.3,0.4,0.5,0.6,1]])
    rp = int(result[0])
    return {'prediccion':rp}

if __name__ == "__main__":
    X, Y = datasets.make_classification(n_samples=200, n_features=7, n_informative=2, n_classes=3,
                                        n_clusters_per_class=1)
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                        hidden_layer_sizes=(5, 2), random_state=1)
    clf.fit(X, Y)
    app.run()
