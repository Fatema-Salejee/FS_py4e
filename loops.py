# Counting example
count = 0
for i in range(1, 6):
    count += 1
    print("Count:", count)

# Totaling up values example
total = 0
for num in [5, 10, 15, 20]:
    total += num
print("Total:", total)

# Computing averages example
numbers = [2, 4, 6, 8, 10]
sum = 0
count = 0
for num in numbers:
    sum += num
    count += 1
average = sum / count
print("Average:", average)

# Filtering example
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print("Even numbers:", even_numbers)

# Finding the smallest value example
numbers = [9, 5, 12, 3, 7]
smallest = None
for num in numbers:
    if smallest is None or num < smallest:
        smallest = num
print("Smallest number:", smallest)