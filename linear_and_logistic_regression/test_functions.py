import linear_and_logistic_regression
import numpy
from sklearn import linear_model

NUM_EXAMPLES = 25000
NUM_FEATURES = 100

NUM_TEST = 10

def main():
    features = numpy.random.random((NUM_EXAMPLES, NUM_FEATURES))
    labels = _fake_function(features=features)
    lr = linear_model.LinearRegression()
    lr.fit(X=features, y=labels)
    my_lr = linear_and_logistic_regression.train_model(
        loss_func=linear_and_logistic_regression.linear_loss,
        update_func=linear_and_logistic_regression.get_update_linear,
        features=features,
        labels=labels,
    )
    test_features = numpy.random.random(
        (NUM_TEST, NUM_FEATURES),
    )
    print(lr.predict(test_features))
    print(
        test_features.dot(my_lr['coefficients']) +
        my_lr['intercept'],
    )
    

def _fake_function(features):
    coef_vector = numpy.random.random(NUM_FEATURES)
    fake_labels = (
        features.dot(coef_vector) +
        numpy.random.random(NUM_EXAMPLES)
    )
    return fake_labels > numpy.ma.median(fake_labels)

if __name__ == '__main__':
    main()
