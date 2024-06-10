from utils.stats import mean, median, var
from utils.load_csv import load
from analyse.describe import get_numerical_columns_centered_and_scaled
import numpy as np
import pandas as pd


def prepare_train(path, house):
    train = load(path)
    if train is None:
        exit (1)
    train.dropna(inplace=True)

    train["Hogwarts House"] = train["Hogwarts House"].apply(lambda x: 1 if x == house else 0).astype(int)
    train["Hogwarts House"] = train["Hogwarts House"].astype(bool)
    numerical_train = get_numerical_columns_centered_and_scaled(train)
    numerical_train["Hogwarts House"] = train["Hogwarts House"]
    del numerical_train["Care of Magical Creatures"]
    del numerical_train["Arithmancy"]
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
    del test["Hogwarts House"]
    numerical_test = get_numerical_columns_centered_and_scaled(test)
    del numerical_test["Care of Magical Creatures"]
    del numerical_test["Arithmancy"]
    return numerical_test
