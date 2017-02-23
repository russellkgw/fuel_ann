import math

# Sigmoid

def sigmoid(value):
    lambda_val = -1.0
    return 1.0 / (1.0 + math.e ** (lambda_val * value))

def sigmoid_gd(target_value, fire_result):
    return 2.0 * (target_value - fire_result) * fire_result * (1.0 - fire_result)

# Hyperbolic tangent

def hyperbolic(value):
    lambda_val = -1.0
    return (2.0 / (1.0 + math.e ** (lambda_val * value))) - 1.0

# Linear

def linear(value):
    lambda_val = 1.0
    return lambda_val * value

# Step

def step(net, theta):
    if net >= theta:
        return 1.0
    else:
        return 0.0

# Learning

def widrow_hoff(target_value, fire_result):
    return 2.0 * (target_value - fire_result)

# Gradient descent where derivative is 1
def gradient_descent(target_value, fire_result):
    return 2.0 * (target_value - fire_result)