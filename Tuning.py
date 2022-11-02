import pandas as pd
import os
from sklearn.metrics import mean_squared_error

MSE_value = float('inf')

# Set initial values for K-value intervals
start_Kp = 6000
end_Kp = 7000

start_Ki = 300
end_Ki = 350

start_Kd = -1
end_Kd = 1

if __name__ == '__main__':
    # Set initial K-values to zero
    MSE_list = []
    best_Kp = 0
    best_Ki = 0
    best_Kd = 0

    # Loop over all possible K-values
    for Kp in range(start_Kp, end_Kp+1):
        k = Kp
        for Ki in range(start_Ki, end_Ki+1):
            Ti = k / Ki
            for Kd in range(start_Kd, end_Kd+1):
                Td = Kd / k

                # Run Command for certain k, Ti and Td values
                os.system(f"FullPlantControllerPID/FullPlantControllerPID -override K={k},ti={Ti},td={Td}")
                FullPlantPID = pd.read_csv("FullPlantControllerPID_res.csv", delimiter=",", skipfooter=1, usecols=["costfunction.vi", "costfunction.v"])

                # Calculate MSE
                MSE = mean_squared_error(FullPlantPID["costfunction.vi"], FullPlantPID["costfunction.v"])
                MSE_list.append(MSE)

                # Set new best MSE and K-values if needed
                if MSE == min(MSE_list):
                    MSE_value = MSE
                    best_Kp = Kp
                    best_Ki = Ki
                    best_Kd = Kd

        print(f"Best Kp: {best_Kp}")
        print(f"Best Ki: {best_Ki}")
        print(f"Best Kd: {best_Kd}")
