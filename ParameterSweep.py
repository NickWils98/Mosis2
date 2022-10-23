import pandas as pd
import scipy
from sklearn.metrics import mean_squared_error
import os

acceleration_data = pd.read_csv("acceleration.csv")
deceleration_data = pd.read_csv("deceleration.csv")

start_S = 150
end_S = 300

MSE_index = 150
MSE_value = 99999999999999999

for S in range(start_S, end_S+1):
    os.system(f"./ODE -override S={S},density=988")

    file = pd.read_csv("ODE_res.csv", usecols=['time', 'v'])
    file.to_csv(f'csv/S{S}.csv', index=False)

    S_csv = pd.read_csv(f"csv/S{S}.csv", usecols=['time', 'v'])
    MSE_temp = mean_squared_error(acceleration_data.values, S_csv.values)

    if MSE_temp < MSE_value:
        MSE_index = S
        MSE_value = MSE_temp

print(MSE_index)




#print(mean_squared_error(acceleration_data.values, moto.values))
