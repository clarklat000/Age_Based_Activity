# Use the input function for card1
card1 = int(input("Enter the value of the first card: "))

# Use the input function for card2
card2 = int(input("Enter the value of the second card: "))

# Make a variable called card_sum and set it equal to the sum of the cards
card_sum = card1 + card2

# Use a relational operator to check if the sum is 21 or over
is_21_or_over = card_sum >= 21

# Print the result
print("Is the sum 21 or over?", is_21_or_over)