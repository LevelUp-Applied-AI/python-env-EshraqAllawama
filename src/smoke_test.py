

import pandas as pd 
import pathlib

from pathlib import Path

data_path = Path(__file__).parent.parent / "data" / "sample.csv"
df = pd.read_csv(data_path)

#full data’s information 
print("Shape: ", df.shape)
print("head: ", df.head())
print("describe: ", df.describe())