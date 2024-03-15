import numpy as np

# random chord length strategy (function generation)
def generate_random_chord_length(n_samples):
    return np.random.rand(n_samples)

# random chord endpoint strategy (function generation)
def generate_random_chord_endpoint(n_samples):
    return np.cos(np.random.uniform(0.0, 2 * np.pi, n_samples))
    

# random radius strategy (function generation)
def generate_random_radius(n_samples):
    return 1 - 2 * np.random.rand(n_samples)

# estimating the probability of the chord to be greater than the half
def estimate_probability(samples):
    count = np.sum(samples > 0.5)
    return count / len(samples)

def main():
    n_samples = 10000000

    radii = generate_random_radius(n_samples)
    probability_radius = estimate_probability(radii)
    print("Probability (random radius method):", probability_radius)

    chord_endpoints = generate_random_chord_endpoint(n_samples)
    probability_chord_endpoint = estimate_probability(chord_endpoints)
    print("Probability (random chord endpoint method):", probability_chord_endpoint)

    chord_lengths = generate_random_chord_length(n_samples)
    probability_chord_length = estimate_probability(chord_lengths)
    print("Probability (random chord length method):", probability_chord_length)

if __name__ == "__main__":
    main()
