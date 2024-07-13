# Exploratory Data Analysis Project - Customer Loans in Finance

## Project Brief
You currently work for a large financial institution, where managing loans is a critical component of business operations.

To ensure informed decisions are made about loan approvals and risk is efficiently managed, your task is to gain a comprehensive understanding of the loan portfolio data.

Your task is to perform exploratory data analysis on the loan portfolio, using various statistical and data visualisation techniques to uncover patterns, relationships, and anomalies in the loan data.

This information will enable the business to make more informed decisions about loan approvals, pricing, and risk management.

By conducting exploratory data analysis on the loan data, you aim to gain a deeper understanding of the risk and return associated with the business' loans.

Ultimately, your goal is to improve the performance and profitability of the loan portfolio.

## Project Description
A description of the project: what it does, the aim of the project, and what you learned.

This project takes a financial loan dataset in .csv file format and exploratory data analysis is performed to gain a deeper understanding of the dataset.

The exploratory data analysis has several steps built into the project:
1. Extract the data from the cloud.
2. Initial data exploration to gain an overview of the dataframe.
3. Convert column to the correct format
4. Removing or imputing missing (null value) data
5. Perform transformations on skewed data columns
6. Identifying and removing outliers from the data
7. Identifying and dropping overly correlated columns
8. Analysis and visualisation to draw deeper insights


## Installation & Usage instructions

Download the repository to your local machine.
The original downloaded dataframe is contained within the loan_payments.csv file, if you wish to inspect this.
Open the following files in this order:
1. loan_payments_queries.ipynb
    - This document runs through the data preparation for the exploratory data analysis, explaining each step in turn and uses code that can be found in db_utils.py and db_utils_local.py. It also produces two copies of the dataframe; mod_loan_payments_pre_skew.csv and mod_loan_payments_post_skew_corr.csv, as well as a correlation_matrix.csv file.
2. analysis_and_visualisations.ipynb
    - This document runs through the analysis of the dataframe with visualisation throughout. It explains each step in the process and discusses the outcomes along the way. 

## File structure of the project
EDA Project
 - analysis_and_visualisations.ipynb (Notebook 2 for this EDA project detailing the analysis of dataframe)
 - correlation matrix.csv (Output by loan_payments_queries.ipynb to allow a more detailed analysis of correlated columns)
 - db_utils_local.py (Code referenced by loan_payments_queries.ipynb for use on the local machine)
 - db_utils.py (Code referenced by loan_payments_queries.ipynb to extract data from the database and download it to a csv file on the local machine)
 - loan_payments_queries.ipynb (Notebook 1 for this EDA project detailing the data preparation before analysis)
 - loan_payments.csv (the original csv file downloaded from the database)
 - mod_loan_payments_post_skew_corr.csv (Output by loan_payments_queries.ipynb to allow further analysis of the dataframe after correction for skew)
 - mod_loan_payments_pre_skew.csv (Output by loan_payments_queries.ipynb to allow further analysis of the dataframe without the alterations to the data produced by skew corrections)
 - README.md (information document to aid understanding of the contents of his repository)
 - requirements.txt (contains a list of all the imports required for the code in this project to work)

## License information
This work is licenced under the MIT Licence as outlined below.

MIT License

Copyright (c) 2024 Claire Castanheira

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.