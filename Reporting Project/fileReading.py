
# handle the differentiation between reading a text file (txt) and a comma-separated values (CSV) file.

# Read the files
def read_file(file_path, fileType):

    # Chucking base on datafile size and memory processing
    #
    print("Reading Data From File.")
    # Read the files
    with open(file_path, "r") as file:
        # Skip the header line
        header = None

        if fileType == "txt":
            # Read as a text file with tab-separated values
            header = file.readline().strip().split("\t")
        elif fileType == "csv":
            # Read as a CSV file
            import csv
            csv_reader = csv.reader(file)
            header = next(csv_reader)  # Read the header row

        # Initialize an empty list to store the data
        data = []

        # Read the rest of the lines
        for line in file:
            # Split the line by tab character if it's a text file, otherwise by comma for CSV
            values = line.strip().split("\t") if fileType == "txt" else line.strip().split(",")

            # Create a dictionary mapping each column header to its corresponding value
            row = {header[i]: values[i] for i in range(len(header))}

            # Append the dictionary to the data list
            data.append(row)
    print("                       Reading Data from file is completed.")
    return data
