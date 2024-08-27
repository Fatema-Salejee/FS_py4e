# Prompt user for file name
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"  # Default to "mbox-short.txt" if no name is provided

handle = open(name)  # Open the file
hour_counts = {}  # Initialize an empty dictionary to store hour counts

# Process each line in the file
for line in handle:
    if line.startswith("From "):  # Check if the line starts with "From "
        words = line.split()  # Split the line into a list of words
        time = words[5]  # Extract the time (which is the 5th word)
        hour = time.split(":")[0]  # Split the time by ":" and extract the hour
        hour_counts[hour] = hour_counts.get(hour, 0) + 1  # Update the count for the hour

# Sort the dictionary by hour and print the results
for hour in sorted(hour_counts.keys()):
    print(hour, hour_counts[hour])