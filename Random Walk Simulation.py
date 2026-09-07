import random

Number_of_steps = int(input("Enter the number of steps for the random walk simulation: "))

starting_position = 0
step_sizes = [1, -1]
positions = [starting_position]
current_step = 0
current_position = starting_position
final_position = 0

while current_step <= Number_of_steps:
    step = random.choice(step_sizes)
    current_position += step
    positions.append(current_position)
    current_step += 1

final_position = current_position
print(positions)