from training import h
from analyse.preparing_datas import prepare

def main():
    theta = [0.7019953083882849, 0.045454916793040985, -0.6315497049397719, -0.5206862767127801, -0.13488016442974707, -0.31424198390008823, 0.13395902975029253, -0.7893727680864071, -0.8791161097824552, -0.4869195635310431, -0.2584135789522841, -0.5363576965063338, 0.2994594361787841, 1.0244991221643136]
    data = prepare("datasets/dataset_train.csv", "Gryffindor")
    del data["Hogwarts House"]
    print(data)
    for i, line in data.iterrows():
        x = [1] + [y for y in line]
        print(h(x, theta))


if __name__ == "__main__":
    main()