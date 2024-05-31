from utils.load_csv import load

from sklearn.metrics import precision_score
def main():
    test = load("datasets/dataset_train.csv")
    houses = load("houses.csv")

    n_error = sum(1 for (prediction, real) in zip(test["Hogwarts House"], houses["Hogwarts House"]) if prediction != real)
    n_true = sum(1 for (prediction, real) in zip(test["Hogwarts House"], houses["Hogwarts House"]) if prediction == real)
    print(f"macro {precision_score(houses['Hogwarts House'], test['Hogwarts House'], average='macro'):.2f}")
    print(f"micro {precision_score(houses['Hogwarts House'], test['Hogwarts House'], average='micro'):.2f}")
    print(f"weighted {precision_score(houses['Hogwarts House'], test['Hogwarts House'], average='weighted'):.2f}")
    # test()

def test():
    test = load("datasets/dataset_train.csv")
    # test.dropna(inplace=True)
    houses = load("houses.csv")

    n_error = sum(1 for (prediction, real) in zip(test["Hogwarts House"], houses["Hogwarts House"]) if prediction != real)
    n_true = sum(1 for (prediction, real) in zip(test["Hogwarts House"], houses["Hogwarts House"]) if prediction == real)
    total = n_true + n_error

    # for prediction, real, i in zip(test["Hogwarts House"], houses["Hogwarts House"], range(len(houses))):
    #     if (prediction != real):
    #         print(prediction, real, i)
    print(f"The prediction are right {((n_true / total) * 100):.2f}% of the time")
    # print(n_error, n_true)

if __name__ == "__main__":
    main()