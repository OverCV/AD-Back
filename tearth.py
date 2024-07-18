from itertools import product
import numpy as np


def generate_binary_states(n):
    """
    Generate all possible binary states of length n in little-endian order.
    """
    return np.array(list(product([0, 1], repeat=n)))


def hamming_distance(matrix):
    """
    Compute the Hamming distance matrix between binary vectors.
    """
    n = matrix.shape[0]
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist_matrix[i, j] = np.sum(matrix[i] != matrix[j])
    return dist_matrix


def earth_movers_distance(first_histogram, second_histogram, distance_matrix):
    """
    Compute the Earth Mover's Distance (EMD) between two histograms given a distance matrix.
    """
    n = len(first_histogram)
    flow = np.zeros((n, n))
    emd = 0

    # Iterate over each bin in the first histogram
    for i in range(n):
        for j in range(n):
            # Determine the amount of flow between bins
            flow_amount = min(first_histogram[i], second_histogram[j])
            flow[i, j] = flow_amount
            # Update the EMD value
            emd += flow_amount * distance_matrix[i, j]
            # Update the histograms
            first_histogram[i] -= flow_amount
            second_histogram[j] -= flow_amount

    return emd


# Example usage:
first_histogram = np.array([0, 0, 0, 0, 0.75, 0, 0.25, 0])
second_histogram = np.array([0, 0, 0, 0, 1, 0, 0, 0])

# Generate all possible binary states of length equal to the histogram length
binary_states = generate_binary_states(len(first_histogram))

# Calculate the Hamming distance matrix between these states
distance_matrix = hamming_distance(binary_states)

# Calculate the EMD between the two histograms
emd = earth_movers_distance(first_histogram, second_histogram, distance_matrix)

print('Hamming Distance Matrix:')
print(distance_matrix)
print('EMD:', emd)

# Example usage:
# first_histogram = np.array([0, 0, 0, 0, 0.75, 0, 0.25, 0])
# second_histogram = np.array([0, 0, 0, 0, 1, 0, 0, 0])
# binary_vectors = np.array([[0, 0, 0], [0, 1, 0], [0, 1, 1]])
# distance_matrix = hamming_distance(binary_vectors)
# emd = earth_movers_distance(first_histogram, second_histogram, distance_matrix)

# print('Hamming Distance Matrix:')
# print(distance_matrix)
# print('EMD:', emd)
