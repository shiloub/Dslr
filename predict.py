from training import predict
from analyse.preparing_datas import prepare, get_thetas

def main():
    # theta = [0.9062190527998321, -0.09609555920688433, 0.9492003756034163, -1.8417226352773377, -1.0429613228035821, 0.6132612272626533, -0.48861779097084407, 1.6580702056621854, -2.330161349793085, -2.52215089463147, -0.9136497310016602, -0.1279728542113315, -1.2928502752905582, 2.106491668516121]
    trad = {"slyt": "Slytherin",
            "gryp": "Gryffudor",
            "huff": "Hufflepuff",
            "rave": "Ravenclaw"}
    
    house_thetas = get_thetas()
    data = prepare("datasets/dataset_train.csv", "Gryffindor")
    del data["Hogwarts House"]
    data['biais'] = 1

    cols = data.columns.tolist()
    cols = ['biais'] + [col for col in cols if col != 'biais']
    data = data[cols]
    print(data)
    for i, line in data.iterrows():
        slyt_score = predict(line, house_thetas["slyt"])
        gryf_score = predict(line, house_thetas["gryf"])
        rave_score = predict(line, house_thetas["rave"])
        huff_score = predict(line, house_thetas["huff"])
        max_ = max([slyt_score, gryf_score, rave_score, huff_score])
        if max_ == slyt_score:
            print("Slytherin")
        elif max_ == gryf_score:
            print("Gryffundor")
        elif max_ == rave_score:
            print("Ravenclaw")
        elif max_ == huff_score:
            print("Hufflepuf")


if __name__ == "__main__":
    main()