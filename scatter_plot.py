from describe import get_describe
from load_csv import load
import pandas as pd
from matplotlib import pyplot as plt

train = load("datasets/dataset_train.csv")
print(train.columns)