import pandas as pd
import scipy
from scipy import io
import os

acceleration_data = pd.read_csv("acceleration.csv")
deceleration_data = pd.read_csv("deceleration.csv")

working_directory = "/private/var/folders/hf/cmv_674s41s716119nhrhb5h0000gn/T/OpenModelica_gauthierlecompte/OMEdit/ODE/"



start_S = 150
end_S = 300

for S in range(start_S, end_S):
    os.system(f"./ODE -override S={S}")
