from analyse.preparing_datas import prepare
import numpy as np

def g(z):
    return 1 / (1 + np.exp(-z))

def h(x, theta):
    return g(x * theta)

def logistic_regression(train, alpha):
    theta = [0.00001 for i in range(train.shape[1] + 1)]
    theta[0] = 1
    print(train)
    print(train.dtypes)
    # for i in range(1000):



def main():
    gryffindor = prepare("datasets/dataset_train.csv", "Gryffindor")
    logistic_regression(gryffindor, 0)

if __name__ == "__main__":
    main()