#!/usr/bin/env python

#This merge multiple Excel files with varied rows into one Excel file in pandas.
#This Python pandas script created by Tommas Huang

import pandas as pd 
lab = pd.read_excel('/Users/TommasHuang/Desktop/test1.xls', sheet_name='lab') 
drugs = pd.read_excel('/Users/TommasHuang/Desktop/test2.xls', sheet_name='drugs') 
# Because sheet_name is difference, and then can change sheet_name and Excel path for read Excel.

drugs['GrpCount'] = (drugs.groupby(['ID'])).cumcount()
lab['GrpCount'] = (lab.groupby(['ID'])).cumcount()
#Because sheet_name is difference, and then can change sheet_name and group by column.

merged_data = pd.merge(drugs, lab, on=['ID', 'GrpCount'], how='left').drop(['GrpCount'], axis=1)
#Start to merge data, need to change sheet_name, group by column. Start merge data From left column or right column.

merged_data.to_excel('/Users/TommasHuang/Desktop/merged_data.xls')
# Chang save merged Excel sheet data path.