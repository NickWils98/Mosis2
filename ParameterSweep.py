import pandas as pd
import os
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# __make_csv__ = False
__make_csv__ = True

# __MSE__ = False
__MSE__ = True

MSE_index = 150
MSE_value = float('inf')
start_S = 150
end_S = 300

if __name__ == '__main__':
    acceleration_data = pd.read_csv("acceleration.csv")
    deceleration_data = pd.read_csv("deceleration.csv")
    samples = acceleration_data.append(deceleration_data, ignore_index=True)

    S_list = []
    MSE_list = []

    if __make_csv__:
        for S in range(start_S, end_S+1):
            os.system(f"YachtPlant_accelerate/YachtPlant_accelerate -override S={S}")
            YachtPlant = pd.read_csv("YachtPlant_accelerate_res.csv", delimiter=",",skiprows=[3,4],skipfooter=1, usecols=["time", "v"])
            YachtPlant.to_csv(f"csv/accelerate/S{S}.csv", index=False)

        for S in range(start_S, end_S+1):
            os.system(f"YachtPlant_decelerate/YachtPlant_decelerate -override S={S}")
            YachtPlant = pd.read_csv("YachtPlant_decelerate_res.csv", delimiter=",",skipfooter=1, usecols=["time", "v"])
            YachtPlant.to_csv(f"csv/decelerate/S{S}.csv", index=False)

    if __MSE__:
        for S in range(start_S, end_S+1):
            S_csv_ac = pd.read_csv(f"csv/accelerate/S{S}.csv")
            S_csv_de = pd.read_csv(f"csv/decelerate/S{S}.csv")
            model = S_csv_ac.append(S_csv_de, ignore_index=True)
            # MSE = mean_squared_error(acceleration_data.values, S_csv_ac.values)
            MSE = mean_squared_error(samples.values, model.values)
            MSE_list.append(MSE)
            S_list.append(S)
            print(f"For file S{S}.csv: MSE = {MSE}")
            if MSE < MSE_value:
                MSE_index = S
                MSE_value = MSE

        df = pd.DataFrame(list(zip(S_list, MSE_list)), columns=['S', 'MSE'])

        best_MSE_index = MSE_list.index(min(MSE_list))
        print("Best MSE: " + f"{S_list[best_MSE_index]}")

        df.plot(x='S', y='MSE', kind='scatter')
        # plt.show()
        plt.savefig("MSE150-300.png")
