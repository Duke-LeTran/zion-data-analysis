#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 21:18:46 2018

@author: dukeletran
"""
#
#
# US Geological Survey, Water Resources Data
# retrieved: 2018-09-20 00:06:46 EDT      (sdww02)
#
# This file contains USGS Surface-Water Daily Statistics
#
# Note:The statistics generated from  this site are based on approved daily-mean data and may not match those published by the USGS in official publications.
# The user is responsible for assessment and use of statistics from this site.
# For more details on why the statistics may not match, visit https://waterdata.usgs.gov/nwis/?dv_statistics_disclaimer.
#
# ** No Incomplete data have been used for statistical calculation
#
# This file includes the following columns:
#
#
# agency_cd  agency code
# site_no    USGS site number
#
#
# Sites in this file include:
# USGS 09405500 NORTH FORK VIRGIN RIVER NEAR SPRINGDALE, UT
# 
# Explanation of Parameter Code and ts_id used in the Statistics Data 
# parameter_cd	Parameter Name					ts_id	Location Name
# 00060		Discharge, cubic feet per second		143263	
#
# Data heading explanations.
# begin_yr_dt ... First complete year of data of daily mean values for this day.
# end_yr_dt   ... Last complete year of data of daily mean values for this day.
# max_va      ... Maximum of daily mean values for this day.
# min_va      ... Minimum of daily mean values for this day.
# mean_va     ... Mean of daily mean values for this day.
# p05_va      ... 05 percentile of daily mean values for this day.
# p10_va      ... 10 percentile of daily mean values for this day.
# p20_va      ... 20 percentile of daily mean values for this day.
# p25_va      ... 25 percentile of daily mean values for this day.
# p50_va      ... 50 percentile (median) of daily mean values for this day.
# p75_va      ... 75 percentile of daily mean values for this day.
# p80_va      ... 80 percentile of daily mean values for this day.
# p90_va      ... 90 percentile of daily mean values for this day.
# p95_va      ... 95 percentile of daily mean values for this day.
#
#

import numpy as np
import pandas as pd
import seaborn as sns

# I. Read Data
df = pd.read_csv('input/dvstat-data-only.csv', sep='\t')

# II. Filter Data
df_sept = df[df['month_nu'] == 9] # september only data
df_09_22 = df_sept.iloc[266] # september 22nd only data

# III. Data Visualization for fun
## A. Sept 22nd row, barplot
s = df.iloc[265][14:]
sns.barplot(x=s.index, y=s)

## B. 
df2 = df[['month_nu', 'day_nu', 'p50_va']]

sns.lmplot(x='day_nu', 
           y='p50_va', 
           col='month_nu', 
           hue='month_nu', 
           col_wrap=3, data=df2)

# grab only 95 percentile daily mean values for this day
df3 = df[['month_nu', 'day_nu', 'p95_va']]

sns.lmplot(x='day_nu', 
           y='p95_va', 
           col='month_nu', 
           hue='month_nu', 
           col_wrap=3, data=df3)

