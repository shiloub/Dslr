from utils.stats import mean, median, var
from utils.load_csv import load
from analyse.describe import get_numerical_columns_normalized
import numpy as np
import pandas as pd


def prepare_train(path, house):
    train = load(path)
    if train is None:
        exit (1)

    # Slytherins = train[train["Hogwarts House"] == "Slytherin"]
    # Ravenclaws = train[train["Hogwarts House"] == "Ravenclaw"]
    # Hufflepuffs = train[train["Hogwarts House"] == "Hufflepuff"]
    # Gryffindors = train[train["Hogwarts House"] == "Gryffindor"]

    # Slytherins_nona = pd.DataFrame()
    # Ravenclaws_nona = pd.DataFrame()
    # Hufflepuffs_nona = pd.DataFrame()
    # Gryffindors_nona = pd.DataFrame()
    # print(train.iloc[81])
    # i = 0
    # for column in get_numerical_columns_normalized(train).columns:
    #     # print(f"colmun nane {column}")
    #     # print(f"before {Slytherins_nona[column]}")
    #     Slytherins_nona[column] = Slytherins[column].fillna(mean(Slytherins[column].dropna()))
    #     if column == "Astronomy":
    #         print(f">>> mean of my column is {mean(Slytherins[column].dropna())} {i}")
    #     i+=1
    #     Ravenclaws_nona[column] = Ravenclaws[column].fillna(mean(Ravenclaws[column].dropna()))
    #     Hufflepuffs_nona[column] = Hufflepuffs[column].fillna(mean(Hufflepuffs[column].dropna()))
    #     Gryffindors_nona[column] = Gryffindors[column].fillna(mean(Gryffindors[column].dropna()))

    # Slytherins_nona["Hogwarts House"] = "Slytherin"
    # Ravenclaws_nona["Hogwarts House"] = "Ravenclaw"
    # Hufflepuffs_nona["Hogwarts House"] = "Hufflepuff"
    # Gryffindors_nona["Hogwarts House"] = "Gryffindor"

    # train = pd.concat([Slytherins_nona, Ravenclaws_nona, Hufflepuffs_nona, Gryffindors_nona])
    # train["Index"] = train.index
    # print(mean(Slytherins["Astronomy"]))
    # train.sort_index(inplace=True)
    # print(train.iloc[81])
    train.dropna(inplace=True)

    train["Hogwarts House"] = train["Hogwarts House"].apply(lambda x: 1 if x == house else 0).astype(int)
    train["Hogwarts House"] = train["Hogwarts House"].astype(bool)
    numerical_train = get_numerical_columns_normalized(train)
    numerical_train["Hogwarts House"] = train["Hogwarts House"]
    # del numerical_train["Astronomy"]
    del numerical_train["Care of Magical Creatures"]
    # del numerical_train["Defense Against the Dark Arts"]
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
    # test.dropna(inplace=True)
    numerical_test = get_numerical_columns_normalized(test)
    # del numerical_test["Astronomy"]
    del numerical_test["Care of Magical Creatures"]
    # del numerical_test["Defense Against the Dark Arts"]
    del numerical_test["Arithmancy"]
    return numerical_test
