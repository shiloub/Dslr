from analyse.preparing_datas import get_thetas, prepare_test
import pandas as pd
from logreg_train import g

def find_subject(serie, subjects):
    positions = []
    for subject, i in zip(serie.index, range(len(serie))):
        if subject in subjects:
            positions.append(i)
    return (positions)

def predict(x, theta):
    # print(len(x))
    temp_theta = theta.copy()
    temp_x = x.copy()
    if (x.isna().any()):
        nan_position = x.isna()
        nan_subjects = nan_position[nan_position].index.tolist()
        subject_position=find_subject(x, nan_subjects)
        for i in subject_position:
            del temp_theta[i]
        temp_x.dropna(inplace = True)
        assert (len(temp_x) == len(temp_theta)), f"len(x) = {len(temp_x)}, len(temp_theta) = {len(temp_theta)}:"
        return g(sum(xi * thetai for xi, thetai in zip(temp_x, temp_theta)))
    assert (len(temp_x) == len(temp_theta)), f"len(x) = {len(temp_x)}, len(temp_theta) = {len(temp_theta)}:"
    return g(sum(xi * thetai for xi, thetai in zip(temp_x, temp_theta)))

def main():
    house_thetas = get_thetas()
    test = prepare_test("data/dataset_train.csv")
    test.dropna(inplace=True)
    test["biais"] = 1
    cols = test.columns.tolist()
    cols = ['biais'] + [col for col in cols if col != 'biais']
    test = test[cols]
    houses = []
    for i, line in test.iterrows():
        try:
            slyt_score = predict(line, house_thetas["slyt"])
            gryf_score = predict(line, house_thetas["gryf"])
            rave_score = predict(line, house_thetas["rave"])
            huff_score = predict(line, house_thetas["huff"])
        except Exception as error:
            print("Valeur manquante non geree", error)
            continue
        max_ = max([slyt_score, gryf_score, rave_score, huff_score])
        if max_ == slyt_score:
            houses.append("Slytherin")
        elif max_ == gryf_score:
            houses.append("Gryffindor")
        elif max_ == rave_score:
            houses.append("Ravenclaw")
        elif max_ == huff_score:
            houses.append("Hufflepuff")
    houses = pd.DataFrame(houses)
    houses.columns = ["Hogwarts House"]
    houses["Index"] = houses.index
    houses.set_index("Index", inplace=True)
    houses.to_csv("houses.csv")

if __name__ == "__main__":
    main()