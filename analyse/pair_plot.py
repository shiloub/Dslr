from describe import get_numerical_columns_normalized
from utils.load_csv import load
from matplotlib import pyplot as plt
from pandas.plotting import scatter_matrix
import pandas as pd

train = load("datasets/dataset_train.csv")
if train is None:
    print("Error loading the file")
    exit(1)

houses_colors = {"Slytherin": "green",
                "Hufflepuff": "yellow",
                "Ravenclaw": "blue",
                "Gryffindor": "red"}

# numerical_train = get_numerical_columns_normalized(train)

# numerical_train["color"] = [houses_colors[house] for house in numerical_train['Hogwarts House']]
# print(numerical_train)

train["color"] = [houses_colors[house] for house in train['Hogwarts House']]
train.dropna(inplace=True)
numerical_train = get_numerical_columns_normalized(train)
for column in numerical_train:
    train[column] = numerical_train[column]
print(train)
matrix = scatter_matrix(train, figsize=(16, 12), color=[color for color in train["color"]])
for ax in matrix.flatten():
    ax.xaxis.label.set_rotation(45)
    ax.yaxis.label.set_rotation(45)
plt.show()