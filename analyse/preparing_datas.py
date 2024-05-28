from utils.stats import mean, median, var
from utils.load_csv import load
from analyse.describe import get_numerical_columns_normalized
import numpy as np

def prepare(path, house):
    train = load(path)
    if train is None:
        exit (1)

    train.dropna(inplace=True)
    train.to_csv("nona.csv")

    train["Hogwarts House"] = train["Hogwarts House"].apply(lambda x: 1 if x == house else 0).astype(int)
    train["Hogwarts House"] = train["Hogwarts House"].astype(bool)
    numerical_train = get_numerical_columns_normalized(train)
    numerical_train["Hogwarts House"] = train["Hogwarts House"]
    return numerical_train

def split_thetas(str):
    thetas = [float(theta.strip("[] \n")) for theta in str.split(",")]
    return thetas

def get_thetas():
    houses_thetas = {}
    with open("theta.txt") as file:
        line = file.readline()
        while line:
            house = line.split(":")[0]
            weights = line.split(":")[1]
            houses_thetas[house] = split_thetas(weights)
            line = file.readline()
    return (houses_thetas)

def prepare_test(path):
    test = load(path)
    if test is None:
        exit (1)
    numerical_test = get_numerical_columns_normalized(test)

    print(numerical_test.dropna().shape)
    print(numerical_test.shape)
    
