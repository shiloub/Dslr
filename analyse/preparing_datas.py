from utils.stats import mean, median, var
from utils.load_csv import load
from analyse.describe import get_numerical_columns_normalized
import numpy as np

def prepare(path, house):
    train = load(path)
    if train is None:
        exit (1)

    train.dropna(inplace=True)
    train["Hogwarts House"] = train["Hogwarts House"].apply(lambda x: 1 if x == house else 0).astype(int)
    train["Hogwarts House"] = train["Hogwarts House"].astype(bool)
    numerical_train = get_numerical_columns_normalized(train)
    numerical_train["Hogwarts House"] = train["Hogwarts House"]
    return numerical_train
