#will contain code to extract the data from the database
import yaml
import psycopg2
from sqlalchemy import create_engine
import pandas as pd

loan_payments_csv_df = pd.read_csv("loan_payments.csv")
#print(loan_payments_csv_df.head())
shape = loan_payments_csv_df.shape
print(f'This dataset has {shape[0]} rows and {shape[1]} columns')