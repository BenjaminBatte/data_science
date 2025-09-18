# -*- coding: utf-8 -*-
"""
Created on Sun Sep  7 19:22:37 2025

@author: bbatte
"""

"""
Lab 4: Pandas Basics
Course: ITS-836 – Data Science & Big Data Analytics
Student: Benjamin Batte
Date: Sep 14, 2025
"""
"""
---------------------------------------------------------------
Import Libraries
---------------------------------------------------------------
"""
import pandas as pd

"""
---------------------------------------------------------------
Part 1: Working with Series
---------------------------------------------------------------
"""

# Q1: Create and display a one-dimensional Series
print("\nQ1: Create and display a Pandas Series\n")
series1 = pd.Series([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
print(series1)

"""
Example of a string Series
series2 = pd.Series(["Salt Lake City", "Draper", 
                     "West Jordan", "Sandy", "Murray"])
print("\nCustom String Series\n")
print(series2)
"""

# Q2: Create two Pandas Series and perform arithmetic operations
print("\nQ2: Perform Arithmetic operations on two Pandas Series")

s1 = pd.Series([2, 4, 6, 8, 10])
s2 = pd.Series([1, 3, 5, 7, 9])

print("\nSeries 1:")
print(s1)
print("\nSeries 2:")
print(s2)

# Addition
print("\nAddition:")
print(s1 + s2)

# Subtraction
print("\nSubtraction:")
print(s1 - s2)

# Multiplication
print("\nMultiplication:")
print(s1 * s2)

# Division
print("\nDivision:")
print(s1 / s2)

"""
---------------------------------------------------------------
 Part 2: Working with the Automobile Dataset
---------------------------------------------------------------
"""

print("\nPart 2: Working with the Automobile Dataset")

# Q3: Load the dataset 'Lab 4 - Automobile.xls'
df = pd.read_excel("Lab 4 - Automobile.xls", engine="xlrd")
print("\nQ3: Automobile dataset loaded successfully!\n")

# Q4: Print first five and last five rows
print("\nQ4: First five rows of the dataset:")
print(df.head())
print("\nLast five rows of the dataset:")
print(df.tail())

# Q5: Clean dataset by removing '?', 'n.a', or NaN values
print("\nQ5: Replace '?' and 'n.a' with NaN, then drop rows with missing values")
df.replace(["?", "n.a"], pd.NA, inplace=True)
cleaned_df = df.dropna()
cleaned_df.to_csv("Automobile_cleaned.csv", index=False)
print("Cleaned dataset saved as 'Automobile_cleaned.csv'")

"""
Q6: Find the most expensive car
Convert price to float before finding maximum
"""
most_expensive = cleaned_df.loc[cleaned_df["price"].astype(float).idxmax()]
print("\nQ6: Most expensive car:")
print("Company:", most_expensive["company"])
print("Price:", most_expensive["price"])

# Q7: Print all cars manufactured by Toyota
print("\nQ7: Cars manufactured by Toyota:")
print(cleaned_df[cleaned_df["company"].str.lower() == "toyota"])

# Q8: Count total number of cars per company
print("\nQ8: Number of cars per company:")
print(cleaned_df["company"].value_counts())

# Q9: Display the most expensive car per company
print("\nQ9: Most expensive car per company:")
print(cleaned_df.groupby("company")["price"].max())

# Q10: Calculate average mileage per company
print("\nQ10: Average mileage per company:")
print(cleaned_df.groupby("company")["average-mileage"].mean())

# Q11: Sort all cars by price (ascending)
print("\nQ11: Cars sorted by price (ascending):")
print(cleaned_df.sort_values(by="price", ascending=True))

"""
---------------------------------------------------------------
 Part 3: Combining DataFrames
---------------------------------------------------------------
"""

print("\nPart 3: Combining DataFrames")

# Q12: Create two DataFrames from dictionaries and concatenate them
GermanCars = {
    "Company": ["Ford", "Mercedes", "BMV", "Audi"],
    "Price": [23845, 171995, 135925, 71400],
}

JapaneseCars = {
    "Company": ["Toyota", "Honda", "Nissan", "Mitsubishi"],
    "Price": [29995, 23600, 61500, 58900],
}

df_german = pd.DataFrame(GermanCars)
df_japanese = pd.DataFrame(JapaneseCars)

print("\nQ12: German Cars DataFrame:")
print(df_german)

print("\nJapanese Cars DataFrame:")
print(df_japanese)

# Concatenate and reset index
df_cars = pd.concat([df_german, df_japanese], ignore_index=True)
print("\nConcatenated DataFrame (German + Japanese Cars):")
print(df_cars)

# Q13: Create and merge Car_Price and Car_Horsepower DataFrames
Car_Price = {
    "Company": ["Toyota", "Honda", "BMV", "Audi"],
    "Price": [23845, 17995, 135925, 71400],
}

Car_Horsepower = {
    "Company": ["Toyota", "Honda", "BMV", "Audi"],
    "Horsepower": [141, 80, 182, 160],
}

df_price = pd.DataFrame(Car_Price)
df_hp = pd.DataFrame(Car_Horsepower)

print("\nQ13: Car_Price DataFrame:")
print(df_price)

print("\nCar_Horsepower DataFrame:")
print(df_hp)

# Merge on 'Company'
merged_df = pd.merge(df_price, df_hp, on="Company")
print("\nMerged DataFrame (Price + Horsepower):")
print(merged_df)
