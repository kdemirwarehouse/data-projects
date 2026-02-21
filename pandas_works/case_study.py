###################################################
# List Comprehensions
###################################################
import seaborn as sns
import pandas as pd
import numpy as np
from unicodedata import category

pd.set_option("display.width",500)
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)

df = sns.load_dataset("car_crashes")
df.columns
df.info()


#TASK 1: Using List Comprehension, convert the names of the numeric variables in the car_crashes data to uppercase and add NUM to the beginning.
df.columns = ["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns]

#TASK 2: Using List Comprehension, add "FLAG" to the end of the names of the variables in the car_crashes data that do not contain "no" in their name.
df.columns = [col.lower() for col in df.columns]

df.columns = df.columns.str.replace(r"^num_", "", regex=True)

[col.upper() + "_FLAG" if not "no" in col else col.upper() for col in df.columns]

#TASK 3: Using List Comprehension, select the names of the variables that are DIFFERENT from the variable names given below and create a new dataframe.
new_cols = []

og_list = ["abbrev", "no_previous"]

new_cols = [col for col in df.columns if col not in og_list]

new_df = df[new_cols]

new_df.head()

#TASK 4: Define the Titanic dataset from the Seaborn library.
df = sns.load_dataset("titanic")
df.head()

#TASK 5: Find the number of male and female passengers in the Titanic dataset defined above.
df["sex"].value_counts()

#TASK 6: Find the number of unique values for each column.
df.nunique()

#TASK 7: Find the unique values of the pclass variable.
df["pclass"].unique()

#TASK 8: Find the number of unique values for the pclass and parch variables
df[["pclass", "parch"]].nunique()

#TASK 9: Check the data type of the embarked variable. Change its type to category. Check the data type again.
df["embarked"].dtype
df["embarked"] = df["embarked"].astype("category")
df["embarked"].dtype
df.info()

#TASK 10: Show all information for those whose embarked value is C.
df[df["embarked"] == "C"].head(10)

#TASK 11: Find the sum of null values in each variable.
df.isnull().sum()