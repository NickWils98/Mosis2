import pandas as pd
import os
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

__makecsv__ = False
#__makecsv__ = True

MSE_index = 150
MSE_value = float('inf')
start_S = 150
end_S = 300

if __name__ == '__main__':
    acceleration_data = pd.read_csv("acceleration.csv")
    deceleration_data = pd.read_csv("deceleration.csv")
    deceleration_data.v = deceleration_data.v.values[::-1]

    S_list = []
    MSE_list = []

    if __makecsv__:
        for S in range(start_S, end_S+1):
            os.system(f"./ODE/ODE -override S={S}")
            YachtPlant = pd.read_csv("ODE_res.csv", delimiter=",", skiprows=[2, 3, 84], usecols=["time", "v"])
            YachtPlant.to_csv(f"csv/S{S}.csv", index=False)

    for S in range(start_S, end_S+1):
        S_csv = pd.read_csv(f"csv/S{S}.csv")
        MSE_ACC = mean_squared_error(acceleration_data.values, S_csv.values)
        MSE_DEC = mean_squared_error(deceleration_data.values, S_csv.values)

        MSE = MSE_ACC+MSE_DEC
        MSE_list.append(MSE)
        S_list.append(S)
        print(f"For file S{S}.csv: MSE = {MSE}")

    df = pd.DataFrame(list(zip(S_list, MSE_list)), columns=['S', 'MSE'])

    best_MSE_index = MSE_list.index(min(MSE_list))
    print("Best MSE: " + f"{S_list[best_MSE_index]}")

    df.plot(x='S', y='MSE', kind='scatter')
    plt.show()