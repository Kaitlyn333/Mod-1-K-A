import pandas as pd

Alz = pd.read_csv('Metadata and Protein Data for Module 1.csv')

for header in Alz.columns:
    print(header)