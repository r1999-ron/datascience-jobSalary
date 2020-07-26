# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 01:25:16 2020

@author: KIIT
"""

import pandas as pd
df = pd.read_csv('D:/ML & DL projects/Youtube Videos/job_desc/glassdoor_jobs.csv')

#salary parsing
df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)

df = df[df['Salary Estimate'] != '-1'] # To print the values which are not having -1
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0]) # To get rid of (Glassjor jobs)
minus_kd = salary.apply(lambda x : x.replace('K','').replace('$','')) #To get rid of 'K' from the salary and also get rid of '$'
min_hr = minus_kd.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary:', ''))
df['min_salary'] = min_hr.apply(lambda x: int(x.split('-')[0])) # To find the min salary out of total salary
df['max_salary'] = min_hr.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary + df.max_salary)/2

#Company name text only
df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] <0 else x['Company Name'][:-3], axis = 1) 

#state field
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1])
df.job_state.value_counts()
df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis = 1)
#age of company
df['age'] = df.Founded.apply(lambda x: x if x <1 else 2020 - x)

#parsing of job description

#Python
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)

#Rstudio
df['R_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)
df.R_yn.value_counts()

#Spark
df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df.spark.value_counts()

#Aws
df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df.aws.value_counts()

#Excel
df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df.excel.value_counts()

#Hadoop
df['hadoop'] = df['Job Description'].apply(lambda x: 1 if 'hadoop' in x.lower() else 0)
df.hadoop.value_counts()

df.columns

df_out = df.drop(['Unnamed: 0'], axis =1)

df_out.to_csv('salary_data_cleaned.csv',index = False)








