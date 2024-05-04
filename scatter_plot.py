from describe import get_describe
from load_csv import load
import pandas as pd
from matplotlib import pyplot as plt


def plot(subject1, subject2):
    plt.figure(figsize=(12, 9))
    plt.scatter(x=train[subject1], y=train[subject2])
    plt.xlabel(subject1)
    plt.ylabel(subject2)
    plt.title("Scatter plot of result in DADA comparing to results in astronomy")
    plt.show()

train = load("datasets/dataset_train.csv")
# print(train.columns)
# for subject1 in train.columns[6:]:
#     for subject2 in train.columns[6:]:
#         if (subject1 != subject2):
#             plot(subject1, subject2)
plot("Defense Against the Dark Arts", "Astronomy")