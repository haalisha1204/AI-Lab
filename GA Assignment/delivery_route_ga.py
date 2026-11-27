"""Genetic Algorithm for the fictional A-to-G delivery route assignment."""

import random


DEPOT = "A"
DELIVERY_LOCATIONS = ["B", "C", "D", "E", "F", "G"]

DISTANCES = {
    "A": {"A": 0, "B": 4, "C": 8, "D": 6, "E": 7, "F": 9, "G": 5},
    "B": {"A": 4, "B": 0, "C": 5, "D": 7, "E": 3, "F": 8, "G": 6},
    "C": {"A": 8, "B": 5, "C": 0, "D": 4, "E": 6, "F": 3, "G": 7},
    "D": {"A": 6, "B": 7, "C": 4, "D": 0, "E": 5, "F": 6, "G": 8},
    "E": {"A": 7, "B": 3, "C": 6, "D": 5, "E": 0, "F": 4, "G": 6},
    "F": {"A": 9, "B": 8, "C": 3, "D": 6, "E": 4, "F": 0, "G": 5},
    "G": {"A": 5, "B": 6, "C": 7, "D": 8, "E": 6, "F": 5, "G": 0},
}

POPULATION_SIZE = 100
GENERATIONS = 200
ELITE_COUNT = 2
TOURNAMENT_SIZE = 3
MUTATION_RATE = 0.20
RANDOM_SEED = 42


def route_distance(route):
    """Return the full route distance, including travel back to depot A."""
    complete_route = [DEPOT, *route, DEPOT]
    return sum(
        DISTANCES[complete_route[index]][complete_route[index + 1]]
        for index in range(len(complete_route) - 1)
    )


def tournament_select(population, rng):
    """Choose the shortest route among three randomly sampled candidates."""
    candidates = rng.sample(population, TOURNAMENT_SIZE)
    return min(candidates, key=route_distance)


def order_crossover(parent_a, parent_b, rng):
    """Combine parent segments while retaining every location exactly once."""
    left, right = sorted(rng.sample(range(len(parent_a)), 2))
    child = [None] * len(parent_a)
    child[left : right + 1] = parent_a[left : right + 1]

    remaining = [location for location in parent_b if location not in child]
    write_index = (right + 1) % len(child)
    for location in remaining:
        while child[write_index] is not None:
            write_index = (write_index + 1) % len(child)
        child[write_index] = location

    return child


def swap_mutation(route, rng):
    """Swap two delivery stops to create another valid route."""
    changed_route = route[:]
    first, second = rng.sample(range(len(changed_route)), 2)
    changed_route[first], changed_route[second] = (
        changed_route[second],
        changed_route[first],
    )
    return changed_route


def run_genetic_algorithm():
    rng = random.Random(RANDOM_SEED)
    population = []
    for _ in range(POPULATION_SIZE):
        route = DELIVERY_LOCATIONS[:]
        rng.shuffle(route)
        population.append(route)

    best_distance_history = []

    for _ in range(GENERATIONS):
        population.sort(key=route_distance)
        best_distance_history.append(route_distance(population[0]))
        next_generation = [route[:] for route in population[:ELITE_COUNT]]

        while len(next_generation) < POPULATION_SIZE:
            parent_a = tournament_select(population, rng)
            parent_b = tournament_select(population, rng)
            child = order_crossover(parent_a, parent_b, rng)

            if rng.random() < MUTATION_RATE:
                child = swap_mutation(child, rng)

            next_generation.append(child)

        population = next_generation

    best_route = min(population, key=route_distance)
    return best_route, route_distance(best_route), best_distance_history


def main():
    best_route, best_distance, history = run_genetic_algorithm()
    route_text = " -> ".join([DEPOT, *best_route, DEPOT])

    assert len(best_route) == len(DELIVERY_LOCATIONS)
    assert set(best_route) == set(DELIVERY_LOCATIONS)
    assert history[-1] <= history[0]

    print("GENETIC ALGORITHM — DELIVERY ROUTE")
    print(f"Random seed: {RANDOM_SEED}")
    print(f"Population: {POPULATION_SIZE} | Generations: {GENERATIONS}")
    print(f"Best route: {route_text}")
    print(f"Total distance: {best_distance} km")
    print(f"Initial best distance: {history[0]} km")
    print(f"Final best distance: {history[-1]} km")


if __name__ == "__main__":
    main()
