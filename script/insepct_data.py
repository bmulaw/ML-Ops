from pathlib import Path
import hashlib
import pandas as pd

# Open the source csv file
source = Path("data/raw/telco.csv")  # Your input path.
source_hash = hashlib.sha256(source.read_bytes()).hexdigest()

# Read the csv file into a pandas DataFrame
df = pd.read_csv(source)
print(df.shape)
print(df.dtypes)
print(df["Churn"].value_counts(dropna=False)[:10])
