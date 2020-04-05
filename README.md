# RUL Prediction for Li-ion Battries

## Dataset
* [Nasa Dataset for RUL of Li-ion](https://ti.arc.nasa.gov/tech/dash/groups/pcoe/prognostic-data-repository/#battery)

## Features Extraction

- In the given dataset every cycle is represented by set of arrays.
- Out of which Temperature, VoltageMeasured, VoltageLoad seems to best describe the cycle
- These values are measured at different time points which are represented in Time array
- Rather than using entire array for training we can extract **critical time points for each of the features** and train the model on these **critical time points**
- Only using these **critical points** will reduce the training time and reduce the noise in data

## Critical Points for a given cycle
**TEMPERATURE_MEASURED**
- Time at highest temperature

**VOLTAGE_MEASURED**
- Time at lowest Voltage
  
**VOLTAGE_LOAD**
- First time it drops below 1 volt after 1500 time

## Plot of Critical Values and Capacity v/s Cycles
![Battery B0005](/CriticalValues.png)
* Above is the plot for battery B0005
* Cycle number is representing the age of battery and with increasing cycle number (age) **battery's capacity** decreases and **linearly critcal values are also decreasing**
* Thus there is a strong linear co-relational in the data
* Thus we used a **Regression Model**

## Regression Model
### Using Dataset from 1 **Battery 005**
* **75%** of discharge cycles are used as training data
* **25%** of discharge cycles are used as testing data
* Accuracy Obtained **99.9903768373228**
* Average difference between Predicted and Real Capacity **0.0001504458509620327**

### Using Dataset from 3 **Batteries 005, 006 and 007**
* A new dataset was fromed by mixing cycles from this battries
* **75%** of discharge cycles are used as training data
* **25%** of discharge cycles are used as testing data
* Accuracy Obtained **99.15812921489568**
* Average difference between Predicted and Real Capacity **0.013404734961093144**