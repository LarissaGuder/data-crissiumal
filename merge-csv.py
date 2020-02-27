# -*- coding: utf-8 -*-

#credited:
#https://stackoverflow.com/questions/9234560/find-all-csv-files-in-a-directory-using-python/12280052

import os
import glob
import pandas as pd
#set working directory
os.chdir("Z:\Code\data")

#find all csv files in the folder
#use glob pattern matching -> extension = 'csv'
#save result in list -> all_filenames
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
#print(all_filenames)

#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv( "data.csv", index=False, encoding='utf-8-sig')
