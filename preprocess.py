import pandas as pd

def load_data(path):
    try:
        df = pd.read_csv(path, encoding='latin-1', header=None)

        df.columns = [
            "sentiment",
            "id",
            "date",
            "query",
            "user",
            "text"
        ]

        df = df[['sentiment','text']]

        return df

    except FileNotFoundError:
        print("Dataset file not found. Check dataset path.")