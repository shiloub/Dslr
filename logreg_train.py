from analyse.preparing_datas import prepare_train
import numpy as np
from utils.loading import ft_tqdm
from utils.load_csv import load
import sys

def g(z):
    return 1 / (1 + np.exp(-z))


def predict(x, theta):
    assert len(x) == len(theta)
    return g(sum(xi * thetai for xi, thetai in zip(x, theta)))
    

def gradient(x, y, theta, j):
    sum_ = sum((predict(xi, theta) - int(y[i])) * xi.iloc[j] for i, xi in x.iterrows())
    gradient = (1 / len(x)) * sum_
    return gradient

def logistic_regression(train, alpha, nb_iteration):
    theta = [0.01 for i in range(train.shape[1])]
    theta[0] = 2
    houses = train["Hogwarts House"]
    data = train.copy(deep=True)
    del data["Hogwarts House"]
    data['biais'] = 1

    cols = data.columns.tolist()
    cols = ['biais'] + [col for col in cols if col != 'biais']
    data = data[cols]
    for k in ft_tqdm(range(nb_iteration)):
       theta_temp = [theta[j] - alpha * gradient(data, houses, theta, j) for j in range(0, len(theta))]
       theta = theta_temp
    return theta



def main():
    if (len(sys.argv) != 2):
        print("Error: one argument expected: dataPath")
        exit(0)
    gryffindor = prepare_train(sys.argv[1], "Gryffindor")
    slytherin = prepare_train(sys.argv[1], "Slytherin")
    ravenclaw = prepare_train(sys.argv[1], "Ravenclaw")
    hufflepuff = prepare_train(sys.argv[1], "Hufflepuff")
    # gryffindor.to_csv(

    alpha = 5
    nb_ite = 20

    gryff_weights = logistic_regression(gryffindor, alpha, nb_ite)
    slyth_weights = logistic_regression(slytherin, alpha, nb_ite)
    raven_weights = logistic_regression(ravenclaw, alpha, nb_ite)
    huffl_weights = logistic_regression(hufflepuff, alpha, nb_ite)

    with open("theta.txt", mode="w") as file:
        file.write(f"gryf:{gryff_weights}\n")
        file.write(f"slyt:{slyth_weights}\n")
        file.write(f"rave:{raven_weights}\n")
        file.write(f"huff:{huffl_weights}")

if __name__ == "__main__":
    main()