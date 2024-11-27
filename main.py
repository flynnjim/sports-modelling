import pandas as pd

file_path = "E3.csv"

data = pd.read_csv(file_path)


print(data.head())

outcome_counts = data['FTR'].value_counts()

