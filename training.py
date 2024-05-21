from analyse.preparing_datas import prepare
import numpy as np
from loading import ft_tqdm

def g(z):
    return 1 / (1 + np.exp(-z))

def h(x, theta):
    return g(scalaire(x, theta))

def scalaire(x, theta):
    result = 0
    assert len(x) == len(theta)
    for i in range(len(x)):
        result += x[i] * theta[i]
        # result += x.iloc[i] * theta[i]

    return result


def gradient(train, theta, j):
    houses = train["Hogwarts House"]
    data = train.copy(deep=True)
    del data["Hogwarts House"]
    m = len(data)
    sum_ = 0
    for (i, x) in train.iterrows():
        sum_ += (h(x, theta) - train["Hogwarts House"][i]) * x[j]
    gradient = (1 / m) * sum_
    return gradient




def logistic_regression(train, alpha):
    theta = [0.00001 for i in range(train.shape[1])]
    theta[0] = 1
    for k in ft_tqdm(range(1000)):
       theta_temp = [theta[j] - alpha * gradient(train, theta, j) for j in range(0, len(theta))]
       theta = theta_temp
    return theta



def main():
    gryffindor = prepare("datasets/dataset_train.csv", "Gryffindor")
    # print(gryffindor.head())
    # print(gryffindor.shape)
    print(logistic_regression(gryffindor, 0.01))

if __name__ == "__main__":
    main()