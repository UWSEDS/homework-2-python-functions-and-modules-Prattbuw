# Read the data in a csv file from a URL into a pandas DataFrame
# Brandon Pratt
# 10/14/2019

# Data description:
# Hospital charges for hospitals that receive Medicare Inpatient Prospective Payment System
# See https://www.cms.gov/Research-Statistics-Data-and-Systems/Statistics-Trends-and-Reports/Medicare-Provider-Charge-Data/Inpatient2011.html
# for more information about the data

# Import pandas package
import pandas as pd

# define url associated with dataset
url="https://data.cms.gov/api/views/97k6-zzx3/rows.csv?accessType=DOWNLOAD"

# load csv file into a dataframe
df=pd.read_csv(url)

# display dataframe
#print(df)

# Obtain a list of column names
col_names=list(df)
#print(col_names)

# Create a function that inputs a pandas dataframe and a list of column names
# returns true if the conditions are satisfied
# define a satisfactory value determining if all conditions are satisified
sat_value=0 # initialized

def test_create_dataframe(dataframe,column_names,sat_value):
    # Determine if the data contained in the dataframe satisfys the following conditions:

    # The DataFrame contains only the columns that you specified as the second argument
    # Obtain all of the column names and see if they are all in the dataframe columns
    if pd.Series(column_names).isin(dataframe.columns).all():
    #if column_names[0] in dataframe.columns:
        print("DataFrame contains columns: True")
        sat_value=sat_value+1
    else:
        print("DataFrame contains columns: False")

    # The values in each column have the same python type
    # Determine the dtypes of each column
    col_types=dataframe.dtypes
    comparison_number=0 #
    # compare the first column type to the rest and if it doesn't match then break out of the for loop and signify False
    for type in col_types:
        # increase comparison number for each iteration
        comparison_number=comparison_number+1

        # Check to see if column types are different
        if type != col_types[0]:
            print("DataFrame column types are not the same: False")
            break
        # Check to see if the column types are the same
        else:
            # if the first and last column types are the same then all of the column types are the same because otherwise the code would break
            if comparison_number == len(col_types):
                print("DataFrame column types are the same: True")
                sat_value=sat_value+1


    # There are at least 10 rows in the DataFrame
    if len(dataframe.index) >= 10:
        print("DataFrame has more than 10 rows: True")
        sat_value=sat_value+1
    else:
        print("DataFrame does not have more than 10 rows: False")

    # if all of the conditions above are true then the satisfactory tag returns True otherwise it returns False
    Satisfactory_Tag=0
    if sat_value==3:
        Satisfactory_Tag=True
    else:
        Satisfactory_Tag=False

    return Satisfactory_Tag

# test function
Satisfactory_Tag=test_create_dataframe(df,col_names,sat_value)

print("All tested conditions hold:",Satisfactory_Tag)
