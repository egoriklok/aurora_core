# Create an agent that calculates the sum of a list of numbers and saves result to a log file

def calculate_sum(numbers):
    result = sum(numbers)
    return result

numbers = [1, 2, 3, 4, 5]
sum_result = calculate_sum(numbers)

# Write the result to a log file
with open('sum_log.txt', 'w') as file:
    file.write(f'The sum of the numbers {numbers} is: {sum_result}')
