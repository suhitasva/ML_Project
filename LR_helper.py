import pandas as pd
import numpy as np
from sklearn import preprocessing

def cat_column_combine_vars(df):

	# For LandContour column replacing values 
	# other than lvl to notlvl

	LC_str_to_replace = ["Bnk", "HLS", "Low"]	
	df['LandContour'].replace(LC_str_to_replace,"NotLvl", inplace=True) 

	# For Heating column replacing values 
	# other than GasA to Heat_othr

	HT_str_to_replace = ["GasW", "Grav", "Wall", "OthW", "Floor"]	
	df['Heating'].replace(HT_str_to_replace,"Heat_othr", inplace=True) 

	# For Electrical column replacing values 
	# other than SBrkr to Electr_othr

	EL_str_to_replace = ["FuseA", "FuseF", "FuseP", "Mix"]	
	df['Electrical'].replace(EL_str_to_replace,"Electr_othr", inplace=True)

	# For PavedDrive column replacing values 
	# other than Y to NP

	PV_str_to_replace = ["N", "P"]	
	df['PavedDrive'].replace(PV_str_to_replace,"NP", inplace=True) 

def num_new_features(df):

	# Combining total type 1 and type 2 basement area 
	# to BsmtFinSF (total finished basement square feet)

	df['BsmtFinSF'] = df['BsmtFinSF1'] + df['BsmtFinSF2']

	# Age of house when sold

	df['sold_age'] = df['YrSold'].astype(int) - df['YearBuilt'].astype(int)

	# Creating column that lists total full and total half baths in the house

	df['Total_Halfbaths'] = df['BsmtHalfBath'] + df['HalfBath']	
	df['Total_Fullbaths'] = df['BsmtFullBath'] + df['FullBath'] 

	# Creating column that sums total enclosed porch sq feet area

	df['Encl_Porch_tot'] = df['EnclosedPorch'] + df['3SsnPorch'] + df['ScreenPorch']
	
	# Creating column that lists total usable space

	df['Usable_Space'] = df['BsmtFinSF'] + df['GrLivArea']\
						 + df['1stFlrSF'] + df['2ndFlrSF'] 

def label_encode_features(df):

	# Label encoding certain categorical features that display rank/order 

	col_list = ['LotShape', 'LandSlope', 'ExterQual', 'ExterCond', 'BsmtQual',\
				'BsmtCond', 'BsmtExposure','BsmtFinType1', 'BsmtFinType2',\
				'HeatingQC','KitchenQual','FireplaceQu','GarageQual','GarageCond',\
				'PoolQC']

	# Label Encoding each column one by one

	for col in col_list:
		label_encoder = preprocessing.LabelEncoder()
		df[col] = label_encoder.fit_transform(df[col])
