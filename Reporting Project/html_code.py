# Generate the HTML table dynamically based on the input data
import pandas as pd
# Open the HTML file in a web browser
import webbrowser


def html_page(file_name, initial_stats, summary_1, summary_2, other_stats):
    # Create DataFrame for stats
    stats_df = pd.DataFrame(list(initial_stats.items()), columns=["Check", "Result"])

    # Add an index column
    stats_df.insert(0, 'Index', range(1, len(stats_df) + 1))

    # Convert DataFrame to HTML table
    html_code_initial_stats = stats_df.to_html(index=False, header=True, classes='dataframe')

    # Transpose the other_stats dictionary
    other_stats_transposed = {
        stat_name: {column_name: other_stats[column_name][stat_name] for column_name in other_stats.keys()} for
        stat_name in other_stats['loginid'].keys()}

    # HTML template
    html_code = f"""
            <html>
            <head>
                <title>Report for {file_name}</title>
            </head>
            <body>
                <h1>Stats Report</h1>
                <h2>Initial Stats</h2>
                <div>
                    <table name="Initial Stats" border="1" class="dataframe">
                        {html_code_initial_stats}
                    </table>
                </div>
                <h2>Numeric Columns Summary - Part 1</h2>
                <div>
                  <table border="1" class="dataframe">
                    <thead>
                      <tr style="text-align: right">
                        <th></th>
    """

    # Add column headers
    for column_name in summary_1.keys():
        html_code += f"<th>{column_name}</th>"
    html_code += "</tr></thead><tbody>"

    # Add row headers and data
    for stat_name, stat_values in summary_1['_id'].items():
        html_code += f"<tr><th>{stat_name}</th>"
        for column_name in summary_1.keys():
            html_code += f"<td>{summary_1[column_name][stat_name]}</td>"
        html_code += "</tr>"

    html_code += """
            </tbody>
          </table>
        </div>
        <h2>Numeric Columns Summary - Part 2</h2>
        <div>
          <table border="1" class="dataframe">
            <thead>
              <tr style="text-align: right">
                <th></th>
    """

    # Add column headers
    for column_name in summary_2.keys():
        html_code += f"<th>{column_name}</th>"
    html_code += "</tr></thead><tbody>"

    # Add row headers and data
    for stat_name in summary_2['longitude'].keys():
        html_code += f"<tr><th>{stat_name}</th>"
        for column_name in summary_2.keys():
            html_code += f"<td>{summary_2[column_name][stat_name]}</td>"
        html_code += "</tr>"

    html_code += """
            </tbody>
          </table>
        </div>
        <h2>Other Columns Summary - Part 1</h2>
        <div>
              <table border="1" class="dataframe">
                <thead>
                  <tr style="text-align: right">
                    <th></th>
        """

    # Add column headers
    for row_name in other_stats_transposed.keys():
        html_code += f"<th>{row_name}</th>"
    html_code += "</tr></thead><tbody>"

    # Add row headers and data
    for column_name in other_stats.keys():
        html_code += f"<tr><th>{column_name}</th>"
        for row_name in other_stats_transposed.keys():
            html_code += f"<td>{other_stats_transposed[row_name][column_name]}</td>"
        html_code += "</tr>"

    html_code += """
                </tbody>
              </table>
            </div>
      </body>
    </html>
    """
    # # Save the HTML code to a file
    with open("summary_stats.html", "w") as file:
        file.write(html_code)

    webbrowser.open("summary_stats.html")


def generate_html_page_initial_stats(file_name, initial_stats):
    # Create DataFrame for stats
    stats_df = pd.DataFrame(list(initial_stats.items()), columns=["Check", "Result"])

    # Add an index column
    stats_df.insert(0, 'Index', range(1, len(stats_df) + 1))

    # Convert DataFrame to HTML table
    html_code_initial_stats = stats_df.to_html(index=False, header=True, classes='dataframe')

    # HTML template
    html_code = f"""
            <html>
            <head>
                <title>Initial Stats Report for {file_name}</title>
            </head>
            <body>
                <h2>Initial Stats</h2>
                <div>
                    <table name="Initial Stats" border="1" class="dataframe">
                        {html_code_initial_stats}
                    </table>
                </div>
      </body>
    </html>
    """
    # # Save the HTML code to a file
    with open("summary_stats.html", "w") as file:
        file.write(html_code)

    webbrowser.open("summary_stats.html")


def generate_html_summary_part(file_name, summary_part, part):
    html_code = f"""
    <html>
      <head>
        <title>Summary {part} Report for {file_name}</title>
      </head>
      <body>
        <h2>Numeric Columns Summary - Part {part}</h2>
        <div>
          <table border="1" class="dataframe">
            <thead>
              <tr style="text-align: right">
                <th></th>
    """

    # Add column headers
    for column_name in summary_part.keys():
        html_code += f"<th>{column_name}</th>"
    html_code += "</tr></thead><tbody>"

    part_condition = ''
    if part == 1:
        part_condition = '_id'
    else:
        part_condition = 'longitude'
    # Add row headers and data
    for stat_name in summary_part[part_condition].keys():
        html_code += f"<tr><th>{stat_name}</th>"
        for column_name in summary_part.keys():
            html_code += f"<td>{summary_part[column_name][stat_name]}</td>"
        html_code += "</tr>"

    html_code += """
            </tbody>
          </table>
        </div>
      </body>
    </html>
    """
    # # Save the HTML code to a file
    with open("summary_stats.html", "w") as file:
        file.write(html_code)

    webbrowser.open("summary_stats.html")


def generate_html_code_other_columns(file_name, other_columns):
    # Transpose the other_columns dictionary
    other_columns_transposed = {
        stat_name: {column_name: other_columns[column_name][stat_name] for column_name in other_columns.keys()} for
        stat_name in other_columns['loginid'].keys()}

    html_code = f"""
    <html>
      <head>
        <title>Other Columns Summary Report for {file_name}</title>
      </head>
      <body>
        <h2>Other Columns Summary - Part 1</h2>
        <div>
          <table border="1" class="dataframe">
            <thead>
              <tr style="text-align: right">
                <th></th>
    """

    # Add column headers
    for row_name in other_columns_transposed.keys():
        html_code += f"<th>{row_name}</th>"
    html_code += "</tr></thead><tbody>"

    # Add row headers and data
    for column_name in other_columns.keys():
        html_code += f"<tr><th>{column_name}</th>"
        for row_name in other_columns_transposed.keys():
            html_code += f"<td>{other_columns_transposed[row_name][column_name]}</td>"
        html_code += "</tr>"

    html_code += """
            </tbody>
          </table>
        </div>
      </body>
    </html>
    """

    # # Save the HTML code to a file
    with open("summary_stats.html", "w") as file:
        file.write(html_code)

    webbrowser.open("summary_stats.html")
