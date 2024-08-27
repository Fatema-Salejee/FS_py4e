# Prompt user for file name
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"  # Default to "mbox-short.txt" if no name is provided

handle = open(name)  # Open the file
senders = {}  # Initialize an empty dictionary to store email counts

# Process each line in the file
for line in handle:
    if line.startswith("From "):  # Check if the line starts with "From "
        words = line.split()  # Corrected: Call split() method properly
        email = words[1]  # Extract the email address
        senders[email] = senders.get(email, 0) + 1  # Update the count in the dictionary

max_count = None
prolific_sender = None  # Corrected: Capitalize None

# Find the email address with the highest count
for email, count in senders.items():
    if max_count is None or count > max_count:
        max_count = count
        prolific_sender = email  # Corrected: Use the assignment operator =

# Print the most prolific sender and their email count
print(prolific_sender, max_count)