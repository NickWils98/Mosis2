# Parameter Sweep
The map structure should look like the following:
- ParameterSweep.py
- csv
  - acceleration
    - ...
  - deceleration
    - ...
- YachtPlant_accelerate
  - YachtPlant_accelerate(executable)
- YachtPlant_decelerate
  - YachtPlant_decelerate(executable)
- YachtPlant_accelerate_init.xml (outputFormat = 'csv')
- YachtPlant_decelerate_init.xml (outputFormat = 'csv')

How to run: 
- The program has 2 parameters that determine what it will do:
  - \_\_make_csv\_\_: If true, the program will fill both the acceleration and deceleration maps with 150 CSV files for all the different S-values. If put to false, it will use the existing CSV files.
  - \_\_MSE\_\_ If true, the program will use the CSV files from acceleration and deceleration to compute the MSE values. It will finaly output the best S-value.

# Tuning Script
The map structure should look like the following:
- Tuning.py
- FullPlantControllerPID
  - FullPlantControllerPID(executable)
- FullPlantControllerPID_init.xml (outputFormat = 'csv')


How to run:
- When running, it will loop over all the possible K/Ti/Td-values and generate the FullPlantControllerPID_res.csv file.
- This file is then immediately used to compute the Mean Squared Error of the v and vi variable of our costfunction. 
- When this is done for all the possible values. The program will output the parameters that provided the lowest MSE value.
