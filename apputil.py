import pandas as pd


# update/add code below ...
def fibonacci(n):
    """
    Compute the nth Fibonacci number using recursion with a helper function.

    Args:
        n (int): The index (non-negative) of the Fibonacci number to compute.
        
    Returns:
        int: The nth Fibonacci number.
    """
    def fib_inner(arr, count):
        # If we've reached the desired count, return the last number
        if count == n:
            return arr[-1]
        # Append next Fibonacci number to the array and remove the oldest
        arr.append(arr[-1] + arr[-2])
        arr.pop(0)
        # Recursive call with updated array and count
        return fib_inner(arr, count + 1)
    # Handling base cases, fib(0) = 0 and fib(1) = 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Start with [0, 1] and count from 1
    return fib_inner([0, 1], 1)

def to_binary(n):
    """
    Convert a positive integer to its binary representation using recursion.
    
    Args:
        n (int): A positive integer to convert to binary
        
    Returns:
        str: Binary representation of the input number as a string
    """
    # Base case: if n is 0 or 1, return it as a string
    if n == 0 or n == 1:
        return str(n)
    # Recursive case: get binary of n//2 and append n%2
    else: 
        return to_binary(n // 2) + str(n % 2)

url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'
df = pd.read_csv(url)

def task_1():
    """
    Return a list of all column names, sorted by the number of missing values.
    
    Returns:
        Column names sorted by number of missing values in ascensding order in the form of a list
    """
    
    # Clean the gender column - replace '?' with NaN
    df['gender'] = df['gender'].replace('?', pd.NA)
    
    # Count missing values for each column and sort
    missing_counts = df.isnull().sum()
    sorted_columns = missing_counts.sort_values().index.tolist()
    
    return sorted_columns


def task_2():
    """
    Return a data frame with year and total number of entries for each year.
    
    Returns:
        A DataFrame with columns 'year' and 'total_admissions'
    """
    
    # Convert date_in to datetime and extract year
    df['date_in'] = pd.to_datetime(df['date_in'], errors='coerce')
    df_year = df['date_in'].dt.year
    
    # Group by year and count entries
    result = df.groupby(df_year).size().reset_index()
    result.columns = ['year', 'total_admissions']
    
    return result


def task_3():
    """
    Return a series with average age for each gender.
    
    Returns:
        Series with gender as the index and average age as the values
    """
    # Clean the gender column, replace NA values
    gender_cleaned = df['gender'].replace(['?', 'g', 'h'], pd.NA)
    
    # Group by gender and calculate mean age
    result = df.groupby(gender_cleaned)['age'].mean()
    
    return result


def task_4():
    """
    Return a list of the 5 most common professions in order of prevalence.
    
    Returns:
        list: Top 5 most common professions as strings
    """
    
    # Count profession occurrences and get top 5
    top_professions = df['profession'].value_counts().head(5).index.tolist()
    
    return top_professions