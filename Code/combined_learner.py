# Author: Robert Patrick
#
# This script contains the code for a wrapper class that contains multiple
# learners, using all of them together to make classifications.


from collections import defaultdict
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier


class CombinerLearner:

    # Class variables
    # --------------------
    self.mnb_clf
    self.knn_clf_k2
    self.knn_clf_k3
    self.knn_clf_k5

    # Constructor
    # --------------------
    # Takes in the intial training data, and trains the contained learners
    # Xtr: Should be 2d-array N x P, with N=data & P=features
    # Ytr: Should be array of classes
    def __init__(Xtr: list, Ytr: list):
        self.mnb_clf = MultinomialNB()
        self.mnb_clf.fit(Xtr, Ytr)

        self.knn_clf_k2 = KNeighborsClassifier(n_neighbors=2, algorithm='auto')
        self.knn_clf_k2.fit(Xtr, Ytr)
        
        self.knn_clf_k3 = KNeighborsClassifier(n_neighbors=3, algorithm='auto')
        self.knn_clf_k3.fit(Xtr, Ytr)

        self.knn_clf_k5 = KNeighborsClassifier(n_neighbors=5, algorithm='auto')
        self.knn_clf_k5.fit(Xtr, Ytr)


    # Public methods
    # --------------------
    # Takes in test data with its classifications, makes the predictions, and uses
    # these to calculate and return the mean-squared-error.
    def mse(Xte: list, Yte: list) -> float:
        pass

    # Makes predictions given some test data, returning a list of the predictions
    def predict(Xte: list) -> list:
        mnb = self.mnb_clf.predict(Xte)
        knn2 = self.knn_clf_k2.predict(Xte)
        knn3 = self.knn_clf_k3.predict(Xte)
        knn5 = self.knn_clf_k5.predict(Xte)

        predictions = []

        for i in range(length(mnb)):
            prediction = [mnb[i],knn2[i],knn3[i],knn5[i]]
            predictions.append(max(set(prediction), key=prediction.count))

        return predictions
