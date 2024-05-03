from load_csv import load
from stats import mean, median, first_quartile, third_quartile, std, min, max, count
import pandas as pd
import sys

def get_describe(datas) -> pd.DataFrame:
    numericalTypes = ["float64", "int64", "int32", "float32", "int16", "float16", "uint8", "uint16", "uint32", "uint"]
    # numerical = train.dtypes[train.dtypes == "float64"].index
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
    del describe["Index"]
    describe.set_index(pd.Index(["Count", "Mean", "Std", "Min", "25%", "50%", "75%", "Max"]), inplace = True)
    return describe


def main():
    if (len(sys.argv) != 2):
        print("Error: one argument expected: dataPath")
        exit(0)
    train = load(sys.argv[1])
    if (train is None):
        print("Error loading the file")
        exit(1)
    del train["Charms"]
    del train["Flying"]
    del train["Astronomy"]
    numericalTypes = ["float64", "int64", "int32", "float32", "int16", "float16", "uint8", "uint16", "uint32", "uint"]
    # numerical = train.dtypes[train.dtypes == "float64"].index
    numerical = train.dtypes[train.dtypes.astype(str).isin(numericalTypes)].index
    numerical_train = train[numerical]
    real_describe = numerical_train.describe()
    del real_describe["Index"]
    print(real_describe)
    print("-----------------------------------------")
    print(get_describe(train))


if __name__ == "__main__":
    main()