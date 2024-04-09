from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

import pandas as pd

cali = fetch_california_housing()
Xaxis = pd.DataFrame(cali.data, columns=cali.feature_names)
Yaxis = cali.target
x_train, x_test, y_train, y_test = train_test_split(Xaxis, Yaxis, test_size=.2, random_state=37)

multipleRegress = LinearRegression()
multipleRegress.fit(x_train, y_train)
y_pred_multiple = multipleRegress.predict(x_test)
r2_multiple = r2_score(y_test, y_pred_multiple)
mseMultiple = mean_squared_error(y_test, y_pred_multiple)

enum = enumerate(Xaxis.columns)
for i, feature in enum:
    x_single = Xaxis[feature].values.reshape(-1, 1)

    x_train_single, x_test_single, y_train, y_test = train_test_split(x_single, Yaxis, test_size=.3, random_state=11)

    single_regress = LinearRegression()
    single_regress.fit(x_train_single, y_train)
    
    y_pred_single = single_regress.predict(x_test_single)
    r2_single = r2_score(y_test, y_pred_single)
    mse_single = mean_squared_error(y_test, y_pred_single)

    print("")
    print(f"Feature {i} has R^2 Score: {r2_single}")
    print(f"and has MSE Score: {mse_single}")