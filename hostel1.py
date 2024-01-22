# Assuming your data is stored in a CSV file with the following format:
# Hostel,Amount
# Hostel A,100
# Hostel B,200
# Hostel A,150
# Hostel C,300
# ...

import csv

# Dictionary to store the sum for each hostel
hostel_sums = {}

# Open the CSV file
with open('data.csv', 'r') as file:
    # Create a CSV reader object
    reader = csv.reader(file)
    
    # Skip the header row
    next(reader)
    
    # Process each row
    for row in reader:
        hostel = row[0]
        amount = int(row[1])
        
        # Add the amount to the sum of the hostel
        if hostel in hostel_sums:
            hostel_sums[hostel] += amount
        else:
            hostel_sums[hostel] = amount

# Print the sum for each hostel
for hostel, total in hostel_sums.items():
    print(f"{hostel}: {total}")
