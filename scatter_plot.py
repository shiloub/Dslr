from describe import get_numerical_columns_normalized
from load_csv import load
from stats import mean
import pandas as pd
from matplotlib import pyplot as plt

def corr(datas, subject1, subject2):
    valid_pairs = pd.DataFrame({subject1: datas[subject1], subject2: datas[subject2]}).dropna()
    xbar = mean(valid_pairs[subject1])
    ybar = mean(valid_pairs[subject2])
    num = sum((x - xbar) * (y - ybar) for (x, y) in zip(valid_pairs[subject1], valid_pairs[subject2]))
    dem = (sum((x - xbar) ** 2 for x in valid_pairs[subject1]) * sum((y - ybar) ** 2 for y in valid_pairs[subject2])) ** 0.5
    return (num / dem)


def get_cor_line(datas, subject):
    cor_line = pd.Series(corr(datas, subject, sub) for sub in datas.columns)
    return (cor_line)


def get_corr_tab(datas):
    cor_tab = pd.DataFrame({sub: get_cor_line(datas, sub) for sub in datas.columns})
    cor_tab.set_index(datas.columns, inplace=True)
    return(cor_tab)

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
# for subject1 in train.columns[6:]:
#     for subject2 in train.columns[6:]:
#         if (subject1 != subject2):
#             plot(numerical_train, subject1, subject2)
plot(numerical_train, "History of Magic", "Transfiguration")
# plot(numerical_train, "Defense Against the Dark Arts", "Astronomy")
# print(numerical_train.corr())
# print("-------------------------------------")
print(get_corr_tab(numerical_train).loc["History of Magic", "Transfiguration"])
# print(corr(numerical_train, "Defense Against the Dark Arts", "Astronomy"))