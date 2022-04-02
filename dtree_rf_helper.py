import pandas as pd
import numpy as np
from math import sqrt
from sklearn import preprocessing
from sklearn.metrics import mean_squared_error, r2_score

def tree_label_encode(df):

	# Label encoding certain categorical features that display rank/order 

	col_list = ['MSSubClass','MSZoning','Street','Alley','LotShape','LandContour',\
 

 				'Utilities','LotConfig','LandSlope','Neighborhood','Condition1',\
 				'Condition2','BldgType','HouseStyle','OverallQual','OverallCond',\
 				'YearBuilt','YearRemodAdd','RoofStyle','RoofMatl','Exterior1st',\
 				'Exterior2nd','MasVnrType','ExterQual','ExterCond','Foundation',\
 				'BsmtQual','BsmtCond','BsmtExposure','BsmtFinType1','BsmtFinType2',\
 				'Heating','HeatingQC','CentralAir','Electrical','KitchenQual','Functional',\
 				'FireplaceQu','GarageType','GarageYrBlt','GarageFinish','GarageQual',\
 				'GarageCond','PavedDrive','PoolQC','Fence','MiscFeature','MoSold',\
 				'YrSold','SaleType','SaleCondition','remod_y_n']

	# Label Encoding each column one by one

	for col in col_list:
		label_encoder = preprocessing.LabelEncoder()
		df[col] = label_encoder.fit_transform(df[col])

def tree_model_res(X_train, y_train, X_test, y_test, model, show = True):

    model.fit(X_train, y_train)

    residuals = y_train - model.predict(X_train)
    train_r2 = model.score(X_train, y_train)
    test_r2 = model.score(X_test, y_test)
    train_error = 1 - train_r2
    test_error  = 1 - test_r2
    Train_RMSE = sqrt(mean_squared_error(y_train, model.predict(X_train)))
    Test_RMSE = sqrt(mean_squared_error(y_test, model.predict(X_test)))

    if show:
        print('Train R^2 is equal to %.3f' %train_r2)
        print('Test R^2 is equal to %.3f' %test_r2)
        print('Train RMSE is equal to %.3f' %Train_RMSE)
        print('Test RMSE is equal to %.3f' %Test_RMSE)
        print("The training error is: %.5f" %train_error)
        print("The test     error is: %.5f" %test_error)
    return [train_error, test_error]