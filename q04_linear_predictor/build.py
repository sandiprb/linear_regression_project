# Default Imports
from greyatomlib.linear_regression.q01_load_data.build import load_data
from greyatomlib.linear_regression.q02_data_splitter.build import data_splitter
from greyatomlib.linear_regression.q03_linear_regression.build import linear_regression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


dataframe = load_data('data/house_prices_multivariate.csv')
X, y = data_splitter(dataframe)
linear_model = linear_regression(X, y)


def linear_predictor(fit, X, y):
    y_pred = fit.predict(X)
    _mean_squared_error = mean_squared_error(y,y_pred)
    _mean_absolute_error = mean_absolute_error(y,y_pred)
    _r_square = r2_score(y,y_pred)

    return y_pred, _mean_squared_error, _mean_absolute_error, _r_square
