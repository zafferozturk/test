import pandas as pd

def load_dataset(df_path):
    df = pd.read_csv(df_path)
    return df

if __name__ == "__main__":
    df = load_dataset("data.csv")
    print(df.head())

