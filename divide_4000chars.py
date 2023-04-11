import csv

# Open the input and output files
with open('input.csv', 'r') as infile, open('output.csv', 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Iterate over each row in the input file
    for row in reader:
        # Check if the column needs to be split
        if len(row[3]) > 4000:
            # Split the column into multiple columns of 4000 characters each
            chunks = [row[3][i:i+4000] for i in range(0, len(row[3]), 4000)]
            # Replace the original column with the split columns
            row = row[:3] + chunks + row[4:]
        # Write the row to the output file
        writer.writerow(row)
