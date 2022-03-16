import pandas as pd
import numpy as np

def common_na_replace(df):

    # Replacing NA values in categorical variables:
    
    df['Alley'].replace(np.nan,'No alley access',inplace = True)
    df['PoolQC'].replace(np.nan,'No Pool',inplace = True)
    df['Fence'].replace(np.nan,'No Fence',inplace = True)
    df['FireplaceQu'].replace(np.nan,'No Fireplace',inplace = True)
    df['MiscFeature'].replace(np.nan,'None',inplace = True)
    df['MasVnrType'].replace(np.nan,'None',inplace = True)
  
    # Replacing NA value in Electrical column with the most 
    # common value "SBrkr"

    df['Electrical'].replace(np.nan,df['Electrical'].mode()[0],inplace = True)

    for col in ('BsmtQual', 'BsmtCond',\
                'BsmtExposure', 'BsmtFinType1',\
                'BsmtFinType2'):\
    df[col] = df[col].fillna('No Basement')

    for col in ('GarageType', 'GarageFinish',\
                'GarageQual', 'GarageCond'):\
    df[col] = df[col].fillna('No Garage')

    # Replacing NA values in numerical variables:
    
    df["LotFrontage"] = df.groupby("Neighborhood")["LotFrontage"]\
    .apply(lambda x: x.replace(np.nan,x.median()))

    df["MasVnrArea"] = df.groupby("MasVnrType")["MasVnrArea"]\
    .apply(lambda x: x.replace(np.nan,x.median()))

    # Replacing NA year values in GarageYrBlt to house YearBuilt:

    df['GarageYrBlt'].fillna(df['YearBuilt'], inplace=True)

def test_na_replace(df):

    # Replacing NA values in categorical variables:
    
    df['KitchenQual'].replace(np.nan,'TA',inplace = True)
    df['Functional'].replace(np.nan,'Typ',inplace = True)
    df['SaleType'].replace(np.nan,'Oth',inplace = True)
  
    # Replacing NA value in MSZoning, Utilities columns with the most 
    # common values

    df['MSZoning'].replace(np.nan,df['MSZoning'].mode()[0],inplace = True)
    df['Utilities'].replace(np.nan,df['Utilities'].mode()[0],inplace = True)

    for col in ('Exterior1st', 'Exterior2nd'):\
    df[col] = df[col].fillna('Other')

    for col in ('BsmtFinSF1', 'BsmtFinSF2',\
                'BsmtUnfSF', 'TotalBsmtSF',
                'BsmtFullBath','BsmtHalfBath',
                'GarageCars','GarageArea'):\
    df[col] = df[col].fillna(0)

def dtype_update(df):

    df['MSSubClass'] = df['MSSubClass'].astype(str)
    df['OverallQual'] = df['OverallQual'].astype(str)
    df['OverallCond'] = df['OverallCond'].astype(str)
    df['YearBuilt'] = df['YearBuilt'].astype(str)
    df['YearRemodAdd'] = df['YearRemodAdd'].astype(str)
    df['GarageYrBlt'] = df['GarageYrBlt'].astype(int)
    df['GarageYrBlt'] = df['GarageYrBlt'].astype(str)
    df['MoSold'] = df['MoSold'].astype(str)
    df['YrSold'] = df['YrSold'].astype(str)