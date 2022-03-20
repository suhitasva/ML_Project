import pandas as pd
import numpy as np


def cat_column_combine_vars(df):

	# For LandContour column replacing values 
	# other than lvl to notlvl

	LC_str_to_replace = ["Bnk", "HLS", "Low"]	

	df['LandContour'] = df['LandContour'].replace(LC_str_to_replace,\
												 "NotLvl", inplace=True) 

	# For Heating column replacing values 
	# other than GasA to Heat_othr

	HT_str_to_replace = ["GasW", "Grav", "Wall", "OthW", "Floor"]	

	df['Heating'] = df['Heating'].replace(HT_str_to_replace,\
										 "Heat_othr", inplace=True) 

	# For Electrical column replacing values 
	# other than SBrkr to Electr_othr

	EL_str_to_replace = ["FuseA", "FuseF", "FuseP", "Mix"]	

	df['Electrical'] = df['Electrical'].replace(EL_str_to_replace,\
										 		"Electr_othr", inplace=True)

	# For PavedDrive column replacing values 
	# other than Y to NP

	PV_str_to_replace = ["N", "P"]	

	df['PavedDrive'] = df['PavedDrive'].replace(PV_str_to_replace,\
										 		"NP", inplace=True) 



