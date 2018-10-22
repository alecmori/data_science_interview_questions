import numpy

def linear_loss(labels, predictions):
    diff = labels - predictions
    return numpy.sum(
        numpy.multiply(
            diff,
            diff,
        ),
    )

def get_update_linear(
    features, labels, predictions, learning_rate, num_examples,
):
    return learning_rate * (predictions - labels).dot(features)/num_examples
    
def train_model(
    loss_func, update_func, features, labels, learning_rate=0.05, tol=1e-5,
    max_iter=10000,
):
    num_examples, _ = features.shape
    features = numpy.append(
        arr=features,
        values=numpy.ones((num_examples, 1)),
        axis=1,
    )
    _, num_features = features.shape
    coefs = numpy.random.random(num_features)
    predictions = features.dot(coefs)
    i = 0
    while (
        loss_func(labels=labels, predictions=predictions) > tol
        and i < max_iter
    ):
        i += 1
        coefs -= update_func(
            features=features,
            labels=labels,
            predictions=predictions,
            learning_rate=learning_rate,
            num_examples=num_examples,
        )
        predictions = features.dot(coefs)
    return {
        'coefficients': coefs[:-1],
        'intercept': coefs[-1],
    }
