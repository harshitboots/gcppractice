import pandas as pd
import os


def write_to_parquet(data, file_path="data/users.parquet"):
    """
    Write transformed data to Parquet file.
    """

    # Ensure data folder exists
    os.makedirs("data", exist_ok=True)

    df = pd.DataFrame(data)

    df.to_parquet(file_path, index=False)

    print(f"Parquet file written to {file_path}")