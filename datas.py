from load_csv import load
from stats import mean, median, first_quartile, third_quartile, std, min, max, count
import pandas as pd
import sys

def main():
    if (len(sys.argv) != 2):
        print("Error: one argument expected: dataPath")
        exit(0)
    train = load(sys.argv[1])
    if (train is None):
        print("Error loading the file")
        exit(1)
    numericalTypes = ["float64", "int64", "int32", "float32", "int16", "float16", "uint8", "uint16", "uint32", "uint"]
    # numerical = train.dtypes[train.dtypes == "float64"].index
    numerical = train.dtypes[train.dtypes.astype(str).isin(numericalTypes)].index
    numerical_train = train[numerical]
    describe = {column : [count(numerical_train[column]),
                          mean(numerical_train[column]),
                          std(numerical_train[column]),
                          min(numerical_train[column]),
                          first_quartile(numerical_train[column]),
                          median(numerical_train[column]),
                          third_quartile(numerical_train[column]),
                          max(numerical_train[column])
                          ] for column in numerical_train.columns}
    real_describe = numerical_train.describe()
    del real_describe["Index"]
    print(real_describe)
    print("-----------------------------------------")
    describe = pd.DataFrame(describe)
    del describe["Index"]
    describe.set_index(pd.Index(["Count", "Mean", "Std", "Min", "25%", "50%", "75%", "Max"]), inplace = True)
    print(describe - real_describe)
    print(describe)


if __name__ == "__main__":
    main()