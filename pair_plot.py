from describe import get_numerical_columns_normalized
from load_csv import load
import pandas as pd
from matplotlib import pyplot as plt
from pandas.plotting import scatter_matrix


def plot(datas, subject1, subject2):
    plt.figure(figsize=(12, 9))
    plt.scatter(x=datas[subject1], y=datas[subject2])
    plt.xlabel(subject1)
    plt.ylabel(subject2)
    plt.title("Scatter plot of result in DADA comparing to results in astronomy")
    plt.show()

train = load("datasets/dataset_train.csv")
if train is None:
    print("Error loading the file")
    exit(1)
numerical_train = get_numerical_columns_normalized(train)
matrix = scatter_matrix(numerical_train, figsize=(16, 12))
for ax in matrix.flatten():
    ax.xaxis.label.set_rotation(45)
    ax.yaxis.label.set_rotation(45)
    ax.yaxis.label.set_position((-10, 0))
plt.show()