import pandas as pd

def intro_to_df(data):
    """
    Creates a DataFrame from a dictionary of lists
    and prints the first few rows and summary statistics.

    >>> data = {"age": [20, 21, 22], "score": [80, 90, 100]}
    >>> intro_to_df(data)  # doctest: +ELLIPSIS
       age  score
    0   20     80
    1   21     90
    2   22    100
    ...
    """
    df = pd.DataFrame(data)
    print(df.head())
    print(df.describe())
