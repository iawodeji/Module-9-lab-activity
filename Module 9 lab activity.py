#Idris Awodeji
#8.26.24

#Problem 1
while True:
    print("Infinite")


#Problem 2
# Initializes the list and counter variable
L = []
counter = 0

# Loop until counter is greater than 10
while counter <= 10:
    L.append(counter)  # Appends current value of counter to the list
    counter += 1       # Increments the counter by 1

print(L)  


#Problem 3
# Initialize an empty list and a sum variable
numbers = []
total_sum = 0

# Loop until the sum of the list is greater than 100
while total_sum <= 100:
    # Asks user to enter a number
    user_input = input("Enter a number: ")
    
    try:
        # Converts input to a float and add it to the list
        number = float(user_input)
        numbers.append(number)
        
        # Updates total sum
        total_sum += number
    except ValueError:
        print("Please enter a valid number.")

print("Numbers entered:", numbers)
print("Total sum:", total_sum)


#Problem 4
# Initializes counter and the list
counter = 0
tens = []

# Loop until the counter reaches 50
while counter <= 50:
    # Checks if counter value is divisible by 10
    if counter % 10 == 0:
        tens.append(counter)
    
    # Increment the counter
    counter += 1

# Print the list of values divisible by 10
print("List of numbers divisible by 10:", tens)
