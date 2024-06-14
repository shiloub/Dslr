from utils.load_csv import load
import pandas as pd
from matplotlib import pyplot as plt

def plot(subject: str):
    plt.figure(figsize=(12, 9))
    bins = 18
    plt.hist(x=Slytherins[subject],
             bins=bins,
             label = "Slytherin",
             alpha = 0.5,
             color="green")
    
    plt.hist(x=Ravenclaws[subject],
             bins=bins,
             label = "Ravenclaw",
             alpha = 0.5,
             color="blue")
    
    plt.hist(x=Gryffindors[subject],
             bins=bins,
             label = "Gryffindor",
             alpha = 0.5,
             color="red")
    
    plt.hist(x=Hufflepuffs[subject],
             bins=bins,
             label = "Hufflepuff",
             alpha = 0.5,
             color="yellow")

    plt.title(subject)
    plt.legend()
    plt.show()
    

train = load("datasets/dataset_train.csv")
Slytherins = train[train["Hogwarts House"] == "Slytherin"]
Ravenclaws = train[train["Hogwarts House"] == "Ravenclaw"]
Hufflepuffs = train[train["Hogwarts House"] == "Hufflepuff"]
Gryffindors = train[train["Hogwarts House"] == "Gryffindor"]

for subject in train.columns[6:]:
    plot(subject)

#The answer is:
plot("Care of Magical Creatures")
#or:
plot("Arithmancy")
