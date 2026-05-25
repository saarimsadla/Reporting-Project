import pandas as pd
# this is used to get the directory of the current script
import os
# this is used for import data and time for naming of output files
from datetime import datetime
# this import hold code of read data from file
from fileReading import read_file
# this returns summary for requested columns
from summary import calculate_Initial_Stats, generate_summary_stats, generate_Other_Columns_Summary

from html_code import html_page, generate_html_page_initial_stats, generate_html_summary_part, generate_html_code_other_columns


def mainFunction():
    # # Getting the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # # update file name here and make sure your file exists in files folder within project directory
    file_name = 'CC_Dom_Customer_extract_231226_V7.txt'

    # # Construct the path to the text files
    file_path = os.path.join(current_dir, 'files', file_name)

    # # Data file is txt then fileType will be set to 'txt' otherwise if file is csv then fileType will be set to 'csv'
    # # for below read_file function class data from files
    data = read_file(file_path, file_name.rsplit('.', 1)[-1])
    # # Print the data
    # for row in data:
    #   print(row)

    # # Convert data to DataFrame
    df = pd.DataFrame(data)
    # # will print first 5 data frame rows
    # print(df.head(5))

    # # # # Initial Stats

    # # Calculate summary statistics
    initial_stats = calculate_Initial_Stats(df)
    # # Print the summary statistics DataFrame
    # print(initial_stats)

    # # # # Numeric Columns Summary

    # # # # Numeric Columns Summary - Part 1
    summary_part_1 = generate_summary_stats(df, 1)
    # print(columns_summary_part_1)

    # # # # Numeric Columns Summary - Part 2
    summary_part_2 = generate_summary_stats(df, 2)
    # print(columns_summary_part_2)

    # # # # Other Columns Summary
    other_Columns_Summary = generate_Other_Columns_Summary(df)
    # print(other_Columns_Summary)

    # # # # set htmlOrCsv to "HTML" if you wants to view html page or if you want to generate "CSV"
    htmlOrCsv = "HTML"

    if htmlOrCsv == "HTML":
        # Call the function with the provided data

        # # # # this will only generate initial stats html page
        # generate_html_page_initial_stats(
        #     file_name=file_name,
        #     initial_stats=initial_stats)

        # # # # this will only generate Numeric Columns Summary - Part 1 html page
        # generate_html_summary_part(file_name=file_name,
        #                            summary_part=summary_part_1,
        #                            part=1)

        # # # # this will only generate Numeric Columns Summary - Part 2 html page
        # generate_html_summary_part(file_name=file_name,
        #                            summary_part=summary_part_2,
        #                            part=2)

        # # # # this will only generate Other Columns Summary - Part 1 html page
        # generate_html_code_other_columns(
        #     file_name=file_name,
        #     other_columns=other_Columns_Summary)

        # # # # This will generate complete Stats html page
        html_page(
            file_name=file_name,
            initial_stats=initial_stats,
            summary_1=summary_part_1,
            summary_2=summary_part_2,
            other_stats=other_Columns_Summary)

    else:
        print('Coming Soon. Please bear with us. Love')
    #     # # Save  Initial Stats  to CSV file
    #     # if initial_stats:
    #     #
    #     #     # # Get the current date and time
    #          current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
    #     #
    #     #     # # Define the filename with the specified format
    #     #     filename = f"initial_stats_{current_datetime}.csv"
    #     #
    #     #     # # Write the DataFrame to a CSV file
    #     #     initial_stats_df.to_csv(filename, index=False)
    #     #
    #     #     print(f"Summary statistics saved to {filename}")


# end of mainFunction() function


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print()
    mainFunction()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
