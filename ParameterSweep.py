import pandas as pd
import os
from sklearn.metrics import mean_squared_error

MSE_index = 150
MSE_value = 99999999999999999

if __name__ == '__main__':

    acceleration_data = pd.read_csv("acceleration.csv")
    deceleration_data = pd.read_csv("deceleration.csv")
    start_S = 150
    end_S = 300

    # for S in range(start_S, end_S+1):
        # os.system(f"./ODE/ODE -override S={S}")
        # YachtPlant = pd.read_csv("ODE_res.csv", delimiter=",", skiprows=[2, 3, 84], usecols=["time", "v"])
        # YachtPlant.to_csv(f"csv/S{S}.csv", index=False)

    for S in range(start_S, end_S + 1):

        S_csv = pd.read_csv(f"csv/S{S}.csv")
        MSE_temp = mean_squared_error(acceleration_data.values, S_csv.values)

        if MSE_temp < MSE_value:
            MSE_index = S
            MSE_value = MSE_temp

print(MSE_index)