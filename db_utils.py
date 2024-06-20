#will contain code to extract the data from the database
import yaml
import psycopg2
from sqlalchemy import create_engine
import pandas as pd

class RDSDatabaseConnector:  # Will contain methods used to extract data from the database
    def __init__(self, load_credentials):
        self.host = load_credentials['RDS_HOST']
        self.port = load_credentials['RDS_PORT']
        self.user = load_credentials['RDS_USER']
        self.password = load_credentials['RDS_PASSWORD']
        self.dbname = load_credentials['RDS_DATABASE']
        self.connection = None

    def create_engine(self):                      # initialises a SQLAlchemy engine from the credentials provided to the class
        conn_str = f"postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.dbname}"
        self.engine = create_engine(conn_str)
            
    def extract_loan_payments(self):            # extracts data from the RDS database and returns it as a Pandas DataFrame, stored in a table called loan_payments
        query = "SELECT * FROM loan_payments;"
        df = pd.read_sql(query, self.engine)
        return df
    
    def output_csv(self, df):               # saves the data to a csv file called 'loan_payments' on local machine
        df.to_csv('loan_payments.csv', index=False)
        
        
       
def load_credentials():                                                 # Load credentials from YAML file anf returns as dictionary
        credentials = yaml.safe_load(open('credentials.yaml', 'r'))
        return credentials
    
db_connector = RDSDatabaseConnector(load_credentials()) 
   
db_connector.create_engine()                                            # Create SQLAlchemy Engine

loan_payments_df = db_connector.extract_loan_payments()                 # Load the dataframe

print(loan_payments_df.head())                                          # Print the start(header) of the dataframe
print(loan_payments_df.shape[0])                                        # Print the number of rows in the dataframe
                        
db_connector.output_csv(loan_payments_df)

loan_payments_csv_df = pd.read_csv("loan_payments.csv")
loan_payments_csv_df.head()