import pandas as pd

def intro_to_df(data):
    df = pd.DataFrame(data)
    print(df.head())
    print(df.describe())


# Test
data = {
    "name": ["Amy", "Bob", "Cindy", "David", "Emma"],
    "age": [20, 21, 19, 22, 20],
    "score": [85, 90, 95, 80, 88]
}

intro_to_df(data)
