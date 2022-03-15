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