###################################
#Pandas Series
###################################
import pandas as pd

s = pd.Series([10, 77, 12, 4, 5])
type(s)
s.index
s.dtype
s.size
s.ndim
s.values
type(s.values)
s.head()
s.tail(3)
#####################################
#Reading Data

import pandas as pd

def load():
    data = pd.read_csv("IMDB Dataset.csv")
    return data

df = load()

df.head()
###################################
#Quick look at Data
import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
df.head()
df.tail()
df.shape
df.info()
df.columns
df.index
df.describe().T
df.isnull().values.any()
df.isnull().sum()
df["sex"].head()
df["sex"].value_counts()
#####################################
#Selection in Pandas
import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
df.head()
df.index
df[0:13]
df.drop(0,axis=0).head()#satırlardan 0.satırı sildim

delete_indexes=[1, 3, 5, 7]
df.drop(delete_indexes, axis=0).head()

#with inplace=True or with df = df.drop(delete_indexes, axis=0).head()
#We can make it permanent

#Converting Variable to Index
#Ways to choose the variable
df["Age"].head()
df.age.head()

df.index = df["age"]

df.drop("age", axis=1).head()
df.drop("age", axis=1,inplace=True)
df.head()

#Converting Index to Variable
df["age"]
#First Way
df["age"] = df.index

df.drop("age", axis=1,inplace=True)
df.head()

#Second Way
df.reset_index().head()
#indexte yer alan değişkeni once siler sonra sutunlara ekler

df = df.reset_index()#permanent
df.head()
####################################################
#Değişkenler Üzerinde İşlemler
import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns',None) #sutunlari gosterirken ... isaretlerini siler
df = sns.load_dataset("titanic")
df.head()

"age" in df
#bu değişken bu verisetinin içerisinde var mı?

df["age"].head()
df.age.head()
type(df.age.head())

#df olarak kalmasını istiyorsan:
df[["age"]].head()
type(df[["age"]].head())

#birden fazla degisken secmek icin iki koseli parantez ac ve listeyi gonder
df[["age", "alive"]]

col_names = ["age", "adult_male", "alive"]
df[col_names]

#tabloya yeni degisken ekleme
df["age2"] = df["age"] ** 2
df.head()
df["age3"] = df["age"] / df["age2"]

df.drop("age3",axis=1).head()

df.drop(col_names, axis=1).head()

df.loc[:, ~df.columns.str.contains("age")].head() #Returns what is outside the age variable

#################################
#iloc % loc
import pandas as pd
import seaborn as sns
pd.set_option("display.max_columns",None)
df = sns.load_dataset("titanic")
df.head()

#iloc --> integer based selection
df.iloc[0:3]
df.iloc[0, 0]

#loc: label based selection
df.loc[0:3]
#including 3

df.iloc[0:3,0:3]#we couldn't fetch variable age
df.loc[0:3,"age"]
#We used the loc function to fetch the variable age

#for multi variables
col_names = ["age", "embarked", "alive"]
df.loc[0:3, col_names]
######################################
#Conditional Selection
import pandas as pd
import seaborn as sns
pd.set_option("display.max_columns", None)
df = sns.load_dataset("titanic")
df.head()

df[df["age"]>50].head()
df[df["age"]>50]["age"].count()#NUMBER OF PEOPLE OVER THE AGE OF 50

df.loc[df["age"] > 50, ["class", "age"]].head()
#I show the class of those over the age of 50

#If you are going to use more than one condition, do not forget to use parentheses
df.loc[(df["age"] > 50) & (df["sex"] == "male"), ["age", "class"]].head()


df["embark_town"].value_counts()

df_new = df.loc[(df["age"] > 50)
       & (df["sex"] == "male")
       & ((df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton")),
        ["age", "class","embark_town"]]

df_new["embark_town"].value_counts()

###########################################
#Aggregation & Grouping
import pandas as pd
import numpy as np
pd.set_option("display.max_columns",None)
df = sns.load_dataset("titanic")
df.head()

df["age"].mean

#age mean based sex
df.groupby("sex")["age"].mean()
#or
df.groupby("sex").agg({"age":["mean","sum"]})

df.groupby("sex").agg({"age":"mean"})
df.groupby("sex").agg({"age":["mean","sum"]})

df.groupby("sex").agg({"age":["mean", "sum"],
                      "survived":"mean"})
#74% of the women who boarded the ship survived, while 18% of the men

df.groupby(["sex","embark_town"]).agg({"age":["mean"],
                                       "survived":"mean"})

#gemiye binen yolcuların hayatta kalma durumlarını cinsiyet,
#yaş ve sınıfa gore belirliyoruz
df.groupby(["sex", "embark_town", "class"]).agg({"age":["mean"],
                                                "survived":"mean"})

df.groupby(["sex", "embark_town", "class"]).agg({
    "age":["mean"],
    "survived":"mean",
    "sex":"count"
})