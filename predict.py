from training import predict
from analyse.preparing_datas import prepare, get_thetas, prepare_test

def main():
    # trad = {"slyt": "Slytherin",
    #         "gryp": "Gryffudor",
    #         "huff": "Hufflepuff",
    #         "rave": "Ravenclaw"}
    
    # house_thetas = get_thetas()
    # data = prepare("datasets/dataset_train.csv", "Gryffindor")
    # del data["Hogwarts House"]
    # data['biais'] = 1
    test = prepare_test("datasets/dataset_train.csv")
    # cols = data.columns.tolist()
    # cols = ['biais'] + [col for col in cols if col != 'biais']
    # data = data[cols]
    # print(data)
    # for i, line in data.iterrows():
    #     slyt_score = predict(line, house_thetas["slyt"])
    #     gryf_score = predict(line, house_thetas["gryf"])
    #     rave_score = predict(line, house_thetas["rave"])
    #     huff_score = predict(line, house_thetas["huff"])
    #     max_ = max([slyt_score, gryf_score, rave_score, huff_score])
    #     if max_ == slyt_score:
    #         print("Slytherin")
    #     elif max_ == gryf_score:
    #         print("Gryffundor")
    #     elif max_ == rave_score:
    #         print("Ravenclaw")
    #     elif max_ == huff_score:
    #         print("Hufflepuf")


if __name__ == "__main__":
    main()