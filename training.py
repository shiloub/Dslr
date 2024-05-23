from analyse.preparing_datas import prepare
import numpy as np
from loading import ft_tqdm

def g(z):
    return 1 / (1 + np.exp(-z))

def predict(x, theta):
    return g(sum(xi * thetai for xi, thetai in zip(x, theta)))


def gradient(x, y, theta, j):
    sum_ = sum((predict(xi, theta) - int(y[i])) * xi.iloc[j] for i, xi in x.iterrows())
    gradient = (1 / len(x)) * sum_
    return gradient




def logistic_regression(train, alpha):
    theta = [0.00001 for i in range(train.shape[1])]
    theta[0] = 1
    houses = train["Hogwarts House"]
    data = train.copy(deep=True)
    del data["Hogwarts House"]
    data['biais'] = 1

    cols = data.columns.tolist()
    cols = ['biais'] + [col for col in cols if col != 'biais']
    data = data[cols]
    for k in ft_tqdm(range(1000)):
       theta_temp = [theta[j] - alpha * gradient(data, houses, theta, j) for j in range(0, len(theta))]
       theta = theta_temp
    return theta



def main():
    gryffindor = prepare("datasets/dataset_train.csv", "Gryffindor")
    slytherin = prepare("datasets/dataset_train.csv", "Slytherin")
    ravenclaw = prepare("datasets/dataset_train.csv", "Ravenclaw")
    hufflepuff = prepare("datasets/dataset_train.csv", "Hufflepuff")
    # gryffindor.to_csv("./gryff.csv")

    with open("theta.txt", mode="w") as file:
        file.write(f"gryf:{logistic_regression(gryffindor, 0.1)}")
        file.write(f"slyt:{logistic_regression(slytherin, 0.1)}")
        file.write(f"rave:{logistic_regression(ravenclaw, 0.1)}")
        file.write(f"huff:{logistic_regression(hufflepuff, 0.1)}")

if __name__ == "__main__":
    main()