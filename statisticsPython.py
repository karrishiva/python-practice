import pandas as pd

titanic = pd.read_csv("./statisticsPython.csv")

# print(titanic.head())


# What is the average age of the Titanic passengers?

average_age = titanic["Age"].mean()

# What is the median age and ticket fare price of the Titanic passengers?

fair_age_fare_price = titanic[["Age", "Fare"]].median()

# By using aggregation method

titanic_agg = titanic.agg(
    {
        "Age" : ["min", "max", "median", "skew"],
        "Fare" : ["min", "max", "median", "mean"],
    }
)


# What is the average age for male versus female Titanic passengers?
average_male_female = titanic[["Sex", "Age"]].groupby("Sex").mean()

num_all = titanic.groupby("Sex").mean(numeric_only=True)

# What is the mean ticket fare price for each of the sex and cabin class combinations?
sex_cabin = titanic.groupby(["Sex", "Pclass"])["Fare"].mean()

# What is the number of passengers in each of the cabin classes?
cabin_class = titanic["Pclass"].value_counts()






print(sex_cabin)