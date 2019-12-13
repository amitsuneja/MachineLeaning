import numpy as np



# def decision_boundary(predicted_y):
#     return 1 if prob >= .5 else 0


def classify(predicted_y):
    decision_boundary = np.vectorize(decision_boundary)
    return decision_boundary(predicted_y).flatten()


class = classify(predicted_y)