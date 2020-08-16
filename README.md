# Data Science Salary Estimator

* Created a tool that estimates data science salaries (MAE ~ $ 11K) to help data scientists negotiate their income when they get a job.
* Scraped over 1000 job descriptions from glassdoor using python and selenium
* Engineered features from the text of each job description to quantify the value companies put on python, excel, aws, and spark.
* Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model.
* Built a client facing API using flask.

# Web Scraping
Tweaked the web scraper github repo (above) to scrape 1000 job postings from glassdoor.com. With each job, we got the following:
  * Job Title
  * Salary estimate
  * Job Description
  * Rating
  * Company
  * Location
  * Company Headquarters
  * Company Size
  * Company Founded Date
  * Type of Ownership
  * Industry
  * Sector
  * Revenue
  * Competitors
 
## Data Cleaning
Data cleaning is an extremely important and often overlooked step in the data science lifecycle. Python has some handy functions that allow us to parse and replace data relatively easily. We can also use regular expressions to do this but here used lambda functions because I think that this is the simplest approach.

The first thing that we clean is the data science salary. We need to make sure that it is numeric because we are using that as our dependent variable. We also want to go through and do some light feature engineering. We can get some info about the state of the job postings and the nature of the job postings themselves.

I went through and looked to see if the postings had python, r-studio, spark, aws, or excel listed and added those as features. 

## EDA 
I looked at the distributions of the data and the value counts for the various categorical variables. Below are a few highlights from the pivot tables.
![salary_by_job_title](https://user-images.githubusercontent.com/55063393/90340414-aaa38680-e015-11ea-9e15-c1e1638c3354.PNG)

![positions_by_state](https://user-images.githubusercontent.com/55063393/90340438-d0309000-e015-11ea-9182-f1f7a709c181.png)  ![correlation_visual](https://user-images.githubusercontent.com/55063393/90340442-d45cad80-e015-11ea-9b4c-5f4124d9d7d2.png)
  
## Model Building Stage:
  First, I transformed the categorical variables into dummy variables. I also split the data into train and tests sets with a test size of 20%.

I tried three different models and evaluated them using Mean Absolute Error. I chose MAE because it is relatively easy to interpret and outliers aren’t particularly bad in for this type of model.

I tried three different models:
  * Multiple Linear Regression – Baseline for the model 
  * Lasso Regression – Because of the sparse data from the many categorical variables, I thought a normalized regression like lasso would be effective.
  * Random Forest – Again, with the sparsity associated with the data, I thought that this would be a good fit.
 
## Model Performance:
  The Random Forest model far outperformed the other approaches on the test and validation sets.
     * Random Forest : MAE = 11.22
     * Linear Regression: MAE = 18.86
     * Ridge Regression: MAE = 19.67

## Productionization:
   In this step, I built a flask API endpoint that was hosted on a local webserver . The API endpoint takes in a request with a list of values from a job listing and returns an estimated salary.

