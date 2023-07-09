# cc-fraud-prevention
Credit Card Fraud: Prevention through Data Science

-- Project Status: [Completed]

## Installation


### Project Introduction/Objective
The main purpose of this project was to develop reliable models that can predict fraudulent credit card charges. This was achieved by preprocessing the data into model friendly forms including categorical treatments and splitting datetime information into separate date and time fields. The F-1 score and accuracy of each model, in training, validation, and testing groups were used to determine the best model for predicting fraudulent charges. By being able to detect fraudulent charges, we hope that detection could be achieved faster or prevented, if at all possible, in our hypothetical company.

### Partners and Contributors:
* Dave Friesen, Brianne Bell, and Michael Nguyen
* Data sourced from:
  * Grover, P., Li, Z., Liu, J., Zablocki, J., Zhou, H., Xu, J., & Cheng, A. (2022). Fraud Dataset Benchmark (primarily 3rd entry: Fraud ecommerce). Retrieved from GitHub: Amazon Research: https://github.com/amazon-research/fraud-dataset-benchmark

### Methods Used:
* Exploratory Data Analysis (EDA) and Preprocessing
  * datetime manipulations
  * pycountry_convert
  * custom profiler and EDA packages
* stratified sampling into train, validate, and test sets
* Tree-based models
  * Decision tree
  * Random Forest
  * AdaBoost classifier
* Linear type models
  * logistic regression
  * linear discriminant analysis
  * linear SVM

### Technologies
Python via Jupyter Notebook and Google Colab

## Project Description
Preprocess credit card transaction data to train various models to determine the best models. Then validate model selection with a validation trial of the models and a final test performance to see how the models perform with new data. This is to maximize finding true instances of fraudulent charges. The F-1 score was used as the main metric for determining performance. The provided data, with no missing values, had 151k entries that were split into 70% training, 20% validation, and 10% testing sets through stratified sampling based on the response variable since it had vastly different portions of fraud (9.4%) and no fraud (90.6%).

## License
The data was open-source data

## Acknowledgements
Thanks to Professor Dillon Orr and Dr. ET for the support
