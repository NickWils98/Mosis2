# Parameter Sweep
The map structure should look like the following:
- ParameterSweep.py:
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
  - \_\_make_csv\_\_: If true, the program will fill both the acceleration and deceleration maps with 150 CSV files for all the different S-values. If put to false, it will use the existing CSV files.
  - \_\_MSE\_\_ If true, the program will re-compute the best S value (i.e. the S value with the lowest Mean Squared Error)

# Tuning Script
The map structure should look like the following:
- Tuning.py:
- FullPlantControllerPID
  - FullPlantControllerPID(executable)
- FullPlantControllerPID_init.xml (outputFormat = 'csv')


How to run:
- When running, it will loop over all the possible K-values and compute at each step the Mean Squared Error of the v and vi variable of our costfunction. 
- A FullPlantControllerPID_res.csv is also generated at each iteration. This is used to get the v and vi value at each step. After the running the program, it contains al the values of the last run so this is not very usefull after the run  