# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 22:36:55 2020

@author: KIIT
"""

import glassdor_scrapper as gs
import pandas as pd
path = "D:/ML & DL projects/Youtube Videos/job_desc/chromedriver"
df = gs.get_jobs('data scientist', 1000, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index = False)