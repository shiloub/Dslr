from load_csv import load
from stats import mean, median, first_quartile, third_quartile, std, min, max, count
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

def get_numerical_columns_normalized(datas):
    numericalTypes = ["float64", "int64", "int32", "float32", "int16", "float16", "uint8", "uint16", "uint32", "uint"]
    numerical = datas.dtypes[datas.dtypes.astype(str).isin(numericalTypes)].index
    numerical_datas = datas[numerical]
    del numerical_datas["Index"]
    normalized = numerical_datas.copy()
    for column in normalized.columns:
        normalized[column] = normalized[column].apply(lambda x: (x - normalized[column].min()) / (normalized[column].max() - normalized[column].min()))
    return normalized

def plot_box(datas):
    datas.dropna(inplace=True)
    plt.figure(figsize=(12, 9))
    print(datas.columns)
    plt.boxplot([datas[column] for column in datas.columns if column != "Arithmancy"], labels=[column for column in datas.columns if column != "Arithmancy"])
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
    numerical_train = get_numerical_columns_normalized(train)
    # real_describe = numerical_train.describe()
    # del real_describe["Index"]
    # print(real_describe)
    # print("-----------------------------------------")
    # print(get_describe(train))
    plot_box(numerical_train)


if __name__ == "__main__":
    main()