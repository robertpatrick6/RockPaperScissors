from combined_learner import CombinedLearner

Xtr = [[0,0,0],
       [0,0,1],
       [0,1,0],
       [0,1,1],
       [1,0,0],
       [1,0,1],
       [1,1,0],
       [1,1,1]]

Ytr = [0,1,0,1,1,0,1,0]

cmb_lrn = CombinedLearner(Xtr,Ytr)

Xte = [[1,1,1],
       [0,1,0],
       [0,1,1],
       [1,0,0],
       [0,0,0],
       [1,0,1]]

Yte = [0,0,1,1,0,0]

print(cmb_lrn.predict(Xte))

print(cmb_lrn.mse(Xte,Yte))
