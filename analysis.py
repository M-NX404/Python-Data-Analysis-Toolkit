# Python-Data-Analysis-Toolkit
# Author: Mainak Dhanantari
# Description: Basic data analysis using Python

import pandas as pd
import statistics as stats

def load_data(file_path):
    """Load CSV data into a DataFrame"""
    return pd.read_csv(file_path)

def basic_statistics(data):
    """Calculate basic statistics for numeric columns"""
    result = {}
    for column in data.select_dtypes(include='number').columns:
        result[column] = {
            "Mean": data[column].mean(),
            "Median": data[column].median(),
            "Mode": data[column].mode()[0],
            "Standard Deviation": data[column].std()
        }
    return result

def main():
    data = load_data("../data/sample_data.csv")
    stats_result = basic_statistics(data)

    print("Basic Statistical Analysis")
    print("--------------------------")
    for col, values in stats_result.items():
        print(f"\nColumn: {col}")
        for stat, val in values.items():
            print(f"{stat}: {val:.2f}")

if __name__ == "__main__":
    main()
