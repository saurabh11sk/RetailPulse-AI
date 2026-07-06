import pandas as pd


def clean_data(df):
    df = df.copy()

    # Remove duplicate records
    df.drop_duplicates(inplace=True)

    # Remove rows with missing values
    df.dropna(inplace=True)

    # Convert Date column
    df["Date"] = pd.to_datetime(df["Date"])

    # Reset index
    df.reset_index(drop=True, inplace=True)

    return df