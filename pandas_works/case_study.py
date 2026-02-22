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

#TASK12: Display all information of females whose age is lower than 30.
df[(df["sex"] == "female") & (df["age"] < 30 )].head()

#TASK13: Display the information of passengers whose Fare is greater than 500 or whose age is greater than 70.
df[(df["fare"] > 500) | (df["age"] > 70)].head()

#TASK14: Find sum of null values in each ariable
df.isnull().sum()

#TASK15: Drop the who variable from dataframe
df.drop("who", axis=1,inplace=True,errors="ignore")

#TASK16: Fill in the blank values in the deck variable with the most repetitive value (mode) of the deck variable.
df["deck"] = df["deck"].fillna(df["deck"].mode()[0])

df["deck"].isnull().sum()

#TASK17: Fill in the blank values in the age variable with the median of age variable
df["age"] = df["age"].fillna(df["age"].median())
df["age"].isnull().sum()

#TASK18: Find the sum, count, mean values in the breakdown of the Pclass and Gender variables of the survived variable.
df.groupby(["pclass","sex"]).agg({"survived": ["sum", "count", "mean"]})

#TASK19: Write a function that assigns 1 to those under the age of 30 and 0 to those who are 30 or older.
#Using the function you wrote, create a variable named age_flag in the Titanic dataset. (Use the apply and lambda structures)

def age_30(age):
    if age < 30:
        return 1
    else:
        return 0

df["age_flag"] = df["age"].apply(lambda x: age_30(x))

# TASK20: Define Tips dataset from Seaborn library.
df = sns.load_dataset("tips")
df.head()
df.shape

#TASK21: Find the sum, min, max and mean of total_bill values based Time categories
df.groupby(["time"]).agg({"total_bill": ["sum", "min", "max", "mean"]})

#TASK22: Find the sum, min, max and mean of total_bill values based days and time
df.groupby(["time", "day"]).agg({"total_bill": ["mean", "sum", "min", "max"]})

#TASK23: Find the sum, minimum, maximum, and average of the total_bill and tip values for Lunch time and female customers by day.
df[(df["time"] == "Lunch") & (df["sex"] == "Female")].groupby("day").agg({"total_bill": ["mean", "sum", "max", "min"]})

#TASK24: What is the average of orders with size less than 3 and  total bill greater than 10?
df.loc[(df["size"] < 3) & (df["total_bill"] > 10), "total_bill"].mean()

#TASK25: Create a new variable named total_bill_tip_sum. Let each customer give the sum of the totalbill and tip paid.
df["total_bill_tip_sum"] = df["total_bill"] + df["tip"]
