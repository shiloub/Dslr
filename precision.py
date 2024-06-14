from utils.load_csv import load

from sklearn.metrics import precision_score
def main():
    test = load("data/dataset_train.csv")
    if test is None:
        exit(1)
    houses = load("houses.csv")

    print(f"sklearn precision: {precision_score(houses['Hogwarts House'], test['Hogwarts House'], average='weighted')}")

if __name__ == "__main__":
    main()