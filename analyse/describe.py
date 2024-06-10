from utils.load_csv import load
from utils.stats import mean, median, first_quartile, third_quartile, std, min, max, count
import pandas as pd
import sys
from matplotlib import pyplot as plt


def get_describe(datas) -> pd.DataFrame:
    numericalTypes = ["float64", "int64", "int32", "float32", "int16", "float16", "uint8", "uint16", "uint32", "uint"]
    numerical = datas.dtypes[datas.dtypes.astype(str).isin(numericalTypes)].index
    numerical_datas = datas[numerical]
    describe = {column : [count(numerical_datas[column]),
                          mean(numerical_datas[column]),
                          std(numerical_datas[column]),
                          min(numerical_datas[column]),
                          first_quartile(numerical_datas[column]),
                          median(numerical_datas[column]),
                          third_quartile(numerical_datas[column]),
                          max(numerical_datas[column])
                          ] for column in numerical_datas.columns}
    describe = pd.DataFrame(describe)
    describe.set_index(pd.Index(["Count", "Mean", "Std", "Min", "25%", "50%", "75%", "Max"]), inplace = True)
    return describe

def get_numerical_columns(datas):
    numericalTypes = ["float64", "int64", "int32", "float32", "int16", "float16", "uint8", "uint16", "uint32", "uint"]
    numerical = datas.dtypes[datas.dtypes.astype(str).isin(numericalTypes)].index
    numerical_datas = datas[numerical]
    del numerical_datas["Index"]
    return(numerical_datas)


# def get_numerical_columns_normalized(datas):
#     numerical_datas = get_numerical_columns(datas)
#     normalized = numerical_datas.copy()
#     for column in normalized.columns:
#         normalized[column] = normalized[column].apply(lambda x: (x - normalized[column].min()) / (normalized[column].max() - normalized[column].min()))
#     return normalized

def get_numerical_columns_centered_and_scaled(datas):
    numerical_datas = get_numerical_columns(datas)
    # centered = numerical_datas.copy()

    colmeans = [mean(numerical_datas[column]) for column in numerical_datas.columns]
    centered = numerical_datas - colmeans
    coldevs = [std(numerical_datas[column]) for column in numerical_datas.columns]
    centered_scaled = centered / coldevs
    return centered_scaled

def plot_box(datas):
    datas.dropna(inplace=True)
    plt.figure(figsize=(12, 9))
    print(datas.columns)
    plt.boxplot([datas[column] for column in datas.columns], labels=[column for column in datas.columns])
    plt.xticks(rotation=45)
    plt.show()

def main():
    if (len(sys.argv) != 2):
        print("Error: one argument expected: dataPath")
        exit(0)
    train = load(sys.argv[1])
    if (train is None):
        print("Error loading the file")
        exit(1)
    numerical_train = get_numerical_columns_centered_and_scaled(train)
    real_describe = train.describe()

    print("Real describe function on raw data:\n", real_describe)
    print("-----------------------------------------")
    print("My describe function on raw data:\n", get_describe(train))
    print("--------------------------------------------")
    print()
    print()
    print("--------------------------------------------")
    real_describe = numerical_train.describe()

    print("Real describe function on normalized data:\n", real_describe)
    print("-----------------------------------------")
    print("My describe function on normalize data:\n", get_describe(numerical_train))
    plot_box(get_numerical_columns(train))
    plot_box(numerical_train)


if __name__ == "__main__":
    main()