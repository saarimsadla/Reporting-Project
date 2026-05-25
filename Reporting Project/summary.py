import pandas as pd


def calculate_Initial_Stats(df):
    print("Generating Summary for Initial Stats.")

    # Total Rows
    total_rows = df.shape[0]

    # Duplicated Rows
    duplicated_rows = df.duplicated().sum()

    initial_Stats = {
        "Total Rows": total_rows,
        "Duplicated Rows": duplicated_rows
    }

    # Columns to process differently
    special_columns = ['loginid', 'unitType', 'state', 'accountEndDate', 'printOrEmail', 'email']

    # for col in df.columns:
    #     # Check if the column needs special processing
    #     if col in special_columns:
    #         missing_values = df[col].isnull().sum()
    #         unique_values = df[col].nunique()
    #         initial_Stats[f"{col} - Missing Values"] = missing_values
    #         initial_Stats[f"{col} - Unique Values"] = unique_values
    #     else:
    #         missing_values = df[col].isnull().sum()
    #         min_value = df[col].min()
    #         max_value = df[col].max()
    #         # fishy
    #         std = df[col].std()
    #         initial_Stats[f"{col} - Missing Values"] = missing_values
    #         initial_Stats[f"{col} - Min Value"] = min_value
    #         initial_Stats[f"{col} - Max Value"] = max_value
    #         initial_Stats[f"{col} - Standard Deviation"] = std

    for col in df.columns:
        # Check if the column needs special processing
        if col in special_columns:
            missing_values = df[col].isnull().sum()
            unique_values = df[col].nunique()
            initial_Stats[f"{col} - Missing Values"] = missing_values
            initial_Stats[f"{col} - Unique Values"] = unique_values
        else:
            missing_values = df[col].isnull().sum()
            min_value = df[col].min()
            max_value = df[col].max()
            std = df[col][pd.to_numeric(df[col], errors='coerce') == df[col]].std()  # Exclude non-numeric values
            initial_Stats[f"{col} - Missing Values"] = missing_values
            initial_Stats[f"{col} - Min Value"] = min_value
            initial_Stats[f"{col} - Max Value"] = max_value
            initial_Stats[f"{col} - Standard Deviation"] = std

    print("                                     Generated Summary for Initial Stats.")
    return initial_Stats


def generate_summary_stats(df, part):
    print("Numeric Columns Summary - Part " + str(part) + " processing.")
    summary_stats = {}
    columns_to_generate_stats = []
    if part == 1:
        columns_to_generate_stats = ['_id', 'custid', 'hFootage', 'hYearconstruct', 'bedrooms', 'hOccupants', 'zip',
                                     'mailingZip', 'latitude']
    else:
        columns_to_generate_stats = ['longitude', 'purchasedSqft', 'userSqft', 'imputedSqft', 'isValidationError',
                                     'Duplicated Rows']

    if columns_to_generate_stats:
        for col in columns_to_generate_stats:
            # Check if the column exists in the DataFrame
            if col in df.columns:
                # Convert the column to numeric type if possible
                df[col] = pd.to_numeric(df[col], errors='coerce')
                stats = {
                    'Min': df[col].min(),
                    '1%': df[col].quantile(0.01),
                    '10%': df[col].quantile(0.10),
                    '25%': df[col].quantile(0.25),
                    'Median': df[col].median(),
                    '75%': df[col].quantile(0.75),
                    '99%': df[col].quantile(0.99),
                    'Max': df[col].max(),
                    'Mean': df[col].mean(),
                    'Std': df[col].std(),
                    'Negative Values': (df[col] < 0).sum(),
                    'Positive Values': (df[col] > 0).sum(),
                    'Zeroes': (df[col] == 0).sum(),
                    'Missing Values': df[col].isna().sum()
                }
                summary_stats[col] = stats
            #else:
                #summary_stats[col] = None
                # print(f"Column '{col}' not found in DataFrame.")
    else:
        print("ERROR")
    # summary_stats_df = pd.DataFrame(summary_stats)
    print("                                            Numeric Columns Summary - Part " + str(part) + " processed.")
    return summary_stats


def generate_Other_Columns_Summary(df):
    print("Generating Summary for Other Columns.")

    other_columns_stats = {}

    # List of columns for which required statistics are to be calculated
    other_processing_columns = ['loginid', 'unitType', 'state', 'accountEndDate', 'printOrEmail', 'email']

    for col in other_processing_columns:
        # Calculate missing values
        missing_values = df[col].isna().sum()

        # Calculate unique values
        unique_values = df[col].nunique()

        # Calculate most common value and its frequency
        if unique_values > 0:
            most_common_value = df[col].mode()[0]
            frequency_most_common = df[col].value_counts()[most_common_value]
        else:
            most_common_value = None
            frequency_most_common = None

        # Calculate duplicate values
        duplicate_values = df.duplicated(subset=[col]).sum()

        # Store the statistics in a dictionary
        other_columns_stats[col] = {
            'Missing Values': missing_values,
            'Unique Values': unique_values,
            'Most Common Value': most_common_value,
            'Frequency of Most Common Value': frequency_most_common,
            'Duplicate Values': duplicate_values
        }

    print("                                     Generated Summary for Other Columns.")
    return other_columns_stats
