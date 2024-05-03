from load_csv import load
from stats import mean, median, first_quartile, third_quartile, std, var, min, max, count
import pandas as pd

def main():
    train = load("datasets/dataset_train.csv")
    numerical = train.dtypes[train.dtypes == "float64"].index
    numerical_train = train[numerical]
    print(numerical_train.describe())
    print(type(numerical_train.describe()))
    describe = {column : [count(numerical_train[column]),
                          mean(numerical_train[column]),
                          std(numerical_train[column]),
                          min(numerical_train[column]),
                          first_quartile(numerical_train[column]),
                          median(numerical_train[column]),
                          third_quartile(numerical_train[column]),
                          max(numerical_train[column])
                          ] for column in numerical_train.columns}
    describe = pd.DataFrame(describe)
    describe.set_index(pd.Index(["Count", "Mean", "std", "min", "25%", "50%", "75%", "max"]), inplace = True)
    print(describe)


if __name__ == "__main__":
    main()