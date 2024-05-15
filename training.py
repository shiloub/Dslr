from analyse.preparing_datas import prepare
import numpy as np

def g(z):
    return 1 / (1 + np.exp(-z))




def main():
    train = prepare("datasets/dataset_train.csv")
    print(train)

if __name__ == "__main__":
    main()