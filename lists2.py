# Prompt the user to enter file name
fname = input("Enter file name: ")
#if len(fname) < 1:
    #fname = "mbox-short.txt"

# Open and read the file
fh = open(fname)

# Initialize a counter to track the number of lines starting with 'From '
count = 0

# Loop through each line in the file
for line in fh:
         
         # Check if the line starts with "From "
        if line.startswith("From "):
            
            # Split the line into a list of words
            words = line.split()
            
            # Print the second word in the line (the email address)
            print(words[1])
            
            # Increment the count
            count = count + 1

# Print the final count of lines starting with "From "
print("There were", count, "lines in the file with From as the first word")
