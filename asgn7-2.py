# Use the file name mbox-short.txt as the file name
# Prompt the user for the file name
fname = input("Enter file name: ")

# Initialize variables to keep track of the total sum and the count of lines
fh = open(fname)
total = 0.0
count = 0

# Iterate over each line in the file
for line in fh:
    # Check if the line starts with "X-DSPAM-Confidence:"
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
# Extract the floating point number from the line
# Split the line at "X-DSPAM-Confidence:" and get the second part, then strip any extra spaces
    else:
        value = line.split(':')[1].strip()

        # Convert the extracted string to a float
        number = float(value)

        # Add the number to the total
        total = total + number

         # Increment the count
        count = count + 1
# Compute the average of the values
# Avoid using sum() by manually summing the values with a variable   
average = total/count

# Print the average value
print('Average spam confidence:',average)
        