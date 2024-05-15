from utils.stats import mean, median, var
from utils.load_csv import load
from analyse.describe import get_numerical_columns_normalized

def prepare(path):
    train = load(path)
    if train is None:
        exit (1)

    train.dropna(inplace=True)
    numerical_train = get_numerical_columns_normalized(train)
    for column in numerical_train:
        train[column] = numerical_train[column]
    train.drop("Index", axis=1, inplace=True)
    return train
