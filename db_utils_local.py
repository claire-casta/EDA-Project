import pandas as pd

class DataTransform:
    def __init__(self, df):
        self.df = df

    def convert_column_to_category(self, column_name):
        """Converts a column to a category data type"""                                
        self.df[column_name] = self.df[column_name].astype('category')

    def convert_column_to_datetime(self, column_name): 
        """Converts a column in mm-yy to a datetime data type"""                              
        self.df[column_name] = pd.to_datetime(self.df[column_name], format='%b-%Y')

    def convert_int_column_to_float(self, column_name):
        """Converts a int column to a float data type"""                              
        self.df[column_name] = self.df[column_name].astype(float)

    def extract_nums_from_start_string(self, column_name):
        """Extracts first numbers in the string and converts to int64 data type which can handle NaN"""                          
        self.df[column_name] = self.df[column_name].str.extract(r'(\d+)').astype(float).astype('Int64')   
    
    def return_dataframe(self): 
        """Returns the dataframe"""                                                      
        return self.df

class DataframeInfo:
    def __init__(self, df):
        self.df = df

    def describe_columns(self):
         """Describe all columns in the DataFrame to check their data types"""
         return self.df.dtypes
    
    def extract_statistics(self):
        """Extract statistical values: median, standard deviation and mean (and others) from the columns and the DataFrame."""
        return self.df.describe(include=None)
    
    def count_dist_values_cat(self):
        """Count distinct values in categorical columns"""
        cat_cols = self.df.select_dtypes(include=['object', 'category'])            # Select only the categorical columns
        distinct_values = cat_cols.nunique()                                                      # Count the distinct values in each categorical column
        return distinct_values
    
    def shape_of_df(self):
        """Print out the shape of the DataFrame"""
        return self.df.shape

    def count_percent_null(self):
        """Generate a count/percentage count of NULL values in each column"""
        count_null = self.df.isnull().sum()                                         #counts the nulls in columns
        percent_null = self.df.isnull().sum() * 100 / len(self.df)                  #% of nulls in columns
        null_values = pd.DataFrame({                                                  #creates a small DataFrame to show the data for each column
                'Count Null': count_null,
                'Percentage Null': percent_null                
                })
        return null_values
    
class DataFrameTransform:
     def __init__(self, df):
        self.df = df

     def delete_column(self, column_name):
         drop_df = self.df.drop(column_name, axis=1, inplace=True) # Drops named column
         return drop_df
     
     def delete_row(self, column_name):
         drop_df = self.df.dropna(subset=[column_name], inplace=True) # Drops rows with null values in named column
         return drop_df
     
     def delete_row_if_both_null(self, column_name_1, column_name_2):
         drop_df = self.df.dropna(subset=[column_name_1, column_name_2], how='all', inplace=True) # Drops rows with null values in both named columns
         return drop_df
     
     def impute_median(self, column_name):
         median_impute = self.df[column_name].fillna(self.df[column_name].median(), inplace=True) # Replaces null value with median value
         return median_impute
     
     def impute_mode(self, column_name):
         mode_impute = self.df[column_name].fillna(self.df[column_name].mode()[0], inplace=True) # Replaces null value with mode value
         return mode_impute
     
     def impute_mean_by_category(self, Category_Column, Value_Column):
         mean_per_category = self.df.groupby(Category_Column)[Value_Column].transform('mean')  #Calculate mean values per category
         ValueColumn_filled = self.df[Value_Column].fillna(mean_per_category, inplace=True)
         return ValueColumn_filled
     
     def impute_previous_row_value(self, Category_Column, Value_Column):
        # Get unique categories
        categories = self.df[Category_Column].unique()
    
        # Loop through each category
        for category in categories:
            # Filter the DataFrame for the current category
            mask = self.df[Category_Column] == category
            # Forward fill missing values within the category
            self.df.loc[mask, Value_Column] = self.df.loc[mask, Value_Column].bfill()
        
        return self.df
     
     def impute_term(self, value_column, loan_amount, int_rate, instalment):
           # Calculate loan term in months using the formula
        import math
        loan_amount = pd.to_numeric(loan_amount, errors='coerce')
        int_rate = pd.to_numeric(int_rate, errors='coerce') / 100  # Convert annual interest rate to decimal
        instalment = pd.to_numeric(instalment, errors='coerce')

        loan_term_months = round(-(math.log(1 - ((loan_amount * ((int_rate) / 12)) / instalment))) / (math.log(1 + ((int_rate) / 12))))
        self[value_column].fillna(int(loan_term_months), inplace=True)
        return self[value_column]
     

     def return_dataframe(self): 
         """Returns the dataframe"""                                                      
         return self.df
     
class Plotter:
     def __init__(self, df):
        self.df = df

     def discrete_probability_distribution(self, column_name):
         import seaborn as sns
         import matplotlib.pyplot as plt
         plt.rc("axes.spines", top=False, right=False)

         # Calculate value counts and convert to probabilities
         probs = self.df[column_name].value_counts(normalize=True)

         # Create bar plot
         dpd=sns.barplot(y=probs.index, x=probs.values, color='r')

         plt.xlabel('Probability')
         plt.ylabel('Values')
         plt.title('Discrete Probability Distribution')
         plt.show()