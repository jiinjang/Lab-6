# CPSC-507-Lab-6
In this lab, we'll familiarize ourselves with pandas.

# Directions for submissions
Create a github repo called "Lab 6." Invite me as a collaborator to your repo. Download the repo files here as a zip file. Unzip the files and add them to your repo. Modify the files as appropriate according to the instructions. Do not change names. Commit and push changes to your repo.

# Directions for solutions
Do not change any of the code given to you (other than the comments which should absolutely be removed). I will run your code with the expected structure. Unless otherwise stated, you are welcome to add any additional lines of code or functions you find necessary. If you make changes in which your solutions do not run, you will receive no credit for that problem. For this and all subsequent labs, you should have docstrings with doctests, test files, and coverage reports included in your submission. Unless otherwise specified, all functions should end with a return of the appropriate type and not a print statement.  Refrain from using AI or other online tools.  All solutions should be yours alone.  Failure to comply will be viewed as dishonesty and treated accordingly.  Feel free to reach out with any questions you may have.

# Problem 1
Define a function called intro_to_df which takes in a dictionary of lists and creates a pandas DataFrame where each list represents a column of data, then prints the first few rows together with summary statistics.

For the following problems, download the College Major ROI dataset from kaggle using \
path=kagglehub.dataset_download("sergionefedov/college-major-roi") \
print("Path to dataset files:", path)\
and then load the dataset using pandas.  This dataset contains synthetic data for fictitious graduates of various majors and institution tiers.
# Problem 2
Let's get to know the data a bit better.  Define a function called intro_to_roi which prints the column names, the number of unique majors in the dataset, the descriptive statistics for the net_roi_usd, and the grad_id for the fictitious person with the greatest net_roi_usd.

# Problem 3
Does the tier of the institution matter?  What about major category?  Define a function called comparison_cat which takes in a label for a column with categorical data (like major or institution tier) and prints the average net_roi_usd for the unique values in that category, labeled by the value.  For example, the institution tier label, this function would print an average for mid_tier, top_public, regional, etc.

# Problem 4
Does net cost, gpa, or the selectivity score of the institution correspond to a higher ROI?  Define a function called comparison_num which takes in a label for a column with numerical data and prints the correlation between that variable at net_roi_usd.
