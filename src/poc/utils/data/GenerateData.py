import pandas as pd
import random


def generate_data(num_records, columns):
    """
    Generate a Pandas DataFrame.

    Parameters
    ----------
    num_records : int
        Number of records to generate.

    columns : dict
        Column definition.

        Examples:
        {
            "Year": [2022, 2023, 2024, 2025],
            "Quarter": ["Q1", "Q2", "Q3", "Q4"],
            "Product": ["Software", "Hardware"],
            "ROI": (50, 90)
        }

        list/tuple with multiple values -> categorical/random choice
        tuple with 2 numeric values -> random numeric range

    Returns
    -------
    pandas.DataFrame
    """

    data = {}

    for column_name, data_range in columns.items():

        # Numeric range
        if (
            isinstance(data_range, tuple)
            and len(data_range) == 2
            and all(isinstance(x, (int, float)) for x in data_range)
        ):
            data[column_name] = [
                (
                    random.randint(*data_range)
                    if all(isinstance(x, int) for x in data_range)
                    else random.uniform(*data_range)
                )
                for _ in range(num_records)
            ]

        # List / categorical values
        else:
            data[column_name] = [random.choice(data_range) for _ in range(num_records)]

    return pd.DataFrame(data)
