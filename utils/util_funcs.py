import pandas as pd
import os

path = os.path.dirname(os.getcwd())


# Create a function to get the columns
def build_columns_for_df(df: pd.DataFrame) -> list:
    column_names = [i[:1][0] for i in df.columns.values]
    column_names.insert(0, 'Date')
    return column_names


# function to save the data into a csv file
def save_to_csv(df: pd.DataFrame, ticker_name: str) -> None:
    df.to_csv(f'{path}/files/{ticker_name}_historical_data.csv', header=False)


# function to read the new csv file, set index Date
def read_from_csv(ticker_name: str, column_names: list[str]) -> pd.DataFrame:
    return pd.read_csv(f'{path}/files/{ticker_name}_historical_data.csv', names=column_names).set_index('Date')

