import pandas as pd
import os
from sklearn.metrics import mean_squared_error

__makecsv__ = False
#__makecsv__ = True

MSE_index = 150
MSE_value = float('inf')

if __name__ == '__main__':
    acceleration_data = pd.read_csv("acceleration.csv")
    deceleration_data = pd.read_csv("deceleration.csv")

    start_S = 150
    end_S = 300

    if __makecsv__:
        for S in range(start_S, end_S+1):
            os.system(f"./ODE/ODE -override S={S}")
            YachtPlant = pd.read_csv("ODE_res.csv", delimiter=",", skiprows=[2, 3, 84], usecols=["time", "v"])
            YachtPlant.to_csv(f"csv/S{S}.csv", index=False)

    for S in range(start_S, end_S+1):
        S_csv = pd.read_csv(f"csv/S{S}.csv")
        MSE_temp = mean_squared_error(acceleration_data.values, S_csv.values)

        print(MSE_temp)
        if MSE_temp < MSE_value:
            MSE_index = S
            MSE_value = MSE_temp

    print("Best MSE Acceleration: " + str(MSE_index))