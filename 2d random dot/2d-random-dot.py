# OP3N1T SECURITY
import matplotlib.pyplot as plt
import numpy as np

def generate_and_save_dots(num_dots, file_name, min_dot_size=10, max_dot_size=40):

    # Generate random coordinates for the dots
    x_coords = np.random.rand(num_dots)
    y_coords = np.random.rand(num_dots)

    # Generate random dot sizes with a non-linear distribution (quadratic)
    dot_sizes = np.random.randint(min_dot_size, max_dot_size + 1, size=num_dots)
    weights = np.linspace(1, 100, num_dots)**2  # Adjust the range based on your preferences
    weights /= weights.sum()  # Normalize weights to make the sum equal to 1

    # Create a scatter plot with random dot sizes
    plt.scatter(x_coords, y_coords, color='blue', marker='.', s=dot_sizes, alpha=0.7)

    plt.xlim(0, 1)
    plt.ylim(0, 1)

    plt.title(f'{num_dots} Random Dots')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')

    plt.savefig(file_name)
    plt.show()

generate_and_save_dots(900, 'random_dots.png', min_dot_size=10, max_dot_size=140)
