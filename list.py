# Prompt the user to enter file name
fname = input("Enter file name: ")

# Open and read the file
fh = open(fname)

# Initialize an empty list to store unique words
lst = list()

# Loop through each line in the file
for line in fh:
    # Split the line into a list of words
    words = line.split()
    # Loop through each word in the line
    for word in words:
        # Check if the word is not already in the list
        if word not in lst:
            # If it's not in the list, append it
            lst.append(word)

# Sort the list of words in alphabetical order
lst.sort()

# Print the sorted list of words
print(lst)