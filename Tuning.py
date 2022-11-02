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

start_Kp = 6000
end_Kp = 7000

start_Ki = 300
end_Ki = 350

start_Kd = -1
end_Kd = 1

if __name__ == '__main__':
    MSE_list = []

    best_Kp = 0
    best_Ki = 0
    best_Kd = 0
    best_index = -1

    if __make_csv__:
        k_counter = 0
        for Kp in range(start_Kp, end_Kp+1, 10):
            k = Kp
            for Ki in range(start_Ki, end_Ki+1):
                Ti = Ki / k
                for Kd in range(start_Kd, end_Kd+1):
                    Td = Kd / k
                    os.system(f"FullPlantControllerPID/FullPlantControllerPID -override K={k},ti={Ti},td={Td}")
                    FullPlantPID = pd.read_csv("FullPlantControllerPID_res1.csv", delimiter=",", skipfooter=1, usecols=["costfunction.v", "costfunction.vi"])

                    MSE = mean_squared_error(FullPlantPID.v, FullPlantPID.vi)
                    MSE_list.append(MSE)

                    best_temp = MSE_list.index(min(MSE_list))

                    if best_temp != best_index:
                        best_Kp = Kp
                        best_Ki = Ki
                        best_Kd = Kd
                        best_index = best_temp

        print(f"Best Kp: {best_Kp}")
        print(f"Best Ki: {best_Ki}")
        print(f"Best Kd: {best_Kd}")

    '''if __MSE__:
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
        plt.savefig("MSE150-300.png")'''
