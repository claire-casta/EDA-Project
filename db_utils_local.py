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
    
    def convert_obj_to_int(self, column_name):
        self.df[column_name] = pd.to_numeric(self.df[column_name]).astype(int)
    
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
    
    def analyze_skew(self):
        """Returns the skewness of each column"""
        numeric_columns = self.df.select_dtypes(include=['number']).columns
        skewness = self.df[numeric_columns].skew()
        return skewness
    
    def analyze_skew_methods(self, columns):
        import pandas as pd
        import numpy as np
        from scipy.stats import boxcox, skew, yeojohnson
        results = []

        for column in columns:
            original_data = self.df[column].dropna()
            
            # Calculate original skewness
            original_skewness = skew(original_data)
            
            # Box-Cox transformation (only works with positive values)
            if (original_data > 0).all():
                boxcox_transformed, _ = boxcox(original_data)
                boxcox_skewness = skew(boxcox_transformed)
            else:
                boxcox_skewness = np.nan
            
            # Log transformation (only works with positive values)
            if (original_data > 0).all():
                log_transformed = np.log1p(original_data)
                log_skewness = skew(log_transformed)
            else:
                log_skewness = np.nan
            
            # Yeo-Johnson transformation (works with all values)
            yeo_transformed, _ = yeojohnson(original_data)
            yeo_skewness = skew(yeo_transformed)
            
            # Append results
            results.append({
                'Column': column,
                'Original Skewness': original_skewness,
                'Box-Cox Skewness': boxcox_skewness,
                'Log Skewness': log_skewness,
                'Yeo-Johnson Skewness': yeo_skewness
            })
    
        return pd.DataFrame(results)

    def correlation_columns(self):
        return self.df.select_dtypes(include=['number']).corr()


class DataFrameTransform:
     def __init__(self, df):
        self.df = df

     def delete_column(self, column_name):
         drop_df = self.df.drop(column_name, axis=1, inplace=True) # Drops named column
         return drop_df
     
     def delete_row_using_id(self, id_no):
        self.df.drop(self.df[self.df['id'] == id_no].index, inplace=True)
        return self.df
     
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
            # Back fill missing values within the category
            self.df.loc[mask, Value_Column] = self.df.loc[mask, Value_Column].bfill()
        
        return self.df
     
     def impute_term(self, value_column, loan_amount, int_rate, instalment):
           # Calculate loan term in months using the formula
        import math
        self.df[loan_amount] = pd.to_numeric(self.df[loan_amount])
        self.df[int_rate] = pd.to_numeric(self.df[int_rate]) / 100  # Convert annual interest rate to decimal
        self.df[instalment] = pd.to_numeric(self.df[instalment])
        import numpy as np
        def calc_loan_term_months(row):            
            if str(row[value_column]) == "<NA>":
                try:
                    row[value_column] = round(-(math.log(1 - ((row[loan_amount] * ((row[int_rate]) / 12)) / row[instalment]))) / (math.log(1 + ((row[int_rate]) / 12))))
                except Exception as e:
                    print(row["id"])
                    print(e)
                    print(row[loan_amount])
                    print(row[int_rate])
                    print(row[instalment])
                return row
            else:
                return row
        self.df = self.df.apply(calc_loan_term_months, axis=1)
        return self.df
     
     def apply_box_cox(self, column_name):
         from scipy.stats import boxcox
         transformed_data, _ = boxcox(self.df[column_name])
         self.df[column_name] = transformed_data
         return self.df[column_name]
     
     def apply_yeo_johnson(self, column_name):
        from scipy.stats import yeojohnson
        transformed_data, _ = yeojohnson(self.df[column_name])
        self.df[column_name] = transformed_data
        return self.df[column_name]
     
     def return_dataframe(self): 
         """Returns the dataframe"""                                                      
         return self.df
    
     def remove_outliers_IQR(self, column_name):
        # Calculate Q1 (25th percentile) and Q3 (75th percentile)
        Q1 = self.df[column_name].quantile(0.25)
        Q3 = self.df[column_name].quantile(0.75)
        
        # Calculate the Interquartile Range (IQR)
        IQR = Q3 - Q1
        
        # Define the bounds for outliers
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        # Filter the DataFrame to remove outliers
        filtered_df = self.df[(self.df[column_name] >= lower_bound) & (self.df[column_name] <= upper_bound)]
        
        # Update the DataFrame within the class
        self.df = filtered_df



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

     def histogram_df_columns(self):

        import numpy as np
        import seaborn as sns
        import matplotlib.pyplot as plt

        numeric_columns = self.df.select_dtypes(include=['number'])

        fig, axes = plt.subplots(5, 5, figsize=(15, 15))  
        ax = axes.flatten()

        for i, col in enumerate(numeric_columns.columns):
            sns.histplot(self.df[col], ax=ax[i], kde=True, bins=20, color='blue', alpha=0.5)
            ax[i].set_title(col)
            ax[i].set_xlabel('Value')
            ax[i].set_ylabel('Frequency')

            # Set tick labels to plain style (non-scientific notation)
            if pd.api.types.is_numeric_dtype(numeric_columns[col]):
                ax[i].get_xaxis().get_major_formatter().set_scientific(False)
                ax[i].get_yaxis().get_major_formatter().set_scientific(False)

        plt.tight_layout()
        plt.show()

     def qqplot_df_columns(self):
        import numpy as np
        import matplotlib.pyplot as plt
        from scipy import stats
        import statsmodels.api as sm

        numeric_columns = self.df.select_dtypes(include=['number'])

        fig, axes = plt.subplots(5, 5, figsize=(15, 15))  
        ax = axes.flatten()

        for i, col in enumerate(numeric_columns.columns):
            sm.qqplot(self.df[col], line='s', ax=ax[i])
            ax[i].set_title(col)
            ax[i].set_xlabel('Theoretical Quantiles')
            ax[i].set_ylabel('Sample Quantiles')
            ax[i].get_xaxis().get_major_formatter().set_scientific(False)
            ax[i].get_yaxis().get_major_formatter().set_scientific(False)

        plt.tight_layout()
        plt.show()

     def boxplot_with_scatter(self):
        import numpy as np
        import seaborn as sns
        import matplotlib.pyplot as plt

        numeric_columns = self.df.select_dtypes(include=['number'])

        fig, axes = plt.subplots(9, 3, figsize=(40, 70))  
        ax = axes.flatten()

        for i, col in enumerate(numeric_columns.columns):
            sns.boxplot(x=numeric_columns[col], ax=ax[i])
            ax[i].set_title(col)
            ax[i].set_ylabel('Value')

        plt.tight_layout()
        plt.show()

     def heatmap(self, matrix):
        import seaborn as sns
        import matplotlib.pyplot as plt

        plt.figure(figsize=(8, 6))
        heatmap = sns.heatmap(matrix, annot=False, cmap='PRGn', center=0)
        heatmap.set_title('Correlation Matrix Heatmap', fontdict={'fontsize':18}, pad=16)

        # Display the heatmap
        plt.show()