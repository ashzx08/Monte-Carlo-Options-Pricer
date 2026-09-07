import random
import numpy as np
import matplotlib.pyplot as plt

Number_of_steps = 100
Number_of_walks = 10000
final_positions = []

def random_walk_simulation():
    starting_position = 0
    step_sizes = [1, -1]
    positions = [starting_position]
    current_step = 0
    current_position = starting_position

    for _ in range(Number_of_steps):
        step = random.choice(step_sizes)
        current_position += step
        positions.append(current_position)
        current_step += 1

    return current_position

for _ in range(Number_of_walks):
    final_position = random_walk_simulation()
    final_positions.append(final_position)

numpy_final_positions = np.array(final_positions)
average_final_position = np.mean(numpy_final_positions)
std_final_position = np.std(numpy_final_positions)
max_final_position = np.max(numpy_final_positions)
min_final_position = np.min(numpy_final_positions)

print(f"Average final position: {average_final_position}")
print(f"Standard deviation of final positions: {std_final_position}")
print(f"Maximum final position: {max_final_position}")
print(f"Minimum final position: {min_final_position}")

plt.hist(numpy_final_positions)
plt.title("Histogram of Final Positions in Random Walk Simulation")
plt.show()