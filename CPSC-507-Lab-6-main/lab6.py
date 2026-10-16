
import pandas as pd
import kagglehub


def intro_to_df(data):
    """
    Creates a DataFrame from a dictionary of lists.
    Prints the first few rows and summary statistics.

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


path = kagglehub.dataset_download("sergionefedov/college-major-roi")
print("Path to dataset files:", path)

df = pd.read_csv(path + "/college_major_roi.csv")


def intro_to_roi():
    """
    Prints column names, number of unique majors,
    summary statistics for net ROI, and the grad_id
    with the highest net ROI.

    >>> intro_to_roi()  # doctest: +ELLIPSIS
    Index(['grad_id', 'major', ... 'high_roi'],
          dtype='str')
    19
    count    ...
    ...
    G015855
    """
    print(df.columns)
    print(df["major"].describe()["unique"])
    print(df["net_roi_usd"].describe())

    highest_roi = df["net_roi_usd"].max()
    print(df[df["net_roi_usd"] == highest_roi]["grad_id"].iloc[0])


def comparison_cat(label):
    """
    Prints the average net ROI for each category.

    >>> comparison_cat("institution_tier")  # doctest: +ELLIPSIS
    mid_tier 278175.229...
    top_public 328414.676...
    ...
    """
    for category in df[label].unique():
        selected = df[df[label] == category]
        print(category, selected["net_roi_usd"].mean())


def comparison_num(label):
    """
    Prints the correlation between a numerical column
    and net_roi_usd.

    >>> comparison_num("gpa")  # doctest: +ELLIPSIS
    0.020024844...
    """
    print(df[label].corr(df["net_roi_usd"]))


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
