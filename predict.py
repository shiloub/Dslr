from training import predict
from analyse.preparing_datas import prepare

def main():
    theta = [0.9062190527998321, -0.09609555920688433, 0.9492003756034163, -1.8417226352773377, -1.0429613228035821, 0.6132612272626533, -0.48861779097084407, 1.6580702056621854, -2.330161349793085, -2.52215089463147, -0.9136497310016602, -0.1279728542113315, -1.2928502752905582, 2.106491668516121]
    data = prepare("datasets/dataset_train.csv", "Gryffindor")
    del data["Hogwarts House"]
    data['biais'] = 1

    cols = data.columns.tolist()
    cols = ['biais'] + [col for col in cols if col != 'biais']
    data = data[cols]
    print(data)
    for i, line in data.iterrows():
        # x = [1] + [y for y in line]
        print(predict(line, theta), "   ", i)


if __name__ == "__main__":
    main()