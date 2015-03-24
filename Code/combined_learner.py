# Author: Robert Patrick
#
# This script contains the code for a wrapper class that contains multiple
# learners, using all of them together to make classifications.


from collections import defaultdict
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier


class CombinedLearner:

    # Class variables
    # --------------------
    # self.mnb_clf
    # self.knn_clf_k2
    # self.knn_clf_k3


    # Constructor
    # --------------------
    # Takes in the intial training data, and trains the contained learners
    # Xtr: Should be 2d-array N x P, with N=data & P=features
    # Ytr: Should be array of classes
    def __init__(self, Xtr: list, Ytr: list):
        self.mnb_clf = MultinomialNB()
        self.mnb_clf.fit(Xtr, Ytr)

        self.knn_clf_k2 = KNeighborsClassifier(n_neighbors=2, algorithm='auto')
        self.knn_clf_k2.fit(Xtr, Ytr)
        
        self.knn_clf_k3 = KNeighborsClassifier(n_neighbors=3, algorithm='auto')
        self.knn_clf_k3.fit(Xtr, Ytr)


    # Public methods
    # --------------------
    # Takes in test data with its classifications, makes the predictions, and uses
    # these to calculate and return the mean-squared-error.
    # NOTE: THIS FUNCTION WILL NOT WORK (WILL CAUSE CRASH) WITH NON-NUMBER CLASSES
    def mse(self, Xte: list, Yte: list) -> float:
        predictions = self.predict(Xte)

        errors = []
        for i in range(len(Yte)):
            errors.append((predictions[i]-Yte[i])**2)

        return sum(errors)/len(errors)

    # Makes predictions given some test data, returning a list of the predictions
    def predict(self, Xte: list) -> list:
        mnb = self.mnb_clf.predict(Xte)
        knn2 = self.knn_clf_k2.predict(Xte)
        knn3 = self.knn_clf_k3.predict(Xte)

        predictions = []

        for i in range(len(mnb)):
            prediction = [mnb[i],knn2[i],knn3[i]]
            print([mnb[i],knn2[i],knn3[i]])
            predictions.append(max(set(prediction), key=prediction.count))

        return predictions
